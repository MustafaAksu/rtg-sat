# Claude: cross-check of the Katz-Tiep unitary Weil formula against the CTblLib table of U7(2) = SU7(2).
# Formula (n = 7 odd, q = 2): zeta_i(g) = -(1/3) * Sum_j rho^(i*j) * (-2)^f_j(g),  i = 0,1,2,
# f_j(g) = dim_F4 ker(g - xi^j) on the natural module.  Inversion: (-2)^f_k = - Sum_i rho^(-i*k) * zeta_i(g).
# For each class we recover (f_0,f_1,f_2) from the table's 42- and 43-dimensional characters and check:
#   every recovered value is (-2)^f with 0 <= f <= 7, sum f <= 7, f_j <= 6 off the identity,
#   |chi_43(g)|^2 <= 4167/9 off the identity (so |chi_43| < 67/3 < 23),
#   moving rank c(g) = 43 - mult_1 (via power maps) >= 11, and report the exact minimum and its f-triple.
LoadPackage("ctbllib");
t := CharacterTable("U7(2)");
rho := E(3);
mult1 := function(chi, i) local o; o := OrdersClassRepresentatives(t)[i];
  return Sum([0..o-1], k -> chi[PowerMap(t, k, i)]) / o; end;
c42 := Filtered(Irr(t), x -> x[1] = 42);
c43 := Filtered(Irr(t), x -> x[1] = 43);
Print("degree-42 characters: ", Length(c42), "   degree-43 characters: ", Length(c43), "\n");
pw := List([0..7], f -> (-2)^f);
best := fail;
for z0 in c42 do
 for perm in [[1,2],[2,1]] do
  z := [z0, c43[perm[1]], c43[perm[2]]];
  ok := true; trip := [];
  for cl in [1..NrConjugacyClasses(t)] do
    x := List([0..2], k -> -Sum([0..2], i -> rho^(-i*k) * z[i+1][cl]));
    if not ForAll(x, v -> v in pw) then ok := false; break; fi;
    f := List(x, v -> Position(pw, v) - 1);
    if Sum(f) > 7 then ok := false; break; fi;
    Add(trip, f);
  od;
  if ok then best := [z, trip, perm]; fi;
 od;
od;
if best = fail then Error("NO assignment matches the Weil formula"); fi;
z := best[1]; trip := best[2];
Print("Weil formula matches CTblLib with zeta_1 = c43[", best[3][1], "], zeta_2 = c43[", best[3][2], "] on all ",
      NrConjugacyClasses(t), " classes\n");
Print("identity triple: ", trip[1], "\n");
noid := [2..NrConjugacyClasses(t)];
Print("max f_j off identity: ", Maximum(List(noid, i -> Maximum(trip[i]))), "\n");
Print("max sum f off identity: ", Maximum(List(noid, i -> Sum(trip[i]))), "\n");
for a in [2,3] do
  chi := z[a];
  m2 := Maximum(List(noid, i -> chi[i] * GaloisCyc(chi[i], -1)));
  Print("zeta_", a-1, ": max |chi|^2 off identity = ", m2, "  (bound 4167/9 = ", 4167/9, ")  <= bound: ", m2 <= 4167/9, "\n");
  cs := List(noid, i -> 43 - mult1(chi, i));
  mn := Minimum(cs);
  Print("zeta_", a-1, ": min moving rank = ", mn, " (>= 11: ", mn >= 11, ")  attained at classes ",
        List(Filtered([1..Length(noid)], j -> cs[j] = mn), j -> ClassNames(t)[noid[j]]),
        " with f-triples ", List(Filtered([1..Length(noid)], j -> cs[j] = mn), j -> trip[noid[j]]),
        " and values ", List(Filtered([1..Length(noid)], j -> cs[j] = mn), j -> chi[noid[j]]), "\n");
od;
# realised f-triples and the analytic bound per triple
Print("number of distinct realised f-triples off identity: ", Length(Set(trip{noid})), "\n");
QUIT;
