# Claude: scan CTblLib for faithful irreducible characters of quasisimple groups in degrees 25..42 (char 0).
# For each: centre order, Frobenius-Schur indicator, character field (is it inside Q(sqrt-3)=CF(3)? equal?),
# and the minimal moving rank d - mult_1(h) over noncentral classes h (mult_1 via power maps).
LoadPackage("ctbllib");
mult1 := function(t, chi, i)
  local o, s, k;
  o := OrdersClassRepresentatives(t)[i]; s := 0;
  for k in [0..o-1] do s := s + chi[PowerMap(t, k, i)]; od;
  return s / o;
end;
names := AllCharacterTableNames(IsPerfect, true, IsDuplicateTable, false);;
Print("perfect tables scanned: ", Length(names), "\n");
for nam in names do
  t := CharacterTable(nam);
  if t = fail then continue; fi;
  degs := List(Irr(t), x -> x[1]);
  if ForAll(degs, x -> x < 25 or x > 42) then continue; fi;
  cen := ClassPositionsOfCentre(t);
  f := t / cen;
  if not IsSimpleCharacterTable(f) then continue; fi;
  for chi in Irr(t) do
    d := chi[1];
    if d < 25 or d > 42 then continue; fi;
    if ClassPositionsOfKernel(chi) <> [1] then continue; fi;
    z := Sum(cen, i -> SizesConjugacyClasses(t)[i]);
    ind := Indicator(t, [chi], 2)[1];
    F := Field(Rationals, chi);
    inK := IsSubset(CF(3), F);
    noncen := Difference([1..NrConjugacyClasses(t)], cen);
    mr := Minimum(List(noncen, i -> d - mult1(t, chi, i)));
    Print(nam, " d=", d, " |Z|=", z, " ind=", ind, " field=", F, " inK=", inK,
          " minMovingRank=", mr, "\n");
  od;
od;
QUIT;
