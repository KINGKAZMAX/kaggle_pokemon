# Iono loss clusters — schema v2

Pooled **71780 games**: 36548 wins / 35232 losses (**50.92%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 15892 | 45.11% [44.59, 45.63] | 2131 | 5.83% [5.60, 6.08] | +39.28pp |
| `setup_incomplete_active` | 10336 | 29.34% [28.86, 29.81] | 1311 | 3.59% [3.40, 3.78] | +25.75pp |
| `active_energy_lt2` | 9204 | 26.12% [25.67, 26.59] | 785 | 2.15% [2.00, 2.30] | +23.98pp |
| `bench_empty` | 10164 | 28.85% [28.38, 29.32] | 482 | 1.32% [1.21, 1.44] | +27.53pp |
| `opponent_prizes_le2` | 29913 | 84.90% [84.53, 85.27] | 15220 | 41.64% [41.14, 42.15] | +43.26pp |
| `hero_prizes_ge4` | 16232 | 46.07% [45.55, 46.59] | 2389 | 6.54% [6.29, 6.79] | +39.54pp |
| `prize_deficit_ge2` | 18272 | 51.86% [51.34, 52.38] | 551 | 1.51% [1.39, 1.64] | +50.35pp |
| `hand_le2` | 6082 | 17.26% [16.87, 17.66] | 3705 | 10.14% [9.83, 10.45] | +7.13pp |
| `deck_le5` | 797 | 2.26% [2.11, 2.42] | 2723 | 7.45% [7.19, 7.72] | -5.19pp |
| `turn_ge12` | 21190 | 60.14% [59.63, 60.65] | 33135 | 90.66% [90.36, 90.96] | -30.52pp |
| `iono_threat_active` | 653 | 1.85% [1.72, 2.00] | 432 | 1.18% [1.08, 1.30] | +0.67pp |

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
| `iono_decisions_real_iono_tomato_s0_20260731T050407Z_p146564.jsonl` | 1200 | 623-577 | 51.92% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T051148Z_p167316.jsonl` | 1200 | 626-574 | 52.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T051940Z_p156216.jsonl` | 1200 | 609-591 | 50.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T052734Z_p164536.jsonl` | 1200 | 596-604 | 49.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T053526Z_p171088.jsonl` | 1200 | 596-604 | 49.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T054327Z_p173560.jsonl` | 1200 | 611-589 | 50.92% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T055131Z_p174168.jsonl` | 1200 | 619-581 | 51.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T055948Z_p132940.jsonl` | 1200 | 620-580 | 51.67% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T060810Z_p176640.jsonl` | 1200 | 638-562 | 53.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T061632Z_p162752.jsonl` | 1200 | 573-627 | 47.75% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T062501Z_p149220.jsonl` | 1200 | 616-584 | 51.33% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T063330Z_p176744.jsonl` | 1200 | 629-571 | 52.42% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T064203Z_p175572.jsonl` | 1200 | 595-605 | 49.58% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T065035Z_p178424.jsonl` | 1200 | 603-597 | 50.25% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T065920Z_p177616.jsonl` | 1200 | 580-620 | 48.33% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
