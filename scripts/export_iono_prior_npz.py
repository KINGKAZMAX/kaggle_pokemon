#!/usr/bin/env python3
"""Export the inference-only Iono prior weights from torch to a NumPy archive."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import torch


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("checkpoint")
    ap.add_argument("--out", default="artifacts/iono_prior_best.npz")
    args = ap.parse_args()

    src = Path(args.checkpoint)
    dst = Path(args.out)
    payload = torch.load(src, map_location="cpu", weights_only=False)
    state = payload["state_dict"]
    names = {
        "state_w1": "state_enc.0.weight",
        "state_b1": "state_enc.0.bias",
        "state_w2": "state_enc.2.weight",
        "state_b2": "state_enc.2.bias",
        "option_w": "opt_enc.0.weight",
        "option_b": "opt_enc.0.bias",
        "score_w1": "score.0.weight",
        "score_b1": "score.0.bias",
        "score_w2": "score.2.weight",
        "score_b2": "score.2.bias",
    }
    arrays = {out: state[key].detach().cpu().numpy().astype(np.float32) for out, key in names.items()}
    arrays["state_mean"] = payload["state_mean"].detach().cpu().numpy().astype(np.float32)
    arrays["state_std"] = payload["state_std"].detach().cpu().numpy().astype(np.float32)
    arrays["max_options"] = np.asarray([int(payload["max_options"])], dtype=np.int32)
    dst.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(dst, **arrays)
    print(f"exported {src} -> {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
