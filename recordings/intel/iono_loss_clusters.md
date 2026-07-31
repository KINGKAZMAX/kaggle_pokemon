# Iono loss clusters — schema v2

Pooled **15380 games**: 7866 wins / 7514 losses (**51.14%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 3359 | 44.70% [43.58, 45.83] | 452 | 5.75% [5.25, 6.28] | +38.96pp |
| `setup_incomplete_active` | 2204 | 29.33% [28.31, 30.37] | 269 | 3.42% [3.04, 3.84] | +25.91pp |
| `active_energy_lt2` | 1976 | 26.30% [25.31, 27.30] | 170 | 2.16% [1.86, 2.51] | +24.14pp |
| `bench_empty` | 2152 | 28.64% [27.63, 29.67] | 101 | 1.28% [1.06, 1.56] | +27.36pp |
| `opponent_prizes_le2` | 6394 | 85.09% [84.27, 85.88] | 3243 | 41.23% [40.14, 42.32] | +43.87pp |
| `hero_prizes_ge4` | 3455 | 45.98% [44.86, 47.11] | 494 | 6.28% [5.77, 6.84] | +39.70pp |
| `prize_deficit_ge2` | 3897 | 51.86% [50.73, 52.99] | 115 | 1.46% [1.22, 1.75] | +50.40pp |
| `hand_le2` | 1291 | 17.18% [16.35, 18.05] | 788 | 10.02% [9.37, 10.70] | +7.16pp |
| `deck_le5` | 171 | 2.28% [1.96, 2.64] | 625 | 7.95% [7.37, 8.56] | -5.67pp |
| `turn_ge12` | 4560 | 60.69% [59.58, 61.79] | 7154 | 90.95% [90.29, 91.56] | -30.26pp |
| `iono_threat_active` | 136 | 1.81% [1.53, 2.14] | 101 | 1.28% [1.06, 1.56] | +0.53pp |

## Readout

`fragile_board_any` is the first evidence-backed target: it covers at least 20% of losses and is strongly enriched versus wins. Its three overlapping components are incomplete active evolution, active energy below two, and an empty bench.

This does **not** identify a safe policy change by itself. A follow-up lever must target an earlier preventable decision and still pass pooled A/B gates; the final state can be a consequence rather than the cause of losing.

## Source shards

| file | games | W-L | WR | skipped |
|---|---:|---:|---:|---:|
| `iono_decisions_real_iono_tomato_s0_20260731T002727Z.jsonl` | 60 | 32-28 | 53.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T010147Z.jsonl` | 800 | 416-384 | 52.00% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T011237Z.jsonl` | 800 | 387-413 | 48.38% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T011303Z.jsonl` | 800 | 403-397 | 50.38% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T012429Z.jsonl` | 120 | 67-53 | 55.83% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T012505Z.jsonl` | 1200 | 619-581 | 51.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T012835Z.jsonl` | 1200 | 602-598 | 50.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T013202Z.jsonl` | 1200 | 605-595 | 50.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T013532Z.jsonl` | 1200 | 616-584 | 51.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T013904Z.jsonl` | 1200 | 609-591 | 50.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T014240Z.jsonl` | 1200 | 634-566 | 52.83% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T014620Z.jsonl` | 1200 | 632-568 | 52.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T015008Z.jsonl` | 1200 | 621-579 | 51.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T015426Z.jsonl` | 1200 | 605-595 | 50.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T015837Z.jsonl` | 1200 | 614-586 | 51.17% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
