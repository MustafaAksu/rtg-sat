"""HHO Addendum 7 §A7.3 — falsification test of the Brauer-tree leaf criterion on cyclic C6 data.

Uses the HCG engine unchanged: cyclic_disc_claude.py (its family() and census() functions,
which call generic_engine.py / Severn v2 Lemma 7.2 formula). This runner only adds new exponent vectors.

Usage (all three files in the current folder):
  python HHO_C6_LEAF_TEST_v0_1.py
Optional: python HHO_C6_LEAF_TEST_v0_1.py <engine dir> <path to cyclic_disc_claude.py>

Prediction (leaf criterion + Hilbert reciprocity): for exponent vectors with m(chi_4)=0 the class must be [1].
A non-[1] class on any TEST row refutes the leaf criterion or its transfer step.
"""
import sys, importlib.util

def m_chi(a, exps, n=6):
    return -2 + sum(1 for e in exps if (a * e) % n)

def main():
    # Defaults: all files in the current working folder (relative paths).
    eng = sys.argv[1] if len(sys.argv) > 1 else "."
    src = sys.argv[2] if len(sys.argv) > 2 else "cyclic_disc_claude.py"
    sys.path.insert(0, eng)
    print("=== loading engine (its built-in C6/C3 controls print first) ===")
    spec = importlib.util.spec_from_file_location("cdc", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    rows = [
        ("CONTROL  C6 separator",          [2,2,2,2,2,3,4,4,4,5], "no prediction (m4>0); recorded [2]"),
        ("TEST-1   (3^8,1,5)",             [3,3,3,3,3,3,3,3,1,5], "predict [1]"),
        ("TEST-1p  (3^8,1,5) reordered",   [1,3,3,3,5,3,3,3,3,3], "predict [1]; same as TEST-1"),
        ("TEST-2   (3^8,2,4)",             [3,3,3,3,3,3,3,3,2,4], "predict [1]"),
        ("TEST-2p  (3^8,2,4) reordered",   [3,2,3,3,3,3,4,3,3,3], "predict [1]; same as TEST-2"),
    ]
    print("\n=== HHO leaf-criterion test ===")
    results = []
    for label, ex, pred in rows:
        assert sum(ex) % 6 == 0
        print(f"\n[{label}] m(chi1)={m_chi(1,ex)} m(chi4)={m_chi(4,ex)} m(chi2)={m_chi(2,ex)} | {pred}")
        d = mod.family(6, ex, label)
        cls = mod.norm_class(d)
        results.append((label, cls, pred))
    print("\n=== SUMMARY ===")
    bad = False
    for label, cls, pred in results:
        verdict = ""
        if label.startswith("TEST"):
            verdict = "CONSISTENT" if cls == "[1]" else "REFUTES LEAF CRITERION"
            bad |= cls != "[1]"
        print(f"{label:34s} class={cls:8s} {verdict}")
    print("OVERALL:", "LEAF CRITERION REFUTED" if bad else "ALL TEST ROWS CONSISTENT")

if __name__ == "__main__":
    main()
