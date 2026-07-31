# Iono loss clusters — schema v2

Pooled **58580 games**: 29868 wins / 28712 losses (**50.99%**). Each row compares the last non-setup hero decision in losses against wins.

| cluster | losses | loss share (95% CI) | wins | win share (95% CI) | delta |
|---|---:|---:|---:|---:|---:|
| `fragile_board_any` | 12945 | 45.09% [44.51, 45.66] | 1722 | 5.77% [5.51, 6.04] | +39.32pp |
| `setup_incomplete_active` | 8425 | 29.34% [28.82, 29.87] | 1059 | 3.55% [3.34, 3.76] | +25.80pp |
| `active_energy_lt2` | 7477 | 26.04% [25.54, 26.55] | 634 | 2.12% [1.97, 2.29] | +23.92pp |
| `bench_empty` | 8280 | 28.84% [28.32, 29.36] | 390 | 1.31% [1.18, 1.44] | +27.53pp |
| `opponent_prizes_le2` | 24353 | 84.82% [84.40, 85.23] | 12479 | 41.78% [41.22, 42.34] | +43.04pp |
| `hero_prizes_ge4` | 13233 | 46.09% [45.51, 46.67] | 1958 | 6.56% [6.28, 6.84] | +39.53pp |
| `prize_deficit_ge2` | 14899 | 51.89% [51.31, 52.47] | 446 | 1.49% [1.36, 1.64] | +50.40pp |
| `hand_le2` | 4971 | 17.31% [16.88, 17.76] | 3016 | 10.10% [9.76, 10.44] | +7.22pp |
| `deck_le5` | 668 | 2.33% [2.16, 2.51] | 2232 | 7.47% [7.18, 7.78] | -5.15pp |
| `turn_ge12` | 17295 | 60.24% [59.67, 60.80] | 27096 | 90.72% [90.38, 91.04] | -30.48pp |
| `iono_threat_active` | 542 | 1.89% [1.74, 2.05] | 343 | 1.15% [1.03, 1.28] | +0.74pp |

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
| `iono_decisions_real_iono_tomato_s20_20260731T002801Z.jsonl` | 400 | 185-215 | 46.25% | 0 |
| `iono_decisions_real_iono_tomato_s21_20260731T002801Z.jsonl` | 400 | 219-181 | 54.75% | 0 |
