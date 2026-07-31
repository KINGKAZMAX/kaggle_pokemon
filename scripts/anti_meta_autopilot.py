#!/usr/bin/env python3
"""Unattended local-compute autopilot for climbing toward first place.

Scope:
  - local data collection / training / gates only
  - no Kaggle submission
  - no ship-floor changes

The loop spends spare compute on the current blockers:
  1. expand schema-v2 Iono data,
  2. train option-outcome Q and prior candidates,
  3. run smoke gates for safe rule candidates,
  4. write an always-readable dashboard.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
METRICS = ROOT / "recordings" / "metrics"
REPORT = ROOT / "report" / "anti_meta_train"
METRICS.mkdir(parents=True, exist_ok=True)
REPORT.mkdir(parents=True, exist_ok=True)


def ts() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run(cmd: list[str], *, env: dict[str, str] | None = None, timeout: int = 14400) -> dict[str, Any]:
    start = time.time()
    p = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        env={**os.environ, **(env or {})},
        timeout=timeout,
    )
    out = (p.stdout or "") + (p.stderr or "")
    return {
        "cmd": cmd,
        "env": env or {},
        "rc": p.returncode,
        "elapsed_s": round(time.time() - start, 1),
        "tail": out[-6000:],
    }


def parse_wr(out: str) -> dict[str, float]:
    vals: dict[str, float] = {}
    for m in re.finditer(r"^(\S+)\s+\([^)]*\)\s+([0-9]+(?:\.[0-9]+)?)\s*%", out, re.M):
        vals[m.group(1)] = float(m.group(2))
    m = re.search(r"OVERALL \(gated\)\s+([0-9]+(?:\.[0-9]+)?)\s*%", out)
    if m:
        vals["OVERALL"] = float(m.group(1))
    return vals


def latest_json(pattern: str) -> dict[str, Any] | None:
    files = sorted(ROOT.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return None
    try:
        data = json.loads(files[0].read_text(encoding="utf-8"))
        data["_path"] = str(files[0])
        return data
    except Exception as e:
        return {"_path": str(files[0]), "error": str(e)}


def director_snapshot() -> dict[str, Any]:
    scripts_dir = str(ROOT / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        from director_gate import evaluate_ship, load_ship_snapshot  # type: ignore
        from auto_submit import submits_today  # type: ignore

        snap = load_ship_snapshot()
        used = submits_today()
        verdict = evaluate_ship(snap, submits_today=used) if snap else None
        return {
            "submits_today": used,
            "snapshot": snap.__dict__ if snap else None,
            "verdict": verdict.__dict__ if verdict else None,
        }
    except Exception as e:
        return {"error": str(e)}


def write_dashboard(payload: dict[str, Any]) -> None:
    latest = METRICS / "anti_meta_autopilot_latest.json"
    latest.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    with (METRICS / "anti_meta_autopilot_history.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    d = payload.get("director", {})
    snap = d.get("snapshot") or {}
    verdict = d.get("verdict") or {}
    q = payload.get("latest_q") or {}
    prior = payload.get("latest_prior") or {}
    gates = payload.get("smoke_gates") or []
    lines = [
        "# Anti-meta autopilot",
        "",
        f"Updated: `{payload['ts_utc']}`",
        f"Cycle: `{payload['cycle']}`",
        "",
        "## Ship status",
        "",
        f"- Decision: `{verdict.get('decision', 'unknown')}`",
        f"- Reasons: {', '.join(verdict.get('reasons') or []) or 'none'}",
        f"- Iono: {snap.get('iono')}",
        f"- Crustle min: {snap.get('crustle_min')}",
        f"- Arch: {snap.get('arch_overall')}",
        f"- Dual: {snap.get('dual_overall')}",
        f"- Submits today: {d.get('submits_today')}/5",
        "",
        "## Latest learned artifacts",
        "",
        f"- Option-Q: `{q.get('_path')}` best_bce={q.get('best_val_bce')} acc={q.get('best_val_acc')}",
        f"- Prior/BC: `{prior.get('_path')}` win_multi_top1={q.get('best_val_win_multi_top1') or prior.get('best_val_win_multi_top1')}",
        "",
        "## Smoke gates",
        "",
        "| candidate | rc | real_iono | overall |",
        "|---|---:|---:|---:|",
    ]
    for g in gates:
        wr = g.get("wrs") or {}
        lines.append(f"| {g.get('name')} | {g.get('rc')} | {wr.get('real_iono')} | {wr.get('OVERALL')} |")
    lines += [
        "",
        "Autopilot is local-only. It never submits to Kaggle.",
        "",
    ]
    (REPORT / "ANTI_META_AUTOPILOT.md").write_text("\n".join(lines), encoding="utf-8")


def gate_candidate(name: str, env: dict[str, str], games: int) -> dict[str, Any]:
    step = run(
        [PY, "-u", "scripts/gate_archaludon.py", "--games", str(games), "--opponents", "real_iono"],
        env=env,
        timeout=7200,
    )
    step["name"] = name
    step["wrs"] = parse_wr(step["tail"])
    return step


def one_cycle(args: argparse.Namespace, cycle: int) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "ts_utc": ts(),
        "cycle": cycle,
        "args": vars(args),
        "director": director_snapshot(),
        "steps": [],
    }

    if args.collect_games > 0:
        payload["steps"].append(run([
            PY, "-u", "scripts/collect_iono_decisions.py",
            "--games", str(args.collect_games),
            "--out", args.data,
            "--opponent", "real_iono",
        ], env={"ARCH_IONO_LEVER": "tomato"}, timeout=14400))

    payload["steps"].append(run([
        PY, "-u", "scripts/analyze_iono_loss_clusters.py",
        "--data", args.data,
        "--out", "recordings/intel/iono_loss_clusters",
    ], timeout=1800))

    payload["steps"].append(run([
        PY, "-u", "scripts/train_iono_option_q.py",
        "--data", args.data,
        "--out", "artifacts/iono_q_v2",
        "--device", args.device,
        "--epochs", str(args.q_epochs),
        "--batch-size", str(args.batch_size),
        "--loss-weight", "2.0",
        "--fragile-loss-weight", "3.0",
        "--fragile-win-weight", "1.5",
    ], timeout=14400))

    if args.train_prior:
        payload["steps"].append(run([
            PY, "-u", "scripts/train_iono_prior.py",
            "--data", args.data,
            "--out", "artifacts/iono_prior_v2",
            "--device", args.device,
            "--epochs", str(args.prior_epochs),
            "--batch-size", str(args.batch_size),
            "--objective", "pos",
            "--select-on", "prior",
            "--loss-weight", "2.0",
            "--fragile-loss-weight", "3.0",
            "--fragile-win-weight", "1.5",
        ], timeout=14400))

    gates = [
        gate_candidate("tomato", {"ARCH_IONO_LEVER": "tomato"}, args.gate_games),
        gate_candidate("tomato_fork_floor2", {
            "ARCH_IONO_LEVER": "tomato_fork",
            "ARCH_IONO_FORK_FLOOR": "2",
        }, args.gate_games),
        gate_candidate("tomato_fork_floor3", {
            "ARCH_IONO_LEVER": "tomato_fork",
            "ARCH_IONO_FORK_FLOOR": "3",
        }, args.gate_games),
    ]
    payload["smoke_gates"] = gates
    payload["latest_q"] = latest_json("artifacts/iono_q_v2/iono_option_q_*.json")
    payload["latest_prior"] = latest_json("artifacts/iono_prior_v2/iono_prior_*.json")
    write_dashboard(payload)
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default="episodes/iono_bc_v2")
    ap.add_argument("--collect-games", type=int, default=1200)
    ap.add_argument("--gate-games", type=int, default=80)
    ap.add_argument("--device", default="auto", choices=("auto", "cuda", "cpu"))
    ap.add_argument("--batch-size", type=int, default=8192)
    ap.add_argument("--q-epochs", type=int, default=40)
    ap.add_argument("--prior-epochs", type=int, default=20)
    ap.add_argument("--train-prior", action="store_true")
    ap.add_argument("--cycles", type=int, default=0, help="0 = forever")
    ap.add_argument("--sleep-sec", type=int, default=60)
    args = ap.parse_args()

    cycle = 0
    while True:
        cycle += 1
        payload = one_cycle(args, cycle)
        print(json.dumps({
            "cycle": cycle,
            "decision": (payload.get("director", {}).get("verdict") or {}).get("decision"),
            "dashboard": str(REPORT / "ANTI_META_AUTOPILOT.md"),
            "latest": str(METRICS / "anti_meta_autopilot_latest.json"),
        }, ensure_ascii=False), flush=True)
        if args.cycles and cycle >= args.cycles:
            return 0
        time.sleep(max(1, args.sleep_sec))


if __name__ == "__main__":
    raise SystemExit(main())
