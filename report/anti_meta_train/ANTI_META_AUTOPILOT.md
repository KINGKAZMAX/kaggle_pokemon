# Anti-meta autopilot

Updated: `2026-07-31T07:25:43+00:00`
Cycle: `53`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 53.125 < 55.0, dual 96.45 < baseline 98.2375 (no regression)
- Iono: 53.125
- Crustle min: 94.7
- Arch: 85.4
- Dual: 96.45
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T073256Z.json` best_bce=0.6296519637107849 acc=0.6481937766075134
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | True | 62.5 | 93.3 | 93.3 | 95.0 | 4.925 |
| 2 | tomato_fork_floor3 | False | 52.5 | 95.0 | 96.7 | 95.0 | -1.975 |
| 3 | tomato_fork_floor2 | False | 47.5 | 93.3 | 93.3 | 98.3 | -7.025 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 62.5 | None | None | 62.5 |
| tomato | crustle | 0 | None | 93.3 | 95.0 | 94.2 |
| tomato_fork_floor2 | iono | 0 | 47.5 | None | None | 47.5 |
| tomato_fork_floor2 | crustle | 0 | None | 93.3 | 98.3 | 95.8 |
| tomato_fork_floor3 | iono | 0 | 52.5 | None | None | 52.5 |
| tomato_fork_floor3 | crustle | 0 | None | 96.7 | 95.0 | 95.8 |

Autopilot is local-only. It never submits to Kaggle.
