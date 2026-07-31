# Anti-meta autopilot

Updated: `2026-07-31T04:56:22+00:00`
Cycle: `35`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 52.1875 < 55.0, dual 96.875 < baseline 98.2375 (no regression)
- Iono: 52.1875
- Crustle min: 94.475
- Arch: 85.4
- Dual: 96.875
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T050216Z.json` best_bce=0.6311507225036621 acc=0.6479730606079102
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato | True | 57.5 | 93.3 | 100.0 | 93.3 | 3.075 |
| 2 | tomato_fork_floor3 | True | 55.0 | 91.5 | 93.3 | 91.5 | 0.55 |
| 3 | tomato_fork_floor2 | False | 46.2 | 93.3 | 95.0 | 93.3 | -8.338 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 57.5 | None | None | 57.5 |
| tomato | crustle | 0 | None | 100.0 | 93.3 | 96.7 |
| tomato_fork_floor2 | iono | 0 | 46.2 | None | None | 46.2 |
| tomato_fork_floor2 | crustle | 0 | None | 95.0 | 93.3 | 94.2 |
| tomato_fork_floor3 | iono | 0 | 55.0 | None | None | 55.0 |
| tomato_fork_floor3 | crustle | 0 | None | 93.3 | 91.5 | 92.4 |

Autopilot is local-only. It never submits to Kaggle.
