# HHO — G34 block data at p = 2, 5 for the 6-dimensional reflection character.
# Run:  gap -q HHO_G34_BLOCKS_v0_1.g > HHO_G34_BLOCKS_v0_1_out.txt
# Needs: GAP 4 with the CTblLib package (standard in full GAP installs).
# Only reads library character tables; no heavy computation.
# r2: QUIT inside 'if' is not allowed at top level; body moved into a function.
# r3: table names discovered via AllCharacterTableNames(Size, 39191040); every
#     table with a degree-6 Q(omega)-valued irreducible is analysed.

LoadPackage("ctbllib");

HHO_G34_Blocks := function(tbl)
  local irr, omega, cand, i, p, pb, b, modtbl, bi, dec;
  irr := Irr(tbl);
  omega := E(3);
  cand := Filtered([1..Length(irr)], i -> irr[i][1] = 6
            and ForAll(irr[i], x -> x in Field(Rationals, [omega])));
  Print("degree-6 irreducibles with values in Q(omega): ", cand, "\n");
  for i in cand do
    Print("  chi", i, " field = ", Field(Rationals, irr[i]),
          "  Frobenius-Schur indicator = ", Indicator(tbl, 2)[i], "\n");
  od;

  for p in [2, 5] do
    Print("\n=== p = ", p, " ===\n");
    pb := PrimeBlocks(tbl, p);
    for i in cand do
      b := pb.block[i];
      Print("chi", i, ": block ", b, ", defect ", pb.defect[b],
            ", ordinary chars in block: ", Positions(pb.block, b), "\n");
      Print("   their degrees: ", List(Positions(pb.block, b), j -> irr[j][1]), "\n");
    od;
    modtbl := tbl mod p;
    if modtbl = fail then
      Print("Brauer table mod ", p, " not in library.\n");
    else
      bi := BlocksInfo(modtbl);
      for i in cand do
        b := First([1..Length(bi)], k -> i in bi[k].ordchars);
        Print("chi", i, ": BlocksInfo block ", b, ", defect ", bi[b].defect,
              ", ordchars ", bi[b].ordchars, "\n");
        dec := DecompositionMatrix(modtbl, b);
        Print("decomposition matrix (rows = ordchars above):\n");
        PrintArray(dec);
        if bi[b].defect = 1 then
          Print("Brauer tree: ", BrauerTree(dec), "\n");
        fi;
      od;
    fi;
  od;
  Print("\nDONE\n");
end;

HHO_Main := function()
  local ok, names, n, t, found;
  ok := LoadPackage("ctbllib");
  Print("ctbllib loaded: ", ok, "\n");
  names := AllCharacterTableNames(Size, 39191040);
  Print("library tables of order 39191040: ", names, "\n");
  found := 0;
  for n in names do
    t := CharacterTable(n);
    if ForAny(Irr(t), x -> x[1] = 6 and ForAll(x, y -> y in Field(Rationals, [E(3)]))) then
      found := found + 1;
      Print("\n################ TABLE: ", n, " ################\n");
      HHO_G34_Blocks(t);
    else
      Print("skip ", n, ": no degree-6 Q(omega)-valued irreducible\n");
    fi;
  od;
  if found = 0 then Print("NO SUITABLE TABLE FOUND\n"); fi;
end;

HHO_Main();
QUIT;
