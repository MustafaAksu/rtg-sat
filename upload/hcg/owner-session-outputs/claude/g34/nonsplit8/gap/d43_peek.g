# Claude: peek at the next primitive candidates with field K (non-self-dual) beyond d = 42 (HM corrigenda rows):
# U7(2) degree 43 (z3), U4(2) degree 45 (z3). Report min moving rank over noncentral classes (Lemma C threshold at
# d = 43..45 is 2*floor((2d+8)/19) = 8, 8, 10).
LoadPackage("ctbllib");
mult1 := function(t, chi, i) local o; o := OrdersClassRepresentatives(t)[i];
  return Sum([0..o-1], k -> chi[PowerMap(t, k, i)]) / o; end;
for c in [["U7(2)",43],["U4(2)",45]] do
  t := CharacterTable(c[1]);
  if t = fail then Print(c[1], ": no table\n"); continue; fi;
  cen := ClassPositionsOfCentre(t);
  chis := Filtered(Irr(t), x -> x[1] = c[2] and Indicator(t,[x],2)[1] = 0 and IsSubset(CF(3), Field(Rationals,x)));
  for chi in chis do
    noncen := Difference([1..NrConjugacyClasses(t)], cen);
    Print(c[1], " d=", c[2], " min moving rank=", Minimum(List(noncen, i -> c[2] - mult1(t, chi, i))), "\n");
  od;
od;
QUIT;
