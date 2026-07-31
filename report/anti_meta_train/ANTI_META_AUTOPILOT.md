# Anti-meta autopilot

Updated: `2026-07-31T02:28:22+00:00`
Cycle: `10`

## Ship status

- Decision: `HOLD`
- Reasons: iono 52.5 < 55.0, crustle_min 85.725 < 89.0
- Iono: 52.5
- Crustle min: 85.725
- Arch: 85.4
- Dual: 94.2625
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T023103Z.json` best_bce=0.6398026347160339 acc=0.6395618319511414
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor2 | False | 51.2 | 90.0 | 91.5 | 90.0 | -3.288 |
| 2 | tomato | False | 56.2 | 81.7 | 91.7 | 81.7 | -6.738 |
| 3 | tomato_fork_floor3 | False | 47.5 | 88.3 | 95.0 | 88.3 | -7.025 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 56.2 | None | None | 56.2 |
| tomato | crustle | 0 | None | 91.7 | 81.7 | 86.7 |
| tomato_fork_floor2 | iono | 0 | 51.2 | None | None | 51.2 |
| tomato_fork_floor2 | crustle | 0 | None | 91.5 | 90.0 | 90.8 |
| tomato_fork_floor3 | iono | 0 | 47.5 | None | None | 47.5 |
| tomato_fork_floor3 | crustle | 0 | None | 95.0 | 88.3 | 91.7 |

Autopilot is local-only. It never submits to Kaggle.
