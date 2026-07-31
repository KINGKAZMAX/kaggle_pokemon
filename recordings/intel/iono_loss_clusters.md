# Iono loss clusters — schema v2

Pooled **860 games**: 436 wins / 424 losses (**50.70%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 171 | 40.33% [35.77, 45.07] | 24 | 5.50% [3.73, 8.06] | +34.83pp |
| `setup_incomplete_active` | 114 | 26.89% [22.89, 31.30] | 15 | 3.44% [2.10, 5.60] | +23.45pp |
| `active_energy_lt2` | 101 | 23.82% [20.01, 28.10] | 9 | 2.06% [1.09, 3.88] | +21.76pp |
| `bench_empty` | 107 | 25.24% [21.34, 29.58] | 4 | 0.92% [0.36, 2.33] | +24.32pp |
| `opponent_prizes_le2` | 373 | 87.97% [84.53, 90.73] | 186 | 42.66% [38.10, 47.35] | +45.31pp |
| `hero_prizes_ge4` | 191 | 45.05% [40.38, 49.81] | 28 | 6.42% [4.48, 9.13] | +38.63pp |
| `prize_deficit_ge2` | 233 | 54.95% [50.19, 59.62] | 5 | 1.15% [0.49, 2.66] | +53.81pp |
| `hand_le2` | 57 | 13.44% [10.52, 17.02] | 45 | 10.32% [7.80, 13.53] | +3.12pp |
| `deck_le5` | 7 | 1.65% [0.80, 3.37] | 30 | 6.88% [4.86, 9.65] | -5.23pp |
| `turn_ge12` | 269 | 63.44% [58.76, 67.89] | 402 | 92.20% [89.30, 94.37] | -28.76pp |
| `iono_threat_active` | 8 | 1.89% [0.96, 3.68] | 2 | 0.46% [0.13, 1.66] | +1.43pp |

## Readout

`fragile_board_any` is the first evidence-backed target: it covers at least 20% of losses and is strongly enriched versus wins. Its three overlapping components are incomplete active evolution, active energy below two, and an empty bench.

This does **not** identify a safe policy change by itself. A follow-up lever must target an earlier preventable decision and still pass pooled A/B gates; the final state can be a consequence rather than the cause of losing.

## Source shards

| file | games | W-L | WR | skipped |
|---|---:|---:|---:|---:|
| `iono_decisions_real_iono_tomato_s0_20260731T002727Z.jsonl` | 60 | 32-28 | 53.33% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
