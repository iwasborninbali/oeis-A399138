# OEIS A399138: no three collinear points in a cube

<!-- oeis-status:begin -->
**OEIS status** (lab registry, 13 Nov 2026):

- [A399138](https://oeis.org/A399138), no three collinear in the n X n X n grid: a(1..6): **approved** (2026-08-19: sequence created). Certificate: complete.
- [A399138](https://oeis.org/A399138), delete our false comment on layer profiles; witness file n = 1..11 (a(9) >= 116, a(10) >= 138, a(11) >= 164): **queued** (2026-11-13: prepared and queued). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

[A399138](https://oeis.org/A399138): a(n) is the greatest number of points in an n × n × n grid with no three collinear in Euclidean space. Aleksei Kudriashov introduced the sequence in August 2026.

| n | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| a(n) | 1 | 8 | 16 | 28 | 40 | 64 |

The witnesses also give a(7) ≥ 73, a(8) ≥ 94, a(9) ≥ 116, a(10) ≥ 138 and a(11) ≥ 164. These are lower bounds, not exact values. Eric W. Weisstein updated the OEIS bounds for 7 and 8; Pontus von Brömssen contributed the entry's connected-set observation. The asymptotic lower bound is due to A. Por and D. R. Wood.

## Correction to a comment in the entry

The entry's comment "Every optimum found has the same layer profile along all three axes ... at n = 5 this profile is
infeasible (two outer layers cannot both carry 2n points at any total)" is wrong on both counts:
`witnesses/A399138_n5_40_nonuniform_cube.txt` is a 40-point optimum for n = 5 with layer profiles (8,8,7,9,8), (9,8,7,9,7)
and (8,8,8,8,8) along the three axes, and two parallel outer layers can trivially both carry 10 points (two planar
10-point configurations in opposite faces have no three collinear points). The research note's best total with both outer
layers full at n = 5 is 39 (a restricted computational optimum).

## Method and checks

`witnesses/a399138.txt` contains coordinates for n = 1…11; `witnesses/A399138_n5_40_nonuniform_cube.txt` is the nonuniform n = 5 optimum. The SAT upper-bound computation for n = 5 and 6 splits the infeasibility questions for 41 and 65 points into cases, using symmetry reduction. The recorded status logs and manifests are in `logs/`; `tools/check_hier.py` and the independently written `tools/audit_coverage_indep.py` check the recorded coverage. **They do not independently establish the truth of the UNSAT lines.** The paper states that DRAT certificates for the cases that were split were not stored because they ran to tens of gigabytes. Thus a full independent proof replay requires regenerating those proofs; the present repository does not contain all exact-value proof certificates. The symmetry and encoding require separate checks. See [verification protocol](docs/VERIFICATION.md) and [paper](docs/paper.tex).

```sh
python3 -B check_table.py
python3 -B tools/verify_witness_lines.py 6 witnesses/sat_witness_n6_64.txt 64
python3 -B tools/check_hier.py logs/no3_3d/proof_n5 5 2 logs/no3_3d/proof_n5/toplevel_256.txt logs/no3_3d/proof_n5/subcases_560.txt
python3 -B tools/check_hier.py logs/no3_3d/proof_n6 6 2 logs/no3_3d/proof_n6/toplevel_484.txt logs/no3_3d/proof_n6/subcases_748.txt
python3 -B tools/audit_coverage_indep.py 5
python3 -B tools/audit_coverage_indep.py 6
```

## Archive and licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance. The paper is archived at [Zenodo 10.5281/zenodo.22019279](https://doi.org/10.5281/zenodo.22019279); the original working material is in [saturation](https://github.com/iwasborninbali/saturation). Code: MIT; data and text: CC BY 4.0; see [LICENSE.md](LICENSE.md).
