# Anti-meta autopilot

Updated: `2026-07-31T05:51:30+00:00`
Cycle: `42`

## Ship status

- Decision: `REGRESS`
- Reasons: iono 52.8125 < 55.0, dual 96.5875 < baseline 98.2375 (no regression)
- Iono: 52.8125
- Crustle min: 93.7375
- Arch: 85.4
- Dual: 96.5875
- Submits today: 2/5

## Latest learned artifacts

- Option-Q: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_q_v2\iono_option_q_20260731T055759Z.json` best_bce=0.6332278251647949 acc=0.6464082598686218
- Prior/BC: `E:\PTCG_AI_Battle_Challenge\kaggle_pokemon\artifacts\iono_prior_v2\iono_prior_20260731T011433Z.json` win_multi_top1=0.5837962031364441

## Candidate ranking

| rank | candidate | smoke green | iono | crustle min | flg | majkel | score |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | tomato_fork_floor2 | True | 55.0 | 95.0 | 100.0 | 95.0 | 0.55 |
| 2 | tomato_fork_floor3 | False | 51.2 | 93.2 | 93.2 | 98.3 | -3.288 |
| 3 | tomato | False | 41.2 | 95.0 | 98.3 | 95.0 | -13.388 |

## Raw smoke gates

| candidate | kind | rc | real_iono | flg | majkel | overall |
|---|---|---:|---:|---:|---:|---:|
| tomato | iono | 0 | 41.2 | None | None | 41.2 |
| tomato | crustle | 0 | None | 98.3 | 95.0 | 96.7 |
| tomato_fork_floor2 | iono | 0 | 55.0 | None | None | 55.0 |
| tomato_fork_floor2 | crustle | 0 | None | 100.0 | 95.0 | 97.5 |
| tomato_fork_floor3 | iono | 0 | 51.2 | None | None | 51.2 |
| tomato_fork_floor3 | crustle | 0 | None | 93.2 | 98.3 | 95.8 |

Autopilot is local-only. It never submits to Kaggle.
