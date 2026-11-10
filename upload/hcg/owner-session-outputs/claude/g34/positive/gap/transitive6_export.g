# Claude: export the 16 transitive groups of degree 6 (GAP TransitiveGroups library) as lists of permutation images.
Lst := l -> Concatenation("[", JoinStringsWithSeparator(List(l, String), ","), "]");
out := OutputTextFile("transitive6.json", false);
SetPrintFormattingStatus(out, false);
PrintTo(out, "[");
for k in [1..NrTransitiveGroups(6)] do
  G := TransitiveGroup(6, k);
  els := Lst(List(Elements(G), g -> Lst(ListPerm(g, 6))));
  if k > 1 then AppendTo(out, ",\n"); fi;
  AppendTo(out, "{\"k\":", k, ",\"name\":\"", Name(G), "\",\"order\":", Size(G), ",\"els\":", els, "}");
od;
AppendTo(out, "]\n");
CloseStream(out);
QUIT;
