# Iono loss clusters — schema v2

Pooled **75380 games**: 38414 wins / 36966 losses (**50.96%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 16706 | 45.19% [44.69, 45.70] | 2244 | 5.84% [5.61, 6.08] | +39.35pp |
| `setup_incomplete_active` | 10849 | 29.35% [28.89, 29.81] | 1381 | 3.60% [3.41, 3.79] | +25.75pp |
| `active_energy_lt2` | 9659 | 26.13% [25.68, 26.58] | 829 | 2.16% [2.02, 2.31] | +23.97pp |
| `bench_empty` | 10689 | 28.92% [28.46, 29.38] | 511 | 1.33% [1.22, 1.45] | +27.59pp |
| `opponent_prizes_le2` | 31373 | 84.87% [84.50, 85.23] | 15973 | 41.58% [41.09, 42.07] | +43.29pp |
| `hero_prizes_ge4` | 17058 | 46.15% [45.64, 46.65] | 2522 | 6.57% [6.32, 6.82] | +39.58pp |
| `prize_deficit_ge2` | 19181 | 51.89% [51.38, 52.40] | 581 | 1.51% [1.40, 1.64] | +50.38pp |
| `hand_le2` | 6403 | 17.32% [16.94, 17.71] | 3911 | 10.18% [9.88, 10.49] | +7.14pp |
| `deck_le5` | 841 | 2.28% [2.13, 2.43] | 2838 | 7.39% [7.13, 7.65] | -5.11pp |
| `turn_ge12` | 22243 | 60.17% [59.67, 60.67] | 34806 | 90.61% [90.31, 90.90] | -30.44pp |
| `iono_threat_active` | 686 | 1.86% [1.72, 2.00] | 458 | 1.19% [1.09, 1.31] | +0.66pp |

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
| `iono_decisions_real_iono_tomato_s0_20260731T070805Z_p177872.jsonl` | 1200 | 622-578 | 51.83% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T071651Z_p180908.jsonl` | 1200 | 614-586 | 51.17% | 0 |
| `iono_decisions_real_iono_tomato_s0_20260731T072544Z_p177200.jsonl` | 1200 | 630-570 | 52.50% | 0 |
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
