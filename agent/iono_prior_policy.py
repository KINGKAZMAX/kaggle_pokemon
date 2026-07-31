"""Inference-only NumPy policy for the learned Iono decision prior.

The module is fail-closed: unsupported selections or any load/inference error
return the rule agent's legal fallback unchanged.
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np
from cg.api import OptionType


DURALUDON = 169
ARCHALUDON_EX = 190
CINDERACE = 666
RELICANTH = 57
IONO_THREATS = {269, 271}
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
OPTION_TYPE_INDEX = {kind: i for i, kind in enumerate(OPTION_TYPES)}
_MODEL = None
_MODEL_PATH = None
_LOAD_FAILED = False


def _i(value, default=0):
    try:
        return int(value)
    except Exception:
        return default


def _side(obs, mine):
    for attr in (("your", "opponent") if mine else ("opponent", "your")):
        side = getattr(obs, attr, None)
        if side is not None:
            return side
    return None


def _pokemon_features(pokemon):
    if pokemon is None:
        return [0.0, 0.0, 0.0]
    return [
        float(_i(getattr(pokemon, "hp", 0))),
        float(_i(getattr(pokemon, "damage", 0))),
        float(len(getattr(pokemon, "energies", None) or [])),
    ]


def _state_vector(obs):
    me = _side(obs, True)
    opp = _side(obs, False)
    active = getattr(me, "active", None) if me is not None else None
    opp_active = getattr(opp, "active", None) if opp is not None else None
    active_hp, active_damage, active_energy = _pokemon_features(active)
    opp_hp, opp_damage, opp_energy = _pokemon_features(opp_active)
    active_id = _i(getattr(active, "id", 0)) if active is not None else 0
    opp_id = _i(getattr(opp_active, "id", 0)) if opp_active is not None else 0
    context = getattr(getattr(obs, "select", None), "context", None)
    context_name = str(getattr(context, "name", context) or "").upper()
    options = list(getattr(getattr(obs, "select", None), "option", None) or [])
    return [
        float(_i(getattr(getattr(obs, "current", None), "turn", 0))),
        float(len(getattr(me, "prize", None) or [])) if me is not None else 0.0,
        float(len(getattr(opp, "prize", None) or [])) if opp is not None else 0.0,
        float(len(getattr(me, "hand", None) or [])) if me is not None else 0.0,
        float(_i(getattr(me, "deck", 0))) if me is not None else 0.0,
        float(len(getattr(me, "discard", None) or [])) if me is not None else 0.0,
        float(len(getattr(me, "bench", None) or [])) if me is not None else 0.0,
        float(len(getattr(opp, "bench", None) or [])) if opp is not None else 0.0,
        active_hp, active_damage, active_energy,
        float(active_id == DURALUDON),
        float(active_id == ARCHALUDON_EX),
        float(active_id == CINDERACE),
        float(active_id == RELICANTH),
        float(active is None),
        opp_hp, opp_damage, opp_energy,
        float(bool(getattr(opp_active, "ex", False) or getattr(opp_active, "megaEx", False))) if opp_active is not None else 0.0,
        float(opp_id in IONO_THREATS),
        float(context_name == "MAIN"),
        float(context_name.startswith("SETUP")),
        float(context_name in ("SWITCH", "TO_ACTIVE", "TO_BENCH")),
        float(len(options)),
    ]


def _option_vector(option):
    vec = [0.0] * len(OPTION_TYPES)
    idx = OPTION_TYPE_INDEX.get(getattr(option, "type", None))
    if idx is not None:
        vec[idx] = 1.0
    card_id = 0
    is_pokemon = 0.0
    is_energy = 0.0
    try:
        card = getattr(option, "card", None)
        if card is not None:
            card_id = _i(getattr(card, "id", 0))
            # Match the collector's historical feature exactly: this is HP for
            # Pokemon cards (not a boolean) because the checkpoint learned it.
            is_pokemon = float(getattr(card, "hp", 0) or False)
            is_energy = float(bool(getattr(card, "energyType", None)))
    except Exception:
        pass
    targets_opponent = 0.0
    try:
        area = getattr(option, "area", None)
        area_name = str(getattr(area, "name", area) or "").upper()
        targets_opponent = float("OPPONENT" in area_name)
    except Exception:
        pass
    return vec + [float(card_id), is_pokemon, is_energy, targets_opponent]


def _silu(values):
    clipped = np.clip(values, -40.0, 40.0)
    return values / (1.0 + np.exp(-clipped))


def _load_model():
    global _MODEL, _MODEL_PATH, _LOAD_FAILED
    if _LOAD_FAILED:
        return None
    root = Path(__file__).resolve().parents[1]
    path = Path(os.environ.get("ARCH_IONO_PRIOR_PATH", root / "artifacts" / "iono_prior_best.npz"))
    if _MODEL is not None and _MODEL_PATH == path:
        return _MODEL
    try:
        with np.load(path, allow_pickle=False) as data:
            _MODEL = {name: data[name].copy() for name in data.files}
        _MODEL_PATH = path
        return _MODEL
    except Exception:
        _LOAD_FAILED = True
        return None


def choose_with_prior(obs, fallback):
    """Return a legal single option, or the supplied legal fallback."""
    try:
        if not isinstance(fallback, list) or len(fallback) != 1:
            return fallback
        options = list(getattr(getattr(obs, "select", None), "option", None) or [])
        model = _load_model()
        if model is None or not options:
            return fallback
        max_options = int(model["max_options"][0])
        if len(options) > max_options:
            return fallback
        state = np.asarray(_state_vector(obs), dtype=np.float32)
        option = np.asarray([_option_vector(item) for item in options], dtype=np.float32)
        state = (state - model["state_mean"]) / model["state_std"]
        option[:, -4] = np.log1p(option[:, -4]) / 8.0
        state_h = _silu(model["state_w1"] @ state + model["state_b1"])
        state_h = _silu(model["state_w2"] @ state_h + model["state_b2"])
        option_h = _silu(option @ model["option_w"].T + model["option_b"])
        state_rows = np.repeat(state_h[None, :], len(options), axis=0)
        hidden = _silu(np.concatenate((state_rows, option_h), axis=1) @ model["score_w1"].T + model["score_b1"])
        scores = (hidden @ model["score_w2"].T + model["score_b2"]).reshape(-1)
        if not np.isfinite(scores).any():
            return fallback
        return [int(np.nanargmax(scores))]
    except Exception:
        return fallback
