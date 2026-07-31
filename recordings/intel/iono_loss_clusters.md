# Iono loss clusters — schema v2

Pooled **1660 games**: 852 wins / 808 losses (**51.33%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 338 | 41.83% [38.48, 45.26] | 45 | 5.28% [3.97, 6.99] | +36.55pp |
| `setup_incomplete_active` | 218 | 26.98% [24.03, 30.14] | 29 | 3.40% [2.38, 4.85] | +23.58pp |
| `active_energy_lt2` | 203 | 25.12% [22.26, 28.23] | 14 | 1.64% [0.98, 2.74] | +23.48pp |
| `bench_empty` | 202 | 25.00% [22.14, 28.10] | 8 | 0.94% [0.48, 1.84] | +24.06pp |
| `opponent_prizes_le2` | 705 | 87.25% [84.78, 89.38] | 366 | 42.96% [39.67, 46.31] | +44.29pp |
| `hero_prizes_ge4` | 365 | 45.17% [41.77, 48.62] | 39 | 4.58% [3.37, 6.20] | +40.60pp |
| `prize_deficit_ge2` | 432 | 53.47% [50.02, 56.88] | 9 | 1.06% [0.56, 2.00] | +52.41pp |
| `hand_le2` | 123 | 15.22% [12.91, 17.86] | 88 | 10.33% [8.46, 12.55] | +4.89pp |
| `deck_le5` | 17 | 2.10% [1.32, 3.34] | 63 | 7.39% [5.82, 9.35] | -5.29pp |
| `turn_ge12` | 497 | 61.51% [58.11, 64.80] | 788 | 92.49% [90.52, 94.07] | -30.98pp |
| `iono_threat_active` | 11 | 1.36% [0.76, 2.42] | 4 | 0.47% [0.18, 1.20] | +0.89pp |

## Readout

`fragile_board_any` is the first evidence-backed target: it covers at least 20% of losses and is strongly enriched versus wins. Its three overlapping components are incomplete active evolution, active energy below two, and an empty bench.

This does **not** identify a safe policy change by itself. A follow-up lever must target an earlier preventable decision and still pass pooled A/B gates; the final state can be a consequence rather than the cause of losing.

## Source shards

| file | games | W-L | WR | skipped |
|---|---:|---:|---:|---:|
| `iono_decisions_real_iono_tomato_s0_20260731T002727Z.jsonl` | 60 | 32-28 | 53.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T010147Z.jsonl` | 800 | 416-384 | 52.00% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
