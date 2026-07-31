# Anti-meta autopilot

Updated: `2026-07-31T06:25:00+00:00`
Cycle: `46`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 52.1875 < 55.0, dual 96.975 < baseline 98.2375 (no regression)
- Iono: 52.1875
- Crustle min: 94.875
- Arch: 85.4
- Dual: 96.975
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T063142Z.json` best_bce=0.6290071606636047 acc=0.6489793062210083
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor3 | True | 56.2 | 96.7 | 98.3 | 96.7 | 1.762 |
| 2 | tomato_fork_floor2 | False | 42.5 | 96.7 | 100.0 | 96.7 | -12.075 |
| 3 | tomato | False | 37.5 | 91.7 | 91.7 | 98.3 | -17.125 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 37.5 | None | None | 37.5 |
| tomato | crustle | 0 | None | 91.7 | 98.3 | 95.0 |
| tomato_fork_floor2 | iono | 0 | 42.5 | None | None | 42.5 |
| tomato_fork_floor2 | crustle | 0 | None | 100.0 | 96.7 | 98.3 |
| tomato_fork_floor3 | iono | 0 | 56.2 | None | None | 56.2 |
| tomato_fork_floor3 | crustle | 0 | None | 98.3 | 96.7 | 97.5 |

Autopilot is local-only. It never submits to Kaggle.
