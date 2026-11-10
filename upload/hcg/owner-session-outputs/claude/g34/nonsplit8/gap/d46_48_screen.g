# Claude: d = 46, 47, 48 primitive almost-quasisimple screen (char 0), same method as d44_45_screen.g.
# (1) CTblLib scan: faithful irreducible characters of degree 46..48 of perfect tables with simple central quotient
#     (cross-check of the Hiss-Malle corrected rows: none at 46; at 47 only A9 with ell = 7; char-0 rows at 48).
# (2) Generic SL2(q): q = 47 (degrees q-1 = 46, q = 47, q+1 = 48), q = 49 (q-1 = 48), q = 97 ((q-1)/2 = 48), + PSL2 quotients.
# Thresholds: self-dual (field Q): 2*floor((2d+8-2*ceil(d/2))/17) = 6 for d = 46,47,48;
#             non-self-dual field K: 2*floor((2d+8)/19) = 10 for d = 46,47,48.
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
Print("thresholds: ", List([46,47,48], d -> [d, thrSD(d), thrK(d)]), "\n");
names := AllCharacterTableNames(IsPerfect, true, IsDuplicateTable, false);;
Print("(1) perfect non-duplicate CTblLib tables scanned: ", Length(names), "\n");
for nam in names do
  t := CharacterTable(nam);
  if t = fail then continue; fi;
  if ForAll(Irr(t), x -> not x[1] in [46, 47, 48]) then continue; fi;
  if not IsSimpleCharacterTable(t / ClassPositionsOfCentre(t)) then continue; fi;
  report(nam, t, [46, 47, 48]);
od;
Print("(2) generic SL2(q) tables (faithful characters only; PSL2 quotients below)\n");
report("SL2(47)", CharacterTable("SL", 2, 47), [46, 47, 48]);
report("SL2(49)", CharacterTable("SL", 2, 49), [48]);
report("SL2(97)", CharacterTable("SL", 2, 97), [48]);
Print("(2') PSL2 quotients\n");
report("PSL2(47)", CharacterTable("PSL", 2, 47), [46, 47, 48]);
report("PSL2(49)", CharacterTable("PSL", 2, 49), [48]);
report("PSL2(97)", CharacterTable("PSL", 2, 97), [48]);
Print("done\n");
QUIT;
