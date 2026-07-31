# Anti-meta autopilot

Updated: `2026-07-31T05:27:33+00:00`
Cycle: `39`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 50.0 < 55.0, dual 97.7125 < baseline 98.2375 (no regression)
- Iono: 50.0
- Crustle min: 94.0625
- Arch: 85.4
- Dual: 97.7125
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T053338Z.json` best_bce=0.6311680674552917 acc=0.6476848721504211
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | False | 53.8 | 93.3 | 93.3 | 96.7 | -0.662 |
| 2 | tomato_fork_floor2 | False | 48.8 | 93.3 | 93.3 | 96.7 | -5.712 |
| 3 | tomato_fork_floor3 | False | 47.5 | 96.7 | 96.7 | 96.7 | -7.025 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 53.8 | None | None | 53.8 |
| tomato | crustle | 0 | None | 93.3 | 96.7 | 95.0 |
| tomato_fork_floor2 | iono | 0 | 48.8 | None | None | 48.8 |
| tomato_fork_floor2 | crustle | 0 | None | 93.3 | 96.7 | 95.0 |
| tomato_fork_floor3 | iono | 0 | 47.5 | None | None | 47.5 |
| tomato_fork_floor3 | crustle | 0 | None | 96.7 | 96.7 | 96.7 |

Autopilot is local-only. It never submits to Kaggle.
