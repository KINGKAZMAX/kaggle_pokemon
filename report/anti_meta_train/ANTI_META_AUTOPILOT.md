# Anti-meta autopilot

Updated: `2026-07-31T01:58:35+00:00`
Cycle: `3`

## Ship status

- Decision: `HOLD`
- Reasons: iono 52.5 < 55.0, crustle_min 87.7125 < 89.0
- Iono: 52.5
- Crustle min: 87.7125
- Arch: 85.4
- Dual: 93.85
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T020105Z.json` best_bce=0.6455451250076294 acc=0.6385945677757263
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | False | 46.2 | 85.0 | 85.0 | 91.7 | -8.338 |
| 2 | tomato_fork_floor3 | False | 43.8 | 91.7 | 95.0 | 91.7 | -10.762 |
| 3 | tomato_fork_floor2 | False | 41.2 | 85.0 | 86.7 | 85.0 | -13.388 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 46.2 | None | None | 46.2 |
| tomato | crustle | 0 | None | 85.0 | 91.7 | 88.3 |
| tomato_fork_floor2 | iono | 0 | 41.2 | None | None | 41.2 |
| tomato_fork_floor2 | crustle | 0 | None | 86.7 | 85.0 | 85.8 |
| tomato_fork_floor3 | iono | 0 | 43.8 | None | None | 43.8 |
| tomato_fork_floor3 | crustle | 0 | None | 95.0 | 91.7 | 93.3 |

Autopilot is local-only. It never submits to Kaggle.
