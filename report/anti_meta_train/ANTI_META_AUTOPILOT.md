# Anti-meta autopilot

Updated: `2026-07-31T06:50:33+00:00`
Cycle: `49`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 51.5625 < 55.0, dual 97.3 < baseline 98.2375 (no regression)
- Iono: 51.5625
- Crustle min: 92.9125
- Arch: 85.4
- Dual: 97.3
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T065733Z.json` best_bce=0.6278353929519653 acc=0.649113118648529
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor3 | False | 53.8 | 98.3 | 98.3 | 98.3 | -0.662 |
| 2 | tomato | False | 52.5 | 91.7 | 94.9 | 91.7 | -1.975 |
| 3 | tomato_fork_floor2 | False | 47.5 | 95.0 | 95.0 | 95.0 | -7.025 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 52.5 | None | None | 52.5 |
| tomato | crustle | 0 | None | 94.9 | 91.7 | 93.3 |
| tomato_fork_floor2 | iono | 0 | 47.5 | None | None | 47.5 |
| tomato_fork_floor2 | crustle | 0 | None | 95.0 | 95.0 | 95.0 |
| tomato_fork_floor3 | iono | 0 | 53.8 | None | None | 53.8 |
| tomato_fork_floor3 | crustle | 0 | None | 98.3 | 98.3 | 98.3 |

Autopilot is local-only. It never submits to Kaggle.
