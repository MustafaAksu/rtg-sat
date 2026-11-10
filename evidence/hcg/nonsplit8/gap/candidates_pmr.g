# Claude: for the non-self-dual field-K candidates, (i) minimal moving rank d - mult_1(h) (commutator test),
# (ii) minimal projective moving rank d - max_lambda mult_lambda(h) over noncentral h (needed for lambda*h in Gamma),
# (iii) whether chi is stable under the outer automorphisms present in CTblLib (L.2 etc.).
LoadPackage("ctbllib");
eigmults := function(t, chi, i)   # multiplicities of eigenvalues E(o)^k, k=0..o-1, of chi at class i
  local o, k, j, res;
  o := OrdersClassRepresentatives(t)[i]; res := [];
  for k in [0..o-1] do
    res[k+1] := Sum([0..o-1], j -> chi[PowerMap(t, j, i)] * E(o)^(-j*k)) / o;
  od;
  return res;
end;
cands := [["3.O7(3)",27],["3.G2(3)",27],["U4(2)",30],["2.U4(2)",36],["3_2.U4(3)",36],["6.A7",36],["6.L3(4)",36],
          ["U4(2)",40],["2.S8(3)",40],["S8(3)",41]];
for c in cands do
  t := CharacterTable(c[1]);
  if t = fail then Print(c[1], ": TABLE NOT IN CTblLib\n"); continue; fi;
  cen := ClassPositionsOfCentre(t);
  chis := Filtered(Irr(t), x -> x[1] = c[2] and Indicator(t,[x],2)[1] = 0 and IsSubset(CF(3), Field(Rationals,x))
                                and ClassPositionsOfKernel(x) = [1]);
  for chi in chis{[1]} do
    noncen := Difference([1..NrConjugacyClasses(t)], cen);
    mr := List(noncen, i -> c[2] - eigmults(t, chi, i)[1]);
    pmr := List(noncen, i -> c[2] - Maximum(eigmults(t, chi, i)));
    best := noncen[Position(pmr, Minimum(pmr))];
    Print(c[1], " d=", c[2], " #chis=", Length(chis), " minMR=", Minimum(mr), " minPMR=", Minimum(pmr),
          " at class ", ClassNames(t)[best], " (order ", OrdersClassRepresentatives(t)[best], ") mults ",
          eigmults(t, chi, best), "\n");
    # outer automorphism stability
    for ext in Filtered(NamesOfFusionSources(t), n -> true) do od;
    exts := Filtered(List(["2","3","S3","D8","2^2","6"], s -> Concatenation(c[1], ".", s)), n -> CharacterTable(n) <> fail);
    for en in exts do
      te := CharacterTable(en); fus := GetFusionMap(t, te);
      if fus = fail then Print("   ", en, ": no fusion stored\n"); continue; fi;
      ind := InducedClassFunction(t, chi, te);
      Print("   ", en, ": induced chi has norm ", ScalarProduct(te, ind, ind),
            " (norm 1 => chi NOT stable under the outer part; >1 => stable/extends)\n");
    od;
  od;
od;
QUIT;
