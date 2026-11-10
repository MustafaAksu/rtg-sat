# Claude: export product-one tuples of real elements in the order-1296 group <diag(1,1,w), M diag(1,1,w) M^-1, (1 2)>
# (G26-type, standard form) that generate an absolutely irreducible subgroup with character field K and have EVEN
# parabolic dimension 2n = sum c_j - 2*3.  Records n, the class of prod a_j b_j, and the matrices (entries a + b*w as [a,b])
# for a direct cup-form computation (python: real_g26_cup_claude.py).
SizeScreen([4096, 24]);
w := E(3); i3 := E(3) - E(3)^2;
M := (1/i3) * [[1,1,1],[1,w,w^2],[1,w^2,w]];
B := Basis(CF(3), [1, E(3)]);
Enc := m -> List(m, r -> List(r, x -> List(Coefficients(B, x), String)));
LocalAB := function(g)
  local d, Mv, E, Gram, C;
  d := Length(g); Mv := IdentityMat(d) - g; E := BaseMat(Mv);
  if E = [] then return 1; fi;
  Gram := List(E, x -> List(E, y -> x * ComplexConjugate(y)));
  C := List(E, x -> SolutionMat(E, x * Mv));
  return Determinant(Gram) * Determinant(C);
end;
NClass := function(q)
  local s, odd, f, p;
  s := SignInt(q); q := AbsoluteValue(q); odd := [];
  for f in [NumeratorRat(q), DenominatorRat(q)] do
    for p in Set(FactorsInt(f)) do
      if p > 1 and p mod 3 = 2 and (Number(FactorsInt(f), x -> x = p) mod 2) = 1 then AddSet(odd, p); fi;
    od;
  od;
  return [s, odd];
end;
AbsIrr := function(gens)
  local d, rows, i, j, k, g, eqs;
  d := Length(gens[1]); eqs := [];
  for g in gens do
    for i in [1..d] do for j in [1..d] do
      rows := List([1..d*d], x -> 0);
      for k in [1..d] do rows[(i-1)*d + k] := rows[(i-1)*d + k] + g[k][j]; od;
      for k in [1..d] do rows[(k-1)*d + j] := rows[(k-1)*d + j] - g[i][k]; od;
      Add(eqs, rows);
    od; od;
  od;
  return Length(NullspaceMat(TransposedMat(eqs))) = 1;
end;
Reset(GlobalMersenneTwister, 20261103);
G := Group([DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1, [[0,1,0],[1,0,0],[0,0,1]]]);
real := Filtered(ConjugacyClasses(G), c -> Representative(c)^-1 in c);
realel := Concatenation(List(real, AsList));
stats := rec(); kept := 0; ex := []; need := rec();
for t in [1..6000] do
  N := Random([4..8]);
  tup := List([1..N-1], i -> Random(realel));
  P := Product(tup)^-1;
  if not P in realel or P = One(G) then continue; fi;
  Add(tup, P);
  cs := List(tup, g -> RankMat(IdentityMat(3) - g));
  if Sum(cs) mod 2 = 1 or Sum(cs) - 6 <= 0 then continue; fi;
  n := (Sum(cs) - 6) / 2;
  if not AbsIrr(tup) then continue; fi;
  H := Group(tup);
  if Field(Rationals, List(ConjugacyClasses(H), c -> TraceMat(Representative(c)))) <> CF(3) then continue; fi;
  kept := kept + 1;
  cl := NClass(Product(List(tup, LocalAB)));
  key := Concatenation("n", String(n mod 2 = 0), "_odd", String(cl[2]), "_sign", String(cl[1]));
  if not IsBound(stats.(key)) then stats.(key) := 0; fi;
  stats.(key) := stats.(key) + 1;
  if not IsBound(need.(key)) then need.(key) := 0; fi;
  if need.(key) < 3 and Sum(cs) <= 16 then
    need.(key) := need.(key) + 1;
    Add(ex, rec(n := n, N := N, c := cs, cls := Concatenation(String(cl[1]), ":", String(cl[2])), mats := List(tup, Enc)));
  fi;
od;
Print("kept (abs. irreducible, field K, even parabolic dimension): ", kept, "\n");
Print("classes of prod a_j b_j by (n even?, odd primes, sign): ", stats, "\n");
PrintTo("real_g26_examples.json", "[");
for i in [1..Length(ex)] do
  e := ex[i];
  AppendTo("real_g26_examples.json", "{\"n\":", e.n, ",\"N\":", e.N, ",\"c\":", e.c, ",\"cls\":\"", e.cls, "\",\"mats\":", e.mats, "}");
  if i < Length(ex) then AppendTo("real_g26_examples.json", ","); fi;
od;
AppendTo("real_g26_examples.json", "]\n");
Print("exported examples: ", Length(ex), "\n");
QUIT;
