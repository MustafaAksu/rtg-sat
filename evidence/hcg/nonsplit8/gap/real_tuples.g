# Claude: does "every local monodromy conjugate to its inverse" (Severn's sufficient condition for (L), PO-4) force a split
# local discriminant product?  Exact experiment in finite subgroups of U_3(K), K = Q(sqrt(-3)), standard form H = I.
# Local factor of g (locality theorem): a(g) b(g), a = Gram det on E = im(1-g), b = det((1-g)|E).
# (A) For every real class (g ~ g^-1 in G) check a*b is rational and [a b] = [ disc(E_{-1}(g)) * 2^{dim E_{-1}} ].
# (B) Random product-one tuples of real elements generating an absolutely irreducible subgroup with character field K:
#     record the class of prod a_j b_j in Q^*/N(K^*)  ([1] = split part; the global sign (-1)^n is separate).
SizeScreen([4096, 24]);
w := E(3); i3 := E(3) - E(3)^2; z6 := -E(3)^2;
M := (1/i3) * [[1,1,1],[1,w,w^2],[1,w^2,w]];
LocalAB := function(g)
  local d, Mv, E, Gram, C, a, b;
  d := Length(g); Mv := IdentityMat(d) - g; E := BaseMat(Mv);
  if E = [] then return 1; fi;
  Gram := List(E, x -> List(E, y -> x * ComplexConjugate(y)));
  C := List(E, x -> SolutionMat(E, x * Mv));
  return Determinant(Gram) * Determinant(C);
end;
MinusDisc := function(g)                       # [disc(E_-1) * 2^dim E_-1]
  local d, E, Gram;
  d := Length(g); E := NullspaceMat(g + IdentityMat(d));
  if E = [] then return 1; fi;
  Gram := List(E, x -> List(E, y -> x * ComplexConjugate(y)));
  return Determinant(Gram) * 2^Length(E);
end;
NClass := function(q)                          # primes p = 2 mod 3 with odd valuation, and the sign
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
AbsIrr := function(gens)                      # commutant dimension 1 (over the cyclotomics)
  local d, rows, i, j, k, l, g, eqs, X;
  d := Length(gens[1]); eqs := [];
  for g in gens do
    # unknown X (d x d) flattened; equation X g - g X = 0
    for i in [1..d] do for j in [1..d] do
      rows := List([1..d*d], x -> 0);
      for k in [1..d] do rows[(i-1)*d + k] := rows[(i-1)*d + k] + g[k][j]; od;   # (X g)_{ij} = sum_k X_ik g_kj
      for k in [1..d] do rows[(k-1)*d + j] := rows[(k-1)*d + j] - g[i][k]; od;   # (g X)_{ij} = sum_k g_ik X_kj
      Add(eqs, rows);
    od; od;
  od;
  return Length(NullspaceMat(TransposedMat(eqs))) = 1;
end;
Experiment := function(name, gens, trials, Nset)
  local G, cls, real, r, ok, el, realel, t, N, tup, P, H, chf, prod, cl, stats, key, x, g, tried, kept;
  G := Group(gens);
  cls := ConjugacyClasses(G);
  real := Filtered(cls, c -> Representative(c)^-1 in c);
  ok := true;
  for c in real do
    g := Representative(c);
    x := LocalAB(g);
    if not x in Rationals then ok := false; Print("  nonrational a*b on a real class!\n"); fi;
    if NClass(x) <> NClass(MinusDisc(g)) then ok := false; Print("  reduction FAILS on ", g, "\n"); fi;
  od;
  Print(name, ": |G| = ", Size(G), ", classes ", Length(cls), ", real classes ", Length(real),
        ", FIRST-VERSION reduction (x+1 only; superseded, see real_reduction_check.g) holds on all real classes: ", ok, "\n");
  realel := Concatenation(List(real, AsList));
  stats := rec(); tried := 0; kept := 0;
  for t in [1..trials] do
    N := Random(Nset);
    tup := List([1..N-1], i -> Random(realel));
    P := Product(tup)^-1;
    if not P in realel or P = One(G) then continue; fi;
    Add(tup, P); tried := tried + 1;
    if not AbsIrr(tup) then continue; fi;
    H := Group(tup);
    chf := Field(Rationals, List(ConjugacyClasses(H), c -> TraceMat(Representative(c))));
    if chf <> CF(3) then continue; fi;
    kept := kept + 1;
    prod := Product(List(tup, LocalAB));
    cl := NClass(prod);
    key := Concatenation("sign", String(cl[1]), "_odd", String(cl[2]));
    if not IsBound(stats.(key)) then stats.(key) := 0; fi;
    stats.(key) := stats.(key) + 1;
  od;
  Print("  product-one real tuples tried ", tried, ", abs. irreducible with character field K: ", kept,
        "; classes of prod a_j b_j: ", stats, "\n");
end;
Experiment("G(3,1,3)", [DiagonalMat([1,1,w]), [[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]], 3000, [4..8]);
Experiment("G(6,1,3)", [DiagonalMat([1,1,z6]), [[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]], 3000, [4..8]);
Experiment("G(6,2,3)", [DiagonalMat([1,w,w^2]), DiagonalMat([-1,-1,1]), DiagonalMat([z6,z6^-1,1])*[[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]]], 3000, [4..8]);
Experiment("<two order-3 reflections> (order 24, G4-type)", [DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1], 3000, [4..8]);
Experiment("<two order-3 reflections, (1 2)> (order 1296, G26-type)", [DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1, [[0,1,0],[1,0,0],[0,0,1]]], 3000, [4..8]);
QUIT;
