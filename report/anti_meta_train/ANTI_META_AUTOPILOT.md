# Anti-meta autopilot

Updated: `2026-07-31T03:57:20+00:00`
Cycle: `27`

## Ship status

- Decision: `HOLD`
- Reasons: iono 48.4375 < 55.0
- Iono: 48.4375
- Crustle min: 93.8625
- Arch: 85.4
- Dual: 96.5625
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T040249Z.json` best_bce=0.6328892707824707 acc=0.6455886363983154
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor2 | False | 48.8 | 96.7 | 98.3 | 96.7 | -5.712 |
| 2 | tomato_fork_floor3 | False | 48.8 | 96.7 | 96.7 | 100.0 | -5.712 |
| 3 | tomato | False | 46.2 | 96.7 | 96.7 | 100.0 | -8.338 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 46.2 | None | None | 46.2 |
| tomato | crustle | 0 | None | 96.7 | 100.0 | 98.3 |
| tomato_fork_floor2 | iono | 0 | 48.8 | None | None | 48.8 |
| tomato_fork_floor2 | crustle | 0 | None | 98.3 | 96.7 | 97.5 |
| tomato_fork_floor3 | iono | 0 | 48.8 | None | None | 48.8 |
| tomato_fork_floor3 | crustle | 0 | None | 96.7 | 100.0 | 98.3 |

Autopilot is local-only. It never submits to Kaggle.
