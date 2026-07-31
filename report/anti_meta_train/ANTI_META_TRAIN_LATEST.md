# Anti-meta local training director

Updated: `2026-07-31T01:01:46+00:00`

## Objective

Build an Archaludon anti-meta/router candidate without burning Kaggle CAP. Current binding targets: Iono >=55%, Crustle min >=89%, Arch overall >=83%, dual >=90/baseline.

## Current ship gate

- Decision: `HOLD`
- Reasons: iono 50.3125 < 55.0, crustle_min 86.575 < 89.0
- Arch: 85.4
- Iono: 50.3125
- Crustle min: 86.575
- Dual: 91.5625
- Submits today: 2/5

## Iono failure target

- Dataset games: 1660
- Pooled WR: 51.33%
- Main cluster: fragile_board_any = incomplete evolved active OR active energy <2 OR empty bench.

## Latest training artifact

- Summary: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T010309Z.json`
- Checkpoint: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T010309Z.pt`
- Decisions: 86108
- Best win multi-option top1: 0.5562943816184998
- Fragile decisions: 52258 (loss=27129, win=25129)

## Required KEEP gates before wiring/submission

```powershell
E:\PTCG_AI_Battle_Challenge\fleet\Shard-Gate.ps1 -Role iono -Script scripts\gate_archaludon.py -Games 300 -Extra @('--opponents','real_iono') -Env @{ARCH_IONO_LEVER='tomato_bc'} -Label iono_bc_fragile

E:\PTCG_AI_Battle_Challenge\fleet\Shard-Gate.ps1 -Role crustle -Script scripts\gate_archaludon.py -Games 120 -Extra @('--opponents','meta_crustle_flg','meta_crustle_majkel') -Env @{ARCH_IONO_LEVER='tomato_bc'} -Label guard_crustle_bc

E:\PTCG_AI_Battle_Challenge\fleet\Shard-Gate.ps1 -Role director -Script scripts\gate_archaludon.py -Games 80 -Suite meta_fast -Env @{ARCH_IONO_LEVER='tomato_bc'} -Label guard_meta_fast_bc
```

KEEP only if Iono clears 55% pooled and guard gates do not regress. Otherwise REJECT and keep tomato.
