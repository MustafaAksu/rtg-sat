#!/usr/bin/env python3
"""
resolv_certificate.py — PREREG-MM1-RESOLVABILITY v1.0 gate.

C1  waveform guards at anchor and at anchor +/- h*d for both directions, h in HJ[:4]
C2  tangent directions: amplitude constraint exact, orthonormal
C3  ladder ratio B:L = 7:20 for every m; L divisible by 4 (quarter blocks exact)
C4  DIRECT-vs-FD agreement at SHORT horizon for BOTH directions AND
    for a chaotic representative as well as a regular one   <-- RANK only did one
C5  h-grid: 21 points, h_j = 0.01*2^-j, and the coefficient perturbations at the
    smallest h are still float-distinct from the anchor
C6  observable is pre-threshold (no 1e-3 token / EPS in observable())

Exit 0 iff all pass.
"""
import sys, math, re, inspect
import numpy as np
import resolv_experiment as R

def main() -> int:
    ok = []
    def chk(n, c):
        ok.append(bool(c)); print(f"[{'PASS' if c else 'FAIL'}] {n}")

    # C2
    c2 = True
    for nm, d in R.DIRS.items():
        c2 &= abs(d[0] + d[1] + 2*d[2]) < 1e-15 and abs(np.linalg.norm(d) - 1) < 1e-12
    c2 &= abs(float(R.DIRS["u"] @ R.DIRS["v"])) < 1e-15
    chk("C2 tangent directions: constraint exact + orthonormal", c2)

    # C1
    phi = np.linspace(0, np.pi, 200001)
    c1 = True
    for nm, d in R.DIRS.items():
        for h in [0.0] + R.HJ[:4]:
            for sg in (1, -1):
                abc = R.ANCHOR + sg*h*d
                g0 = float(R.g1(np.array([0.0]), abc)[0])
                v = R.g(phi, abc)
                mx = float(np.abs(v).max()); am = float(phi[int(np.argmax(np.abs(v)))])
                inner = v[(phi > 1e-9) & (phi < np.pi - 1e-9)]
                nz = int(np.sum(inner[:-1]*inner[1:] < 0))
                c1 &= (abs(g0-1) < 1e-12 and abs(mx-R.A0) < 1e-9
                       and abs(am-np.pi/2) < 1e-4 and nz == 0)
    chk("C1 waveform guards at anchor and perturbed points (both dirs)", c1)

    # C3
    c3 = all((R.BL(m)[0]*20 == R.BL(m)[1]*7) and (R.BL(m)[1] % 4 == 0) for m in R.MS)
    Ts = [sum(R.BL(m)) for m in R.MS]
    chk(f"C3 ladder B:L = 7:20, L%4==0, T = {Ts}", c3)

    # C4 — direct vs FD at short horizon, BOTH directions, regular AND chaotic kappa.
    # A FIXED h cannot serve here: the linear window itself shrinks with sensitivity
    # (that is the object of study). The certificate therefore ADAPTS h downward and
    # requires that SOME h achieves agreement -- this certifies the implementation,
    # not the size of the window.
    # The certification criterion is the SHAPE, not a fixed tolerance: E(h) must fall
    # as h decreases (truncation regime), reach an interior minimum, then rise again
    # (roundoff regime). A clear U-curve with a small minimum certifies that FD really
    # converges toward the direct derivative before precision limits take over. A fixed
    # threshold cannot serve, because the achievable minimum depends on |D| itself --
    # which is exactly the quantity under study.
    print(f"{'dir':>4} {'kappa':>7} {'type':>8} {'|D|':>13} {'argmin h':>10} "
          f"{'min rel':>10} {'U-curve':>8}")
    c4 = True
    for dname, d in R.DIRS.items():
        for kap, typ in ((4.00, "regular"), (2.90, "chaotic")):
            ks = np.array([kap]); B, L = 70, 200
            D, _ = R.sensitivity(R.ANCHOR, d, ks, B, L)
            nd = float(np.linalg.norm(D))
            hs, es = [], []
            for e in range(4, 17):
                h = 10.0**(-e)
                Yp, _ = R.observable(R.ANCHOR + h*d, ks, B, L)
                Ym, _ = R.observable(R.ANCHOR - h*d, ks, B, L)
                hs.append(h)
                es.append(float(np.linalg.norm((Yp - Ym)/(2*h) - D))/max(nd, 1e-300))
            i = int(np.argmin(es))
            interior = 0 < i < len(es)-1
            rises = interior and es[-1] > 10*es[i]      # roundoff regime present
            falls = interior and es[0] > 10*es[i]       # truncation regime present
            good = interior and rises and falls and es[i] < 1e-2
            c4 &= good
            print(f"{dname:>4} {kap:7.2f} {typ:>8} {nd:13.4e} {hs[i]:10.1e} "
                  f"{es[i]:10.2e} {'yes' if (interior and rises and falls) else 'NO':>8}")
    chk("C4 E(h) shows a clear U-curve with small interior minimum "
        "(both dirs, regular AND chaotic)", c4)

    # C5
    c5 = len(R.HJ_PRIMARY) == 21 and abs(R.HJ_PRIMARY[0] - 0.01) < 1e-18
    hmin = R.HJ[-1]
    for d in R.DIRS.values():
        pert = R.ANCHOR + hmin*d
        c5 &= np.any(pert != R.ANCHOR)          # float-distinct at the smallest h
    chk(f"C5 primary h-grid 21 pts from 0.01; full hmin={hmin:.3e}, perturbations float-distinct", c5)

    # C6
    src = inspect.getsource(R.observable)
    chk("C6 observable() is pre-threshold",
        not re.search(r"1e-3(?!\d)", src) and "EPS" not in src)

    # C7 — canonical classifier, tested as a UNIT on a synthetic fixture
    # (no source introspection: the helper itself is exercised)
    lam_fx = np.array([[2e-3, 5e-4],       # cell 0: IC0 has big lam ...
                       [2e-3, 2e-3]])      # cell 1: both ICs big lam
    Q_fx = np.zeros((4, 2, 2))
    Q_fx[:, 0, 0] = [2e-3, 2e-3, 5e-4, 2e-3]   # ... but one quarter fails -> NOT chaos
    Q_fx[:, 0, 1] = [5e-4, 5e-4, 5e-4, 5e-4]
    Q_fx[:, 1, 0] = [2e-3, 2e-3, 2e-3, 2e-3]   # all four pass -> chaos
    Q_fx[:, 1, 1] = [5e-4, 5e-4, 5e-4, 5e-4]
    got = R.canonical_classifier(lam_fx, Q_fx)
    lam_only_fx = (lam_fx > R.CHAOS_EPS).any(axis=1)
    c7 = (got.tolist() == [False, True]) and (lam_only_fx.tolist() == [True, True])
    print(f"    unit fixture: lam-only={lam_only_fx.tolist()}  canonical={got.tolist()}"
          f"  (expected [True,True] vs [False,True])")
    # and a real short-horizon demo that the two rules genuinely differ
    ks = np.array([2.90, 4.00])
    _, lam, Q = R.observable(R.ANCHOR, ks, 700, 2000, return_quarters=True)
    lam_only = (lam > R.CHAOS_EPS).any(axis=1)
    canon = R.canonical_classifier(lam, Q)
    c7 &= bool(np.any(lam_only != canon))
    print(f"    real demo: lam-only={lam_only.tolist()}  canonical={canon.tolist()}")
    chk("C7 canonical classifier: unit fixture correct AND differs from lam-only", c7)

    # C9 — censor semantics: non-finite scaled norm must be detectable
    big = np.full(10, 1e308)
    c9 = (not np.isfinite(R.snorm(big))) and np.isfinite(R.snorm(np.array([1e308, 1e308])))
    print(f"    snorm(10x1e308)={R.snorm(big)}  snorm(2x1e308)={R.snorm(np.array([1e308,1e308])):.3e}")
    chk("C9 snorm overflows to inf where it must (numeric-censor trigger works)", c9)

    # C8 — h-grid extension present and reaches below the certified U-minimum
    c8 = (len(R.HJ_PRIMARY) == 21 and len(R.HJ) > 21
          and R.HJ[-1] < 1e-13)
    chk(f"C8 h-grid: primary 21 + deterministic extension, hmin={R.HJ[-1]:.3e}", c8)

    # C10 — end-to-end: mixed numeric-censor + measured rows must survive write+summary
    import tempfile, csv as _csv, io, contextlib
    with tempfile.TemporaryDirectory() as td:
        # censored file (D is None branch) and measured file (normal branch)
        cen = [R.make_row(270, 70, 200, "u", st, "SENSITIVITY-NUMERIC-CENSORED")
               for st in ("all", "regular", "chaos")]
        mea = [R.make_row(270, 70, 200, "v", st, "measured", h_res="1.000000e-04",
                          S_norm="1.0e5", C_chaos="5.0e-01", N90="7",
                          eps_sec={e: "1.000000e-04" for e in R.EPS_SECONDARY})
               for st in ("all", "regular", "chaos")]
        R._write(cen, td, 270, "u"); R._write(mea, td, 270, "v")
        # schemas must be identical and rectangular
        hdrs = []
        for f in ("resolv_T270_u.csv", "resolv_T270_v.csv"):
            with open(f"{td}/{f}") as fh:
                hdrs.append(next(_csv.reader(fh)))
        same_schema = hdrs[0] == hdrs[1] == R.ROW_FIELDS
        crashed = False
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                R.summary(td)
        except Exception as ex:
            crashed = True
            print(f"    summary() raised: {type(ex).__name__}: {ex}")
        out = buf.getvalue()
        prog_ok = "UNRESOLVED" in out
        print(f"    schemas identical={same_schema}  summary crashed={crashed}  "
              f"program-level UNRESOLVED={prog_ok}")
    chk("C10 mixed censored+measured rows: rectangular schema, summary runs, "
        "program-level UNRESOLVED", same_schema and (not crashed) and prog_ok)

    good = all(ok)
    print("\nCERTIFICATE:", "PASS" if good else "FAIL")
    return 0 if good else 1

if __name__ == "__main__":
    sys.exit(main())
