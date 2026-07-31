# Anti-meta autopilot

Updated: `2026-07-31T04:26:37+00:00`
Cycle: `31`

## Ship status

- Decision: `HOLD`
- Reasons: iono 47.1875 < 55.0
- Iono: 47.1875
- Crustle min: 94.175
- Arch: 85.4
- Dual: 96.5625
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T043210Z.json` best_bce=0.6318389177322388 acc=0.6462951898574829
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | False | 52.5 | 96.7 | 96.7 | 96.7 | -1.975 |
| 2 | tomato_fork_floor3 | False | 52.5 | 96.7 | 98.3 | 96.7 | -1.975 |
| 3 | tomato_fork_floor2 | False | 48.8 | 93.3 | 98.3 | 93.3 | -5.712 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 52.5 | None | None | 52.5 |
| tomato | crustle | 0 | None | 96.7 | 96.7 | 96.7 |
| tomato_fork_floor2 | iono | 0 | 48.8 | None | None | 48.8 |
| tomato_fork_floor2 | crustle | 0 | None | 98.3 | 93.3 | 95.8 |
| tomato_fork_floor3 | iono | 0 | 52.5 | None | None | 52.5 |
| tomato_fork_floor3 | crustle | 0 | None | 98.3 | 96.7 | 97.5 |

Autopilot is local-only. It never submits to Kaggle.
