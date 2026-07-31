# Iono loss clusters — schema v2

Pooled **6980 games**: 3535 wins / 3445 losses (**50.64%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 1546 | 44.88% [43.22, 46.54] | 214 | 6.05% [5.31, 6.89] | +38.82pp |
| `setup_incomplete_active` | 1033 | 29.99% [28.48, 31.54] | 129 | 3.65% [3.08, 4.32] | +26.34pp |
| `active_energy_lt2` | 915 | 26.56% [25.11, 28.06] | 82 | 2.32% [1.87, 2.87] | +24.24pp |
| `bench_empty` | 973 | 28.24% [26.77, 29.77] | 48 | 1.36% [1.03, 1.80] | +26.89pp |
| `opponent_prizes_le2` | 2954 | 85.75% [84.54, 86.88] | 1471 | 41.61% [40.00, 43.25] | +44.14pp |
| `hero_prizes_ge4` | 1568 | 45.52% [43.86, 47.18] | 211 | 5.97% [5.23, 6.80] | +39.55pp |
| `prize_deficit_ge2` | 1820 | 52.83% [51.16, 54.49] | 53 | 1.50% [1.15, 1.96] | +51.33pp |
| `hand_le2` | 582 | 16.89% [15.68, 18.18] | 340 | 9.62% [8.69, 10.63] | +7.28pp |
| `deck_le5` | 78 | 2.26% [1.82, 2.82] | 268 | 7.58% [6.75, 8.50] | -5.32pp |
| `turn_ge12` | 2108 | 61.19% [59.55, 62.80] | 3231 | 91.40% [90.43, 92.28] | -30.21pp |
| `iono_threat_active` | 56 | 1.63% [1.25, 2.10] | 35 | 0.99% [0.71, 1.37] | +0.64pp |

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
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
