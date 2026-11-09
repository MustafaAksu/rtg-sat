#!/usr/bin/env python3
"""
pairbc_certificate.py — PREREG-MM1-PAIRBC v1.0.3 gate.

C1 constants        a_A/a_B/a_C, domain, coarse/fine grids, CF threshold
C2 frozen refs      tri0 2.65 / path3 2.35 present as literals
C3 w0 covariance    same dimensionless w0 ensemble across A/B/C  => u0 = w0/dt
C4 anchor sentinels sentinel kappas match the locked source brackets
C5 decision part.   synthetic (p,r,q) grid: exactly one branch, always
C6 primary firewall decide() must not accept path3 data at all
C7 frozen-A guard   runtime anchor scan cannot mutate the reference constants
C8 replication fw   path3 yields CONCORDANT/DISCORDANT/CENSORED only; never a primary label
C9 protocol         per-update lambda, four-quarter, 25 IC, CF>=15/25, Pair-A horizons

Exit 0 iff all pass.  Run BEFORE any scientific execution.
"""
import sys, math, inspect
import pairbc_experiment as E


def main() -> int:
    ok = []
    def chk(n, c):
        ok.append(bool(c)); print(f"[{'PASS' if c else 'FAIL'}] {n}")

    # ---- C1 constants
    c1 = (abs(E.A_PAIR["A"] - 0.030) < 1e-12 and abs(E.A_PAIR["B"] - 0.100) < 1e-12
          and abs(E.A_PAIR["C"] - 0.156) < 1e-12
          and E.K_LO == 0.5 and E.K_HI == 15.0
          and abs(E.D_COARSE - 0.25) < 1e-12 and abs(E.D_FINE - 0.025) < 1e-12
          and E.N_IC == 25 and E.CF_MIN == 15)
    print(f"    a = {E.A_PAIR}   domain [{E.K_LO},{E.K_HI}]   coarse {E.D_COARSE} fine {E.D_FINE}")
    print(f"    N_IC={E.N_IC}  CF_MIN={E.CF_MIN} (= {E.CF_MIN}/{E.N_IC} = {E.CF_MIN/E.N_IC:.2f})")
    chk("C1 locked constants", c1)

    # ---- C2 frozen references
    c2 = (abs(E.KAPPA_A_REF["tri0"] - 2.65) < 1e-12
          and abs(E.KAPPA_A_REF["path3"] - 2.35) < 1e-12)
    print(f"    KAPPA_A_REF = {E.KAPPA_A_REF}")
    chk("C2 frozen Pair-A reference constants", c2)

    # ---- C3 w0 covariance: same dimensionless w0 across pairs -> u0 = w0/dt
    c3 = True
    for pair in ("A", "B", "C"):
        w0 = E.w0_ensemble()
        u0 = E.u0_for_pair(pair)
        dt = E.DT_PAIR[pair]
        c3 &= all(abs(ua - wa/dt) < 1e-12 and abs(ub - wb/dt) < 1e-12
                  for (ua, ub), (wa, wb) in zip(u0, w0))
    print(f"    dt per pair = {E.DT_PAIR};  |w0 ensemble| = {len(E.w0_ensemble())}")
    chk("C3 w0 ensemble identical across pairs; u0 = w0/dt", c3)

    # ---- C4 anchor sentinels
    s = E.ANCHOR_SENTINELS
    c4 = (abs(s["path3"]["neg"] - 2.30) < 1e-12 and abs(s["path3"]["pos"] - 2.35) < 1e-12
          and abs(s["tri0"]["neg"] - 2.60) < 1e-12 and abs(s["tri0"]["pos"] - 2.65) < 1e-12)
    print(f"    sentinels = {s}")
    chk("C4 anchor sentinels match locked source brackets", c4)

    # ---- C5 decision partition: exactly one branch over a synthetic grid
    labels = set()
    bad = []
    n = 0
    rng = [i/20.0 for i in range(-40, 61)]          # p in [-2, 3]
    rq = [0.5, 0.85, 0.95, 1.0, 1.05, 1.15, 1.5]
    for p in rng:
        for r in rq:
            for q in rq:
                n += 1
                lab = E.decide(p_bc=p, r_beta_B=r, r_beta_C=r, q_B=q, q_C=q, censored=False)
                labels.add(lab)
                if lab not in ("P-beta", "P-kappa", "P-ara", "P-other"):
                    bad.append((p, r, q, lab))
    cens = E.decide(p_bc=1.0, r_beta_B=1.0, r_beta_C=1.0, q_B=1.0, q_C=1.0, censored=True)
    c5 = (not bad) and cens == "P-cens" and labels <= {"P-beta", "P-kappa", "P-ara", "P-other"}
    print(f"    tested {n} synthetic (p,r,q) points -> labels {sorted(labels)}; censored -> {cens}")
    chk("C5 decision partition total & exclusive", c5)

    # ---- C6 primary firewall: decide() has no path3 channel
    sig = inspect.signature(E.decide).parameters
    src = inspect.getsource(E.decide)
    c6 = ("path3" not in src) and not any("path3" in k for k in sig)
    print(f"    decide() params = {list(sig)}")
    chk("C6 primary firewall: decide() cannot receive path3 data", c6)

    # ---- C7 frozen-A guard: mutation attempt must not stick
    before = dict(E.KAPPA_A_REF)
    try:
        E.set_anchor_result("tri0", 2.625)      # simulated runtime anchor scan
    except Exception:
        pass
    c7 = (E.KAPPA_A_REF == before)
    print(f"    after simulated anchor scan (2.625): KAPPA_A_REF = {E.KAPPA_A_REF}")
    chk("C7 runtime anchor scan cannot mutate frozen references", c7)

    # ---- C8 replication firewall
    reps = {E.replication_report("P-kappa", "P-kappa", censored=False),
            E.replication_report("P-kappa", "P-beta", censored=False),
            E.replication_report("P-kappa", None, censored=True)}
    c8 = reps <= {"REPLICATION-CONCORDANT", "REPLICATION-DISCORDANT", "REPLICATION-CENSORED"}
    c8 &= E.replication_report("P-kappa", None, censored=True) == "REPLICATION-CENSORED"
    print(f"    replication outputs = {sorted(reps)}")
    chk("C8 replication yields only its three states; never a primary label", c8)

    # ---- C9 protocol semantics
    psrc = inspect.getsource(E.chaos_fraction)
    c9 = (E.EPS_LAM == 1e-3 and E.N_QUARTERS == 4
          and "quarter" in psrc.lower()
          and E.BURN_A == E.BURN_B == E.BURN_C
          and E.LYAP_A == E.LYAP_B == E.LYAP_C)
    print(f"    eps_lambda={E.EPS_LAM}  quarters={E.N_QUARTERS}  "
          f"burn={E.BURN_A}  lyap={E.LYAP_A} (identical across pairs)")
    chk("C9 per-update lambda, four-quarter persistence, Pair-A horizons preserved", c9)

    good = all(ok)
    print("\nCERTIFICATE:", "PASS" if good else "FAIL")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
