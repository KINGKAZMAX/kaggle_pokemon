# Iono loss clusters — schema v2

Pooled **32180 games**: 16451 wins / 15729 losses (**51.12%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 7113 | 45.22% [44.45, 46.00] | 957 | 5.82% [5.47, 6.19] | +39.40pp |
| `setup_incomplete_active` | 4623 | 29.39% [28.68, 30.11] | 576 | 3.50% [3.23, 3.79] | +25.89pp |
| `active_energy_lt2` | 4118 | 26.18% [25.50, 26.87] | 354 | 2.15% [1.94, 2.39] | +24.03pp |
| `bench_empty` | 4541 | 28.87% [28.17, 29.58] | 219 | 1.33% [1.17, 1.52] | +27.54pp |
| `opponent_prizes_le2` | 13341 | 84.82% [84.25, 85.37] | 6826 | 41.49% [40.74, 42.25] | +43.32pp |
| `hero_prizes_ge4` | 7262 | 46.17% [45.39, 46.95] | 1052 | 6.39% [6.03, 6.78] | +39.77pp |
| `prize_deficit_ge2` | 8146 | 51.79% [51.01, 52.57] | 240 | 1.46% [1.29, 1.65] | +50.33pp |
| `hand_le2` | 2724 | 17.32% [16.73, 17.92] | 1656 | 10.07% [9.62, 10.54] | +7.25pp |
| `deck_le5` | 360 | 2.29% [2.07, 2.53] | 1238 | 7.53% [7.13, 7.94] | -5.24pp |
| `turn_ge12` | 9486 | 60.31% [59.54, 61.07] | 14951 | 90.88% [90.43, 91.31] | -30.57pp |
| `iono_threat_active` | 315 | 2.00% [1.80, 2.23] | 200 | 1.22% [1.06, 1.39] | +0.79pp |

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
| `iono_decisions_real_iono_tomato_s0_20260731T020253Z.jsonl` | 1200 | 621-579 | 51.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T020703Z.jsonl` | 1200 | 607-593 | 50.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T021115Z.jsonl` | 1200 | 606-594 | 50.50% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T021529Z.jsonl` | 1200 | 607-593 | 50.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T021944Z.jsonl` | 1200 | 647-553 | 53.92% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T022403Z.jsonl` | 1200 | 620-580 | 51.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T022824Z.jsonl` | 1200 | 579-621 | 48.25% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T023248Z.jsonl` | 1200 | 614-586 | 51.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T023717Z.jsonl` | 1200 | 605-595 | 50.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T024147Z.jsonl` | 1200 | 587-613 | 48.92% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T024620Z.jsonl` | 1200 | 652-548 | 54.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T025055Z.jsonl` | 1200 | 590-610 | 49.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T025530Z.jsonl` | 1200 | 609-591 | 50.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T030012Z.jsonl` | 1200 | 641-559 | 53.42% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
