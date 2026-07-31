# Anti-meta autopilot

Updated: `2026-07-31T03:00:11+00:00`
Cycle: `17`

## Ship status

- Decision: `HOLD`
- Reasons: iono 51.5625 < 55.0, crustle_min 83.1625 < 89.0
- Iono: 51.5625
- Crustle min: 83.1625
- Arch: 85.4
- Dual: 93.4375
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T030311Z.json` best_bce=0.6359381675720215 acc=0.6423357129096985
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | False | 53.8 | 85.0 | 85.0 | 86.7 | -3.462 |
| 2 | tomato_fork_floor2 | False | 47.5 | 86.7 | 86.7 | 88.3 | -7.025 |
| 3 | tomato_fork_floor3 | False | 36.2 | 93.3 | 95.0 | 93.3 | -18.438 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 53.8 | None | None | 53.8 |
| tomato | crustle | 0 | None | 85.0 | 86.7 | 85.8 |
| tomato_fork_floor2 | iono | 0 | 47.5 | None | None | 47.5 |
| tomato_fork_floor2 | crustle | 0 | None | 86.7 | 88.3 | 87.5 |
| tomato_fork_floor3 | iono | 0 | 36.2 | None | None | 36.2 |
| tomato_fork_floor3 | crustle | 0 | None | 95.0 | 93.3 | 94.2 |

Autopilot is local-only. It never submits to Kaggle.
