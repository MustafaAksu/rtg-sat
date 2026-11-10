# Claude: d = 50, 51 primitive almost-quasisimple screen (char 0), same method as d46_48_screen.g.
# (1) CTblLib scan: faithful irreducible characters of degree 50, 51 of perfect tables with simple central quotient.
# (2) Generic SL2(q): q = 49 (q+1 = 50), q = 101 ((q-1)/2 = 50; (q+1)/2 = 51), + PSL2 quotients.
# Thresholds: self-dual (field Q) 2*floor((2d+8-2*ceil(d/2))/17) = 6 at d = 50, 51; field K 2*floor((2d+8)/19) = 10 at d = 50, 51.
LoadPackage("ctbllib"); SizeScreen([4096, 24]);
mult1 := function(t, chi, i) local o; o := OrdersClassRepresentatives(t)[i];
  return Sum([0..o-1], k -> chi[PowerMap(t, k, i)]) / o; end;
thrSD := d -> 2 * Int((2*d + 8 - 2*Int((d+1)/2)) / 17);
thrK  := d -> 2 * Int((2*d + 8) / 19);
report := function(nam, t, degs)
  local cen, chi, d, ind, F, inK, noncen, mr, thr, verdict, z;
  cen := ClassPositionsOfCentre(t);
  z := Sum(cen, i -> SizesConjugacyClasses(t)[i]);
  for chi in Irr(t) do
    d := chi[1];
    if not d in degs then continue; fi;
    if ClassPositionsOfKernel(chi) <> [1] then continue; fi;
    ind := Indicator(t, [chi], 2)[1];
    F := Field(Rationals, chi);
    inK := IsSubset(CF(3), F);
    noncen := Difference([1..NrConjugacyClasses(t)], cen);
    mr := Minimum(List(noncen, i -> d - mult1(t, chi, i)));
    if not inK then verdict := "field not in K: excluded";
    else
      if F = Rationals then thr := thrSD(d); else thr := thrK(d); fi;
      if mr > thr then verdict := Concatenation("field ", String(F), ", minc ", String(mr), " > ", String(thr), ": excluded by Lemma C");
      else verdict := Concatenation("field ", String(F), ", minc ", String(mr), " <= ", String(thr), ": NOT excluded"); fi;
    fi;
    Print(nam, " d=", d, " |Z|=", z, " ind=", ind, " field=", F, " inK=", inK, " minMovingRank=", mr, " -> ", verdict, "\n");
  od;
end;
Print("thresholds: ", List([50,51], d -> [d, thrSD(d), thrK(d)]), "\n");
names := AllCharacterTableNames(IsPerfect, true, IsDuplicateTable, false);;
Print("(1) perfect non-duplicate CTblLib tables scanned: ", Length(names), "\n");
for nam in names do
  t := CharacterTable(nam);
  if t = fail then continue; fi;
  if ForAll(Irr(t), x -> not x[1] in [50, 51]) then continue; fi;
  if not IsSimpleCharacterTable(t / ClassPositionsOfCentre(t)) then continue; fi;
  report(nam, t, [50, 51]);
od;
Print("(2) generic SL2(q) tables (faithful characters only; PSL2 quotients below)\n");
report("SL2(49)", CharacterTable("SL", 2, 49), [50, 51]);
report("SL2(101)", CharacterTable("SL", 2, 101), [50, 51]);
Print("(2') PSL2 quotients\n");
report("PSL2(49)", CharacterTable("PSL", 2, 49), [50, 51]);
report("PSL2(101)", CharacterTable("PSL", 2, 101), [50, 51]);
Print("done\n");
QUIT;
