# Claude: d = 44, 45 primitive almost-quasisimple screen (char 0).
# (1) CTblLib scan: every faithful irreducible character of degree 44 or 45 of a perfect table with simple central quotient.
# (2) Generic SL2(q) (outside the Hiss-Malle tables): q = 43 (degree q+1 = 44) and q = 89 (degrees (q-1)/2 = 44, (q+1)/2 = 45).
# For each: centre order, indicator, character field, field inside K = CF(3)?, min moving rank over noncentral classes,
# and the Lemma C verdict.  Thresholds (Sum c = 2d+8, N >= 19 effective branches, no element with c <= 2):
#   self-dual (field Q):    two similitude branches c >= ceil(d/2), others >= 3  =>  c_min = 3, Lemma C needs <= 6;
#   non-self-dual, field K: c_min <= floor((2d+8)/19) = 5  =>  Lemma C needs <= 10.
LoadPackage("ctbllib"); SizeScreen([4096, 24]);
mult1 := function(t, chi, i) local o; o := OrdersClassRepresentatives(t)[i];
  return Sum([0..o-1], k -> chi[PowerMap(t, k, i)]) / o; end;
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
    elif F = Rationals then thr := 6;
      if mr > thr then verdict := Concatenation("self-dual, minc ", String(mr), " > 6: excluded by Lemma C");
      else verdict := Concatenation("self-dual, minc ", String(mr), " <= 6: NOT excluded by Lemma C"); fi;
    else thr := 2 * Int((2*d+8)/19);
      if mr > thr then verdict := Concatenation("field K, minc ", String(mr), " > ", String(thr), ": excluded by Lemma C");
      else verdict := Concatenation("field K, minc ", String(mr), " <= ", String(thr), ": NOT excluded"); fi;
    fi;
    Print(nam, " d=", d, " |Z|=", z, " ind=", ind, " field=", F, " inK=", inK, " minMovingRank=", mr, " -> ", verdict, "\n");
  od;
end;
names := AllCharacterTableNames(IsPerfect, true, IsDuplicateTable, false);;
Print("(1) perfect non-duplicate CTblLib tables scanned: ", Length(names), "\n");
for nam in names do
  t := CharacterTable(nam);
  if t = fail then continue; fi;
  if ForAll(Irr(t), x -> not x[1] in [44, 45]) then continue; fi;
  if not IsSimpleCharacterTable(t / ClassPositionsOfCentre(t)) then continue; fi;
  report(nam, t, [44, 45]);
od;
Print("(2) generic SL2(q) tables\n");
report("SL2(43)", CharacterTable("SL", 2, 43), [44]);
report("SL2(89)", CharacterTable("SL", 2, 89), [44, 45]);
Print("(2') PSL2 quotients are covered: a character of SL2(q) with -1 in its kernel is a character of L2(q);\n",
      "    re-run on L2(43), L2(89) for the non-faithful ones:\n");
report("L2(43)", CharacterTable("L2(43)"), [44]);
report("L2(89)", CharacterTable("L2(89)"), [44, 45]);
QUIT;
