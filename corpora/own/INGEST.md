# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 212 (the final check needs at least 200)
- Words: 315,871
- Estimated tokens (words times 1.4): 442,219 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `bearing-capacity__p001-004` | 538 | 832 | - | 3 running line(s) removed |
| `bearing-capacity__p005-008` | 1,582 | 2592 | - | 3 running line(s) removed |
| `bearing-capacity__p009-012` | 1,064 | 1628 | - | 3 running line(s) removed |
| `bearing-capacity__p013-016` | 1,139 | 1746 | - | 3 running line(s) removed |
| `bearing-capacity__p017-020` | 1,222 | 1975 | - | 3 running line(s) removed |
| `bearing-capacity__p021-024` | 1,737 | 2782 | - | 3 running line(s) removed |
| `bearing-capacity__p025-028` | 1,341 | 2219 | - | 3 running line(s) removed |
| `bearing-capacity__p029-032` | 1,015 | 1390 | - | 3 running line(s) removed |
| `bearing-capacity__p033-036` | 1,495 | 2273 | - | 3 running line(s) removed |
| `bearing-capacity__p037-040` | 1,015 | 1674 | - | 3 running line(s) removed |
| `bearing-capacity__p041-044` | 896 | 1338 | - | 3 running line(s) removed |
| `bearing-capacity__p045-048` | 609 | 852 | - | 3 running line(s) removed |
| `bearing-capacity__p049-052` | 997 | 1483 | - | 3 running line(s) removed |
| `bearing-capacity__p053-056` | 1,073 | 1627 | - | 3 running line(s) removed |
| `bearing-capacity__p057-060` | 854 | 1258 | - | 3 running line(s) removed |
| `bearing-capacity__p061-064` | 1,202 | 1417 | - | 3 running line(s) removed |
| `bearing-capacity__p065-068` | 1,165 | 1383 | - | 3 running line(s) removed |
| `bearing-capacity__p069-072` | 1,171 | 1866 | - | 3 running line(s) removed |
| `bearing-capacity__p073-076` | 1,046 | 1502 | - | 3 running line(s) removed |
| `bearing-capacity__p077-080` | 804 | 1156 | - | 3 running line(s) removed |
| `bearing-capacity__p081-084` | 1,168 | 1669 | - | 3 running line(s) removed |
| `bearing-capacity__p085-088` | 916 | 1152 | - | 3 running line(s) removed |
| `bearing-capacity__p089-092` | 1,259 | 1828 | - | 3 running line(s) removed |
| `bearing-capacity__p093-096` | 987 | 1419 | - | 3 running line(s) removed |
| `bearing-capacity__p097-100` | 1,378 | 2067 | - | 3 running line(s) removed |
| `bearing-capacity__p101-104` | 931 | 1390 | - | 3 running line(s) removed |
| `bearing-capacity__p105-108` | 1,056 | 1540 | - | 3 running line(s) removed |
| `bearing-capacity__p109-112` | 806 | 1072 | - | 3 running line(s) removed |
| `bearing-capacity__p113-116` | 1,411 | 2118 | - | 3 running line(s) removed |
| `bearing-capacity__p117-120` | 538 | 746 | - | 3 running line(s) removed |
| `bearing-capacity__p121-124` | 583 | 806 | - | 3 running line(s) removed |
| `bearing-capacity__p125-128` | 826 | 1166 | - | 3 running line(s) removed |
| `bearing-capacity__p129-132` | 1,292 | 1722 | - | 3 running line(s) removed |
| `bearing-capacity__p133-136` | 1,178 | 1493 | - | 3 running line(s) removed |
| `bearing-capacity__p137-140` | 1,202 | 1980 | - | 3 running line(s) removed |
| `bearing-capacity__p141-144` | 1,258 | 2123 | - | 3 running line(s) removed |
| `bearing-capacity__p145-148` | 1,649 | 2780 | - | 3 running line(s) removed |
| `bearing-capacity__p149-152` | 1,012 | 1436 | - | 3 running line(s) removed |
| `bearing-capacity__p153-156` | 797 | 1162 | - | 3 running line(s) removed |
| `bearing-capacity__p157-160` | 801 | 1205 | - | 3 running line(s) removed |
| `bearing-capacity__p161-164` | 668 | 1388 | - | 3 running line(s) removed |
| `bearing-capacity__p165-168` | 539 | 881 | - | 3 running line(s) removed |
| `bearing-capacity__p169-172` | 727 | 1864 | - | 3 running line(s) removed |
| `bearing-capacity__p173-176` | 424 | 1166 | - | 3 running line(s) removed |
| `bearing-capacity__p177-180` | 402 | 1182 | - | 3 running line(s) removed |
| `bearing-capacity__p181-184` | 377 | 891 | - | 3 running line(s) removed |
| `bearing-capacity__p185-188` | 793 | 1176 | - | 3 running line(s) removed |
| `bearing-capacity__p189-192` | 805 | 1258 | - | 3 running line(s) removed |
| `bearing-capacity__p193-196` | 657 | 1006 | - | 3 running line(s) removed |
| `geotechnical-investigations__p001-004` | 620 | 965 | - | 3 running line(s) removed |
| `geotechnical-investigations__p005-008` | 1,427 | 1750 | - | 3 running line(s) removed |
| `geotechnical-investigations__p009-012` | 1,468 | 2646 | - | 3 running line(s) removed |
| `geotechnical-investigations__p013-016` | 1,356 | 2234 | - | 3 running line(s) removed |
| `geotechnical-investigations__p017-020` | 1,118 | 1864 | - | 3 running line(s) removed |
| `geotechnical-investigations__p021-024` | 1,564 | 2644 | - | 3 running line(s) removed |
| `geotechnical-investigations__p025-028` | 727 | 1309 | - | 3 running line(s) removed |
| `geotechnical-investigations__p029-032` | 1,646 | 2823 | - | 3 running line(s) removed |
| `geotechnical-investigations__p033-036` | 1,417 | 2558 | - | 3 running line(s) removed |
| `geotechnical-investigations__p037-040` | 1,806 | 3189 | - | 3 running line(s) removed |
| `geotechnical-investigations__p041-044` | 1,547 | 2665 | - | 3 running line(s) removed |
| `geotechnical-investigations__p045-048` | 1,338 | 2181 | - | 3 running line(s) removed |
| `geotechnical-investigations__p049-052` | 1,709 | 3006 | - | 3 running line(s) removed |
| `geotechnical-investigations__p053-056` | 1,464 | 2203 | - | 3 running line(s) removed |
| `geotechnical-investigations__p057-060` | 2,113 | 2772 | - | 3 running line(s) removed |
| `geotechnical-investigations__p061-064` | 2,649 | 3946 | - | 3 running line(s) removed |
| `geotechnical-investigations__p065-068` | 1,995 | 3058 | - | 3 running line(s) removed |
| `geotechnical-investigations__p069-072` | 1,853 | 2790 | - | 3 running line(s) removed |
| `geotechnical-investigations__p073-076` | 1,237 | 1945 | - | 3 running line(s) removed |
| `geotechnical-investigations__p077-080` | 2,012 | 3176 | - | 3 running line(s) removed |
| `geotechnical-investigations__p081-084` | 2,611 | 3961 | - | 3 running line(s) removed |
| `geotechnical-investigations__p085-088` | 2,158 | 3428 | - | 3 running line(s) removed |
| `geotechnical-investigations__p089-092` | 2,346 | 3728 | - | 3 running line(s) removed |
| `geotechnical-investigations__p093-096` | 1,270 | 2088 | - | 3 running line(s) removed |
| `geotechnical-investigations__p097-100` | 1,897 | 3162 | - | 3 running line(s) removed |
| `geotechnical-investigations__p101-103` | 1,503 | 3255 | - | 3 running line(s) removed |
| `rock-foundations__p001-004` | 568 | 907 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p005-008` | 1,181 | 2076 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p009-012` | 2,449 | 4211 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p013-016` | 2,559 | 4284 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p017-020` | 1,666 | 2761 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p021-024` | 2,308 | 3712 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p025-028` | 1,767 | 3025 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p029-032` | 2,186 | 3603 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p033-036` | 2,667 | 4325 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p037-040` | 1,499 | 2529 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p041-044` | 1,614 | 2704 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p045-048` | 1,835 | 2949 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p049-052` | 1,463 | 2370 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p053-056` | 1,689 | 2806 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p057-060` | 2,179 | 3232 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p061-064` | 1,851 | 2913 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p065-068` | 3,035 | 4987 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p069-072` | 2,064 | 3327 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p073-076` | 1,964 | 3076 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p077-080` | 2,910 | 4864 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p081-084` | 2,401 | 4059 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p085-088` | 2,810 | 4441 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p089-092` | 3,279 | 5210 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p093-096` | 2,602 | 4126 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p097-100` | 1,624 | 2799 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p101-104` | 2,090 | 3474 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p105-108` | 2,185 | 3581 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `rock-foundations__p109-112` | 653 | 1098 | - | 3 running line(s) removed; reference list dropped, 12,510 characters (heading) |
| `settlement-analysis__p001-004` | 674 | 1047 | - | 3 running line(s) removed |
| `settlement-analysis__p005-008` | 1,496 | 2468 | - | 3 running line(s) removed |
| `settlement-analysis__p009-012` | 1,485 | 2378 | - | 3 running line(s) removed |
| `settlement-analysis__p013-016` | 984 | 1627 | - | 3 running line(s) removed |
| `settlement-analysis__p017-020` | 1,219 | 1968 | - | 3 running line(s) removed |
| `settlement-analysis__p021-024` | 1,026 | 1623 | - | 3 running line(s) removed |
| `settlement-analysis__p025-028` | 1,294 | 2027 | - | 3 running line(s) removed |
| `settlement-analysis__p029-032` | 519 | 743 | - | 3 running line(s) removed |
| `settlement-analysis__p033-036` | 805 | 1140 | - | 3 running line(s) removed |
| `settlement-analysis__p037-040` | 1,038 | 1589 | - | 3 running line(s) removed |
| `settlement-analysis__p041-044` | 553 | 855 | - | 3 running line(s) removed |
| `settlement-analysis__p045-048` | 732 | 1088 | - | 3 running line(s) removed |
| `settlement-analysis__p049-052` | 757 | 1098 | - | 3 running line(s) removed |
| `settlement-analysis__p053-056` | 1,200 | 1861 | - | 3 running line(s) removed |
| `settlement-analysis__p057-060` | 1,101 | 1659 | - | 3 running line(s) removed |
| `settlement-analysis__p061-064` | 1,178 | 1808 | - | 3 running line(s) removed |
| `settlement-analysis__p065-068` | 346 | 522 | - | 3 running line(s) removed |
| `settlement-analysis__p069-072` | 781 | 1212 | - | 3 running line(s) removed |
| `settlement-analysis__p073-076` | 1,019 | 1570 | - | 3 running line(s) removed |
| `settlement-analysis__p077-080` | 1,634 | 2666 | - | 3 running line(s) removed |
| `settlement-analysis__p081-084` | 1,070 | 1664 | - | 3 running line(s) removed |
| `settlement-analysis__p085-088` | 573 | 786 | - | 3 running line(s) removed |
| `settlement-analysis__p089-092` | 540 | 806 | - | 3 running line(s) removed |
| `settlement-analysis__p093-096` | 487 | 713 | - | 3 running line(s) removed |
| `settlement-analysis__p097-100` | 1,018 | 1629 | - | 3 running line(s) removed |
| `settlement-analysis__p101-104` | 1,429 | 2167 | - | 3 running line(s) removed |
| `settlement-analysis__p105-108` | 957 | 1353 | - | 3 running line(s) removed |
| `settlement-analysis__p109-112` | 1,309 | 1997 | - | 3 running line(s) removed |
| `settlement-analysis__p113-116` | 1,236 | 1876 | - | 3 running line(s) removed |
| `settlement-analysis__p117-120` | 867 | 1454 | - | 3 running line(s) removed |
| `settlement-analysis__p121-124` | 1,409 | 2246 | - | 3 running line(s) removed |
| `settlement-analysis__p125-128` | 1,466 | 2417 | - | 3 running line(s) removed |
| `settlement-analysis__p129-132` | 1,216 | 2104 | - | 3 running line(s) removed |
| `settlement-analysis__p133-136` | 1,682 | 2834 | - | 3 running line(s) removed |
| `settlement-analysis__p137-140` | 758 | 1151 | - | 3 running line(s) removed |
| `settlement-analysis__p141-144` | 402 | 652 | - | 3 running line(s) removed |
| `settlement-analysis__p145-148` | 444 | 705 | - | 3 running line(s) removed |
| `settlement-analysis__p149-152` | 599 | 899 | - | 3 running line(s) removed |
| `settlement-analysis__p153-156` | 946 | 1334 | - | 3 running line(s) removed |
| `settlement-analysis__p157-160` | 1,125 | 1702 | - | 3 running line(s) removed |
| `settlement-analysis__p161-164` | 1,238 | 1892 | - | 3 running line(s) removed |
| `settlement-analysis__p165-168` | 614 | 966 | - | 3 running line(s) removed |
| `settlement-analysis__p169-172` | 1,209 | 1713 | - | 3 running line(s) removed |
| `settlement-analysis__p173-176` | 671 | 962 | - | 3 running line(s) removed |
| `settlement-analysis__p177-180` | 763 | 1084 | - | 3 running line(s) removed |
| `settlement-analysis__p181-184` | 791 | 1629 | - | 3 running line(s) removed |
| `settlement-analysis__p185-188` | 378 | 1135 | - | 3 running line(s) removed |
| `settlement-analysis__p189-192` | 305 | 1200 | - | 3 running line(s) removed |
| `settlement-analysis__p193-196` | 359 | 1173 | - | 3 running line(s) removed |
| `settlement-analysis__p197-200` | 674 | 1024 | - | 3 running line(s) removed |
| `settlement-analysis__p201-205` | 820 | 1033 | - | 3 running line(s) removed |
| `tunnels-shafts-rock__p001-004` | 826 | 1616 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p005-008` | 2,433 | 3822 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p009-012` | 2,410 | 3690 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p013-016` | 1,014 | 1712 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p017-020` | 3,098 | 4649 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p021-024` | 3,522 | 5130 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p025-028` | 2,648 | 3818 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p029-032` | 2,200 | 3398 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p033-036` | 2,368 | 3580 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p037-040` | 2,528 | 3668 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p041-044` | 2,173 | 3069 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p045-048` | 1,911 | 2684 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p049-052` | 2,896 | 4091 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p053-056` | 1,813 | 2614 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p057-060` | 1,248 | 1851 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p061-064` | 1,297 | 1812 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p065-068` | 1,263 | 1930 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p069-072` | 1,679 | 2407 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p073-076` | 1,328 | 1906 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p077-080` | 3,528 | 5074 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p081-084` | 3,384 | 4950 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p085-088` | 3,221 | 4722 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p089-092` | 2,660 | 4092 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p093-096` | 3,343 | 5029 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p097-100` | 2,534 | 3705 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p101-104` | 2,424 | 3454 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p105-108` | 2,257 | 3124 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p109-112` | 1,962 | 2772 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p113-116` | 2,892 | 4207 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p117-120` | 2,695 | 3961 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p121-124` | 2,967 | 4342 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p125-128` | 1,421 | 2072 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p129-132` | 1,644 | 2294 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p133-136` | 2,311 | 2856 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p137-140` | 2,192 | 2499 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p141-144` | 1,782 | 2435 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p145-148` | 1,133 | 1692 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p149-152` | 1,837 | 2885 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p153-156` | 1,634 | 2544 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p157-160` | 1,429 | 2283 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p161-164` | 1,880 | 2927 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p165-168` | 2,037 | 3306 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p169-172` | 2,144 | 3435 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p173-176` | 2,603 | 4124 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p177-180` | 1,766 | 2730 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p181-184` | 1,811 | 2738 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p185-188` | 905 | 1290 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p189-192` | 1,166 | 1565 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p193-196` | 1,258 | 1824 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p197-200` | 588 | 797 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p201-204` | 1,890 | 3199 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p205-208` | 2,026 | 3353 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p213-216` | 605 | 905 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p217-220` | 2,560 | 3826 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p221-224` | 1,949 | 3041 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p225-228` | 2,552 | 4046 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p229-232` | 2,213 | 3557 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |
| `tunnels-shafts-rock__p233-236` | 1,589 | 2226 | - | 3 running line(s) removed; reference list dropped, 25,210 characters (heading) |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
