# Verification certificate

## Claim

- a(1) = 1.
- a(2) = 8.
- a(3) = 16.
- a(4) = 28.
- a(5) = 40.
- a(6) = 64.
- Delete the false OEIS comment about layer profiles; see the 40-point n = 5 nonuniform witness.
- `witnesses/a399138.txt`: configurations for n = 1..11.
- a(9) >= 116.
- a(10) >= 138.
- a(11) >= 164.

## Evidence

| What | Repository path | Author and date | Coverage | Result | Independence / shared code or data |
|---|---|---|---|---|---|
| Witness check | `check_table.py`, `witnesses/a399138.txt` | Athanor lab, individual author and exact date not stated | n=1..11 coordinates, ranges and triples | All witnesses pass | Uses the supplied producer coordinates; separate checking code, authorship independence unspecified |
| Witness check | `tools/verify_witness_lines.py`, `witnesses/A399138_n5_40_nonuniform_cube.txt` | Athanor lab, individual author and exact date not stated | Nonuniform n=5 witness | 40 distinct points, 9880 triples, no collinear triple | Separate checking code; uses producer witness |
| Report / coverage checks | `logs/no3_3d/proof_n5/`, `logs/no3_3d/proof_n6/`, `tools/check_hier.py`, `tools/audit_coverage_indep.py`, `docs/paper.tex` | Athanor lab, AI assisted; individual authors and exact dates not stated | n=5 and n=6 SAT upper-bound case coverage | Coverage complete in stored status logs; UNSAT truth is not verified by these scripts | Two separately written coverage checkers use the same SAT logs; neither checks UNSAT proofs |

## Replayed for this repository

Executed on 13 Nov 2026 WITA, locally. Commands use the logged working directory; logs contain the full outputs. Wall times include process startup.

- `python3 -B tools/audit_coverage_indep.py 5` — exit 0, 0.034 s; output: stored case coverage complete (this does not prove UNSAT). [`logs/certificate-2026-11-13/coverage-n5.log`](logs/certificate-2026-11-13/coverage-n5.log) (SHA-256 `e8c4449b9ecc039a5a4a2c213c712d36836975e29e55f28111c9a9db3a8f9458`).
- `python3 -B tools/audit_coverage_indep.py 6` — exit 0, 0.034 s; output: stored case coverage complete (this does not prove UNSAT). [`logs/certificate-2026-11-13/coverage-n6.log`](logs/certificate-2026-11-13/coverage-n6.log) (SHA-256 `d7590cc46af33f99a7f3383f9a4d9fe78e1a0b27293e9720c9fa6ea0a31ec8e1`).
- `python3 -B tools/check_hier.py logs/no3_3d/proof_n5 5 2 logs/no3_3d/proof_n5/toplevel_256.txt logs/no3_3d/proof_n5/subcases_560.txt` — exit 0, 0.034 s; output: stored case coverage complete (this does not prove UNSAT). [`logs/certificate-2026-11-13/hier-n5.log`](logs/certificate-2026-11-13/hier-n5.log) (SHA-256 `535cd4b260b867a3b35f2798243a256a6946df4fa27baf7ab1686e002875499f`).
- `python3 -B tools/check_hier.py logs/no3_3d/proof_n6 6 2 logs/no3_3d/proof_n6/toplevel_484.txt logs/no3_3d/proof_n6/subcases_748.txt` — exit 0, 0.038 s; output: stored case coverage complete (this does not prove UNSAT). [`logs/certificate-2026-11-13/hier-n6.log`](logs/certificate-2026-11-13/hier-n6.log) (SHA-256 `3c9e85ba4cd2c4100e8978c5726b3903ae726193a8360f396fb9828295ce5dc1`).
- `python3 -B tools/verify_witness_lines.py 5 witnesses/A399138_n5_40_nonuniform_cube.txt 40` — exit 0, 0.048 s; output: n=5: 40 points, 9880 triples, 0 collinear. [`logs/certificate-2026-11-13/nonuniform.log`](logs/certificate-2026-11-13/nonuniform.log) (SHA-256 `6fd542ae6ccf889c62229f6f80c1e8a8f83675db059d6f5832e15eab81ce9f9d`).
- `python3 -B /tmp/c7-profile.py` — exit 0, 0.036 s; output: axis 0 layers [8, 8, 7, 9, 8]; axis 1 layers [9, 8, 7, 9, 7]; axis 2 layers [8, 8, 8, 8, 8]; from collections import Counter; from pathlib import Path; p=Path("witnesses/A399138_n5_40_nonuniform_cube.txt"); pts=[tuple(map(int,l.split())) for l in p.read_te [`logs/certificate-2026-11-13/profiles.log`](logs/certificate-2026-11-13/profiles.log) (SHA-256 `5495718e9cef7c0be2d20f472bb11787bf030e7df85ace989c7bf13ace2c0a82`).
- `python3 -B check_table.py` — exit 0, 1.647 s; output: n=1..11: all listed point sets pass triple checks (1, 8, 16, 28, 40, 64, 73, 94, 116, 138, 164). [`logs/certificate-2026-11-13/table.log`](logs/certificate-2026-11-13/table.log) (SHA-256 `b3dc4aba97bec16a01b4f14f372225c30c9def24634f5ea36bae0a72c54c2064`).

Full SAT proof regeneration was not replayed: the split-case proof traces were not retained and were reported to occupy tens of gigabytes; the time to regenerate is not established.

## Not covered

Witnesses alone establish lower bounds, not exactness. The n=5 and n=6 upper bounds rest on stored SAT solver reports: DRAT traces for split cases are absent; encoding, symmetry and UNSAT results need independent proof. The full written upper-bound argument for n=3 and n=4 was not independently checked here. The claim about two full outer faces and the restricted optimum 39 were not separately replayed. The Guide check is pending.

## Guide's independent check

pending

## Verdict

partial — The evidence and replay leave the gaps above, and the Guide's independent check is pending.
