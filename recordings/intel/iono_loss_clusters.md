# Iono loss clusters — schema v2

Pooled **53780 games**: 27414 wins / 26366 losses (**50.97%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 11902 | 45.14% [44.54, 45.74] | 1593 | 5.81% [5.54, 6.09] | +39.33pp |
| `setup_incomplete_active` | 7749 | 29.39% [28.84, 29.94] | 972 | 3.55% [3.33, 3.77] | +25.84pp |
| `active_energy_lt2` | 6865 | 26.04% [25.51, 26.57] | 591 | 2.16% [1.99, 2.33] | +23.88pp |
| `bench_empty` | 7611 | 28.87% [28.32, 29.42] | 366 | 1.34% [1.21, 1.48] | +27.53pp |
| `opponent_prizes_le2` | 22351 | 84.77% [84.33, 85.20] | 11457 | 41.79% [41.21, 42.38] | +42.98pp |
| `hero_prizes_ge4` | 12171 | 46.16% [45.56, 46.76] | 1789 | 6.53% [6.24, 6.82] | +39.64pp |
| `prize_deficit_ge2` | 13673 | 51.86% [51.26, 52.46] | 412 | 1.50% [1.37, 1.65] | +50.36pp |
| `hand_le2` | 4568 | 17.33% [16.87, 17.79] | 2766 | 10.09% [9.74, 10.45] | +7.24pp |
| `deck_le5` | 616 | 2.34% [2.16, 2.53] | 2025 | 7.39% [7.08, 7.70] | -5.05pp |
| `turn_ge12` | 15871 | 60.19% [59.60, 60.78] | 24879 | 90.75% [90.40, 91.09] | -30.56pp |
| `iono_threat_active` | 500 | 1.90% [1.74, 2.07] | 323 | 1.18% [1.06, 1.31] | +0.72pp |

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
| `iono_decisions_real_iono_tomato_s0_20260731T030455Z.jsonl` | 1200 | 602-598 | 50.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T030938Z.jsonl` | 1200 | 588-612 | 49.00% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T031425Z.jsonl` | 1200 | 616-584 | 51.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T031916Z.jsonl` | 1200 | 607-593 | 50.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T032456Z.jsonl` | 1200 | 613-587 | 51.08% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T033113Z.jsonl` | 1200 | 569-631 | 47.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T033648Z_p169188.jsonl` | 1200 | 595-605 | 49.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T034246Z_p167968.jsonl` | 1200 | 638-562 | 53.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T035016Z_p169032.jsonl` | 1200 | 602-598 | 50.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T035722Z_p159428.jsonl` | 1200 | 613-587 | 51.08% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T040440Z_p162944.jsonl` | 1200 | 651-549 | 54.25% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T041159Z_p171420.jsonl` | 1200 | 584-616 | 48.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T041923Z_p169432.jsonl` | 1200 | 642-558 | 53.50% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T042638Z_p172852.jsonl` | 1200 | 617-583 | 51.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T043358Z_p147636.jsonl` | 1200 | 599-601 | 49.92% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T044120Z_p163744.jsonl` | 1200 | 631-569 | 52.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T044852Z_p167164.jsonl` | 1200 | 618-582 | 51.50% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T045624Z_p172636.jsonl` | 1200 | 578-622 | 48.17% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
