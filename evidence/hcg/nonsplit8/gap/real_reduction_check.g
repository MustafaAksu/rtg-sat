# Claude: corrected reduction (Lemma R') for K-real local monodromies, K = Q(sqrt(-3)), standard form H = I.
# For g conjugate in G (a group of K-isometries) to g^-1:
#   [a(g) b(g)] = [ prod_{n >= 2, 3 does not divide n}  disc(E_{Phi_n}(g)) * Phi_n(1)^(dim E_{Phi_n} / phi(n)) ]
# (for 3 | n the K-factors of Phi_n come in pairs f, fbar swapped by inversion and contribute norms).
# The first version (only the factor x + 1) is checked alongside and is expected to FAIL on elements with eigenvalues +-i.
SizeScreen([4096, 24]);
w := E(3); i3 := E(3) - E(3)^2; z6 := -E(3)^2;
M := (1/i3) * [[1,1,1],[1,w,w^2],[1,w^2,w]];
LocalAB := function(g)
  local d, Mv, E, Gram, C;
  d := Length(g); Mv := IdentityMat(d) - g; E := BaseMat(Mv);
  if E = [] then return 1; fi;
  Gram := List(E, x -> List(E, y -> x * ComplexConjugate(y)));
  C := List(E, x -> SolutionMat(E, x * Mv));
  return Determinant(Gram) * Determinant(C);
end;
DiscOf := function(E) return Determinant(List(E, x -> List(E, y -> x * ComplexConjugate(y)))); end;
PhiFactor := function(g)                      # Lemma R'
  local d, res, n, Phi, PM, E;
  d := Length(g); res := 1;
  for n in DivisorsInt(Order(g)) do
    if n = 1 or n mod 3 = 0 then continue; fi;
    Phi := CyclotomicPolynomial(Rationals, n);
    PM := Value(Phi, g);
    E := NullspaceMat(PM);
    if E = [] then continue; fi;
    res := res * DiscOf(E) * Value(Phi, 1)^(Length(E) / Phi_n_deg(n));
  od;
  return res;
end;
Phi_n_deg := n -> Phi(n);
MinusOnly := function(g)                      # first version (x + 1 only)
  local E; E := NullspaceMat(g + IdentityMat(Length(g)));
  if E = [] then return 1; fi;
  return DiscOf(E) * 2^Length(E);
end;
NClass := function(q)
  local s, odd, f, p;
  if q = 0 then return "zero"; fi;
  s := SignInt(q); q := AbsoluteValue(q); odd := [];
  for f in [NumeratorRat(q), DenominatorRat(q)] do
    for p in Set(FactorsInt(f)) do
      if p > 1 and p mod 3 = 2 and (Number(FactorsInt(f), x -> x = p) mod 2) = 1 then AddSet(odd, p); fi;
    od;
  od;
  return [s, odd];
end;
Check := function(name, gens)
  local G, real, c, g, x, okR, okMinus, nonrat, bad;
  G := Group(gens);
  real := Filtered(ConjugacyClasses(G), c -> Representative(c)^-1 in c);
  okR := 0; okMinus := 0; nonrat := 0; bad := [];
  for c in real do
    g := Representative(c); x := LocalAB(g);
    if not x in Rationals then nonrat := nonrat + 1; continue; fi;
    if NClass(x) = NClass(PhiFactor(g)) then okR := okR + 1; else Add(bad, g); fi;
    if NClass(x) = NClass(MinusOnly(g)) then okMinus := okMinus + 1; fi;
  od;
  Print(name, ": real classes ", Length(real), "; a*b rational on all: ", nonrat = 0,
        "; Lemma R' holds on ", okR, "/", Length(real), "; first version (x+1 only) holds on ", okMinus, "/", Length(real), "\n");
  if bad <> [] then Print("  R' failures: ", bad, "\n"); fi;
end;
Check("G(3,1,3)", [DiagonalMat([1,1,w]), [[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]]);
Check("G(6,1,3)", [DiagonalMat([1,1,z6]), [[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]]);
Check("G(6,2,3)", [DiagonalMat([1,w,w^2]), DiagonalMat([-1,-1,1]), DiagonalMat([z6,z6^-1,1])*[[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]]);
Check("<two order-3 reflections> (order 24, G4-type)", [DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1]);
Check("<two order-3 reflections, (1 2)> (order 1296, G26-type)", [DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1, [[0,1,0],[1,0,0],[0,0,1]]]);
QUIT;
