#!/usr/bin/env python3
"""Collect decision-level (state, options, choice, outcome) data for Archaludon vs Iono.

Why this exists
---------------
The Iono matchup is the fleet's #1 bottleneck. Rule levers are exhausted
(``configs/iono_tomato_train.yaml``: rule ceiling ~32%, tomato hybrid ~50% pooled,
floor is 55%). Breaking it needs a *learned* re-ranker, and there was no
Archaludon learning path at all — only the Lucario MCTS trainer, which the iono
config explicitly forbids retraining for this gate.

This script is the data half of that path. It plays real gate games (same engine,
same opponent brain as ``scripts/gate_archaludon.py``) and logs, for every hero
decision, a fixed-width state feature vector plus per-option feature vectors and
which option the current rule agent actually picked. Games are labelled with the
final outcome, so the dump trains either

  * a value head (state -> P(win)), or
  * a decision prior / re-ranker (state+option -> advantage),

which can then be wired in as a new ``ARCH_IONO_LEVER`` branch.

The hero agent is *not* modified: we wrap the brain callable, so collection is
observation-only and cannot change gate behaviour.

Usage
-----
  python scripts/collect_iono_decisions.py --games 200 --opponent real_iono
  python scripts/collect_iono_decisions.py --games 2000 --out episodes/iono_bc

Output: ``<out>/iono_decisions_<tag>.jsonl`` (one JSON object per game) plus a
``.meta.json`` summary. Shard-safe: honours ``PTCG_SHARD`` for the filename.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE_DIR = ROOT / "data" / "sim" / "sample_submission"
for p in (str(ENGINE_DIR), str(ROOT)):
    if p not in sys.path:
        sys.path.insert(0, p)

from cg import game  # noqa: E402
from cg.api import OptionType, SelectContext, to_observation_class  # noqa: E402
from cg.sim import Battle, lib  # noqa: E402

from eval.field_registry import load_registry, opponent_meta, resolve_deck_path  # noqa: E402
from eval.harness import (  # noqa: E402
    DEFAULT_ARCHALUDON_DECK,
    MAX_STEPS,
    get_opponent_brain,
    load_deck,
    make_archaludon_brain,
)

# Iono-relevant card ids, mirrored from agent/archaludon_agent.py so the feature
# layout stays readable without importing the whole agent module namespace.
DURALUDON = 169
ARCHALUDON_EX = 190
CINDERACE = 666
RELICANTH = 57
IONO_THREATS = {269, 271}  # Bellibolt ex / Kilowattrel

OPTION_TYPES = [
    OptionType.PLAY,
    OptionType.ATTACH,
    OptionType.EVOLVE,
    OptionType.ABILITY,
    OptionType.RETREAT,
    OptionType.ATTACK,
    OptionType.END,
    OptionType.CARD,
    OptionType.ENERGY,
]
OPTION_TYPE_INDEX = {t: i for i, t in enumerate(OPTION_TYPES)}

STATE_FEATURES = [
    "turn", "my_prize", "opp_prize", "hand", "deck", "discard",
    "my_bench", "opp_bench",
    "act_hp", "act_dmg", "act_energy", "act_is_dura", "act_is_arch",
    "act_is_cinder", "act_is_relic", "act_is_none",
    "opp_hp", "opp_dmg", "opp_energy", "opp_is_ex", "opp_is_threat",
    "ctx_main", "ctx_setup", "ctx_switch", "n_options",
]
OPTION_FEATURES = [
    f"type_{t.name.lower()}" for t in OPTION_TYPES
] + ["card_id", "is_pokemon_card", "is_energy_card", "targets_opponent"]


def _i(x, default: int = 0) -> int:
    try:
        return int(x)
    except Exception:
        return default


def _pokemon_features(pkm) -> list[float]:
    """[hp_remaining, damage, energy_count] for a board slot (zeros if empty)."""
    if pkm is None:
        return [0.0, 0.0, 0.0]
    return [
        float(_i(getattr(pkm, "hp", 0))),
        float(_i(getattr(pkm, "damage", 0))),
        float(len(getattr(pkm, "energies", None) or [])),
    ]


def _side(obs, mine: bool):
    """Return the board side object for hero (mine=True) or opponent."""
    for attr in (("your", "opponent") if mine else ("opponent", "your")):
        side = getattr(obs, attr, None)
        if side is not None:
            return side
    return None


def state_vector(obs) -> list[float]:
    """Fixed-width state features. Never raises; unknown fields become 0."""
    me = _side(obs, True)
    opp = _side(obs, False)

    act = getattr(me, "active", None) if me is not None else None
    oact = getattr(opp, "active", None) if opp is not None else None
    act_hp, act_dmg, act_en = _pokemon_features(act)
    opp_hp, opp_dmg, opp_en = _pokemon_features(oact)

    act_id = _i(getattr(act, "id", 0)) if act is not None else 0
    opp_id = _i(getattr(oact, "id", 0)) if oact is not None else 0

    ctx = getattr(getattr(obs, "select", None), "context", None)
    ctx_name = str(getattr(ctx, "name", ctx) or "").upper()
    n_opts = len(getattr(getattr(obs, "select", None), "option", None) or [])

    return [
        float(_i(getattr(getattr(obs, "current", None), "turn", 0))),
        float(len(getattr(me, "prize", None) or [])) if me is not None else 0.0,
        float(len(getattr(opp, "prize", None) or [])) if opp is not None else 0.0,
        float(len(getattr(me, "hand", None) or [])) if me is not None else 0.0,
        float(_i(getattr(me, "deck", 0))) if me is not None else 0.0,
        float(len(getattr(me, "discard", None) or [])) if me is not None else 0.0,
        float(len(getattr(me, "bench", None) or [])) if me is not None else 0.0,
        float(len(getattr(opp, "bench", None) or [])) if opp is not None else 0.0,
        act_hp, act_dmg, act_en,
        float(act_id == DURALUDON),
        float(act_id == ARCHALUDON_EX),
        float(act_id == CINDERACE),
        float(act_id == RELICANTH),
        float(act is None),
        opp_hp, opp_dmg, opp_en,
        float(bool(getattr(oact, "ex", False) or getattr(oact, "megaEx", False))) if oact is not None else 0.0,
        float(opp_id in IONO_THREATS),
        float(ctx_name == "MAIN"),
        float(ctx_name.startswith("SETUP")),
        float(ctx_name in ("SWITCH", "TO_ACTIVE", "TO_BENCH")),
        float(n_opts),
    ]


def option_vector(obs, opt) -> list[float]:
    """Fixed-width per-option features."""
    vec = [0.0] * len(OPTION_TYPES)
    otype = getattr(opt, "type", None)
    idx = OPTION_TYPE_INDEX.get(otype)
    if idx is not None:
        vec[idx] = 1.0

    card_id = 0
    is_pkm = 0.0
    is_energy = 0.0
    try:
        card = getattr(opt, "card", None)
        if card is not None:
            card_id = _i(getattr(card, "id", 0))
            is_pkm = float(getattr(card, "hp", 0) or 0 > 0)
            is_energy = float(bool(getattr(card, "energyType", None)))
    except Exception:
        pass

    targets_opp = 0.0
    try:
        area = getattr(opt, "area", None)
        area_name = str(getattr(area, "name", area) or "").upper()
        targets_opp = float("OPPONENT" in area_name)
    except Exception:
        pass

    return vec + [float(card_id), is_pkm, is_energy, targets_opp]


class _Recorder:
    """Wraps the hero brain and records every decision it makes."""

    def __init__(self, brain):
        self._brain = brain
        self.decisions: list[dict] = []

    def __call__(self, obs_dict):
        picked = self._brain(obs_dict)
        try:
            obs = to_observation_class(obs_dict)
            select = getattr(obs, "select", None)
            options = list(getattr(select, "option", None) or []) if select else []
            if options:
                self.decisions.append({
                    "s": [round(v, 3) for v in state_vector(obs)],
                    "o": [[round(v, 3) for v in option_vector(obs, o)] for o in options],
                    "pick": list(picked) if isinstance(picked, list) else [],
                })
        except Exception:
            pass  # collection must never perturb the game
        return picked

    def reset(self) -> list[dict]:
        out = self.decisions
        self.decisions = []
        return out


def _select_player() -> int:
    return lib.GetBattleData(Battle.battle_ptr).selectPlayer


def play_one(deck_a, deck_b, brain_a, brain_b) -> str:
    """Copy of eval.harness.run_match — inlined so we own the game boundary."""
    obs, start = game.battle_start(deck_a, deck_b)
    if obs is None:
        raise RuntimeError(f"battle_start failed: err={getattr(start, 'errorType', '?')}")
    policies = (brain_a, brain_b)
    try:
        for _ in range(MAX_STEPS):
            cur = obs["current"]
            if cur is not None and cur.get("result", -1) != -1:
                r = cur["result"]
                return {0: "a", 1: "b", 2: "draw"}.get(r, "unfinished")
            if obs["select"] is None:
                return "unfinished"
            obs = game.battle_select(policies[_select_player()](obs))
        return "unfinished"
    finally:
        game.battle_finish()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--games", type=int, default=200)
    ap.add_argument("--opponent", default="real_iono")
    ap.add_argument("--out", default="episodes/iono_bc")
    ap.add_argument("--hero-deck", default=None)
    ap.add_argument("--losses-only", action="store_true",
                    help="Only keep lost games (oversample the failure mode)")
    ap.add_argument("--max-decisions", type=int, default=0,
                    help="Stop early once this many decisions are logged (0 = no cap)")
    args = ap.parse_args()

    shard = os.environ.get("PTCG_SHARD", "0")
    lever = os.environ.get("ARCH_IONO_LEVER", "tomato")

    out_dir = ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    tag = f"{args.opponent}_{lever}_s{shard}_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}"
    out_path = out_dir / f"iono_decisions_{tag}.jsonl"

    hero_deck_path = args.hero_deck or DEFAULT_ARCHALUDON_DECK
    hero_deck = load_deck(hero_deck_path)
    brain = make_archaludon_brain(hero_deck_path)
    rec = _Recorder(brain)

    reg = load_registry()
    opponent_meta(args.opponent, reg)  # fail fast on unknown opponent
    deck_path = resolve_deck_path(args.opponent, reg)
    if not deck_path.exists():
        print(f"ERROR: opponent deck not found: {deck_path}", file=sys.stderr)
        return 1
    deck_o = load_deck(deck_path)
    opp_brain, opp_label = get_opponent_brain(args.opponent, registry=reg)

    wins = losses = other = 0
    n_decisions = 0
    n_games_written = 0
    t0 = time.time()

    with out_path.open("w", encoding="utf-8") as f:
        for i in range(args.games):
            rec.reset()
            # Seat swap on odd games, matching eval.harness.gate_vs_opponent so
            # the collected distribution matches the gate we are measured on.
            hero_first = (i % 2 == 0)
            if hero_first:
                outcome = play_one(hero_deck, deck_o, rec, opp_brain)
                hero_won = outcome == "a"
                hero_lost = outcome == "b"
            else:
                outcome = play_one(deck_o, hero_deck, opp_brain, rec)
                hero_won = outcome == "b"
                hero_lost = outcome == "a"

            if hero_won:
                wins += 1
            elif hero_lost:
                losses += 1
            else:
                other += 1

            decisions = rec.reset()
            if args.losses_only and not hero_lost:
                continue
            if not decisions:
                continue
            f.write(json.dumps({
                "game": i,
                "hero_first": hero_first,
                "outcome": outcome,
                "label": 1 if hero_won else (0 if hero_lost else -1),
                "n_decisions": len(decisions),
                "decisions": decisions,
            }, ensure_ascii=False) + "\n")
            n_games_written += 1
            n_decisions += len(decisions)

            if i and i % 20 == 0:
                n = wins + losses
                wr = 100.0 * wins / n if n else 0.0
                print(f"[collect] {i}/{args.games} wr={wr:.1f}% "
                      f"decisions={n_decisions} {time.time() - t0:.0f}s", flush=True)
            if args.max_decisions and n_decisions >= args.max_decisions:
                print(f"[collect] decision cap {args.max_decisions} reached at game {i}", flush=True)
                break

    n = wins + losses
    wr = 100.0 * wins / n if n else 0.0
    meta = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "opponent": args.opponent,
        "opponent_brain": opp_label,
        "lever": lever,
        "shard": shard,
        "hero_deck": str(hero_deck_path),
        "games": wins + losses + other,
        "wins": wins, "losses": losses, "other": other,
        "wr_pct": round(wr, 2),
        "games_written": n_games_written,
        "decisions": n_decisions,
        "losses_only": args.losses_only,
        "state_features": STATE_FEATURES,
        "option_features": OPTION_FEATURES,
        "elapsed_s": round(time.time() - t0, 1),
        "path": str(out_path),
    }
    (out_path.with_suffix(".meta.json")).write_text(
        json.dumps(meta, indent=2), encoding="utf-8")

    # Shard-Gate.ps1 pools on this line, so a collection run doubles as a gate.
    print(f"\n{args.opponent} (gated) {wr:.1f}%  n={n}")
    print(f"OVERALL (gated) {wr:.1f}%")
    print(f"[collect] wrote {n_games_written} games / {n_decisions} decisions -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
