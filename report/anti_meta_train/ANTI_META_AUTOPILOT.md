# Anti-meta autopilot

Updated: `2026-07-31T03:24:54+00:00`
Cycle: `22`

## Ship status

- Decision: `HOLD`
- Reasons: iono 54.375 < 55.0, crustle_min 87.0875 < 89.0
- Iono: 54.375
- Crustle min: 87.0875
- Arch: 85.4
- Dual: 94.575
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T032915Z.json` best_bce=0.6324662566184998 acc=0.644964873790741
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor3 | False | 51.2 | 90.0 | 90.0 | 90.0 | -3.288 |
| 2 | tomato | False | 56.2 | 85.0 | 86.4 | 85.0 | -3.438 |
| 3 | tomato_fork_floor2 | False | 48.8 | 83.3 | 88.3 | 83.3 | -5.712 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 56.2 | None | None | 56.2 |
| tomato | crustle | 0 | None | 86.4 | 85.0 | 85.7 |
| tomato_fork_floor2 | iono | 0 | 48.8 | None | None | 48.8 |
| tomato_fork_floor2 | crustle | 0 | None | 88.3 | 83.3 | 85.8 |
| tomato_fork_floor3 | iono | 0 | 51.2 | None | None | 51.2 |
| tomato_fork_floor3 | crustle | 0 | None | 90.0 | 90.0 | 90.0 |

Autopilot is local-only. It never submits to Kaggle.
