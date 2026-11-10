# Claude: sanity check of the Weil-character identity |chi_W(h)|^2 = q^{dim ker(h-1)} (Thomas Thm 1A) on tables in CTblLib:
# Sp4(3)=2.U4(2) (Weil 4+5), Sp6(3)=2.S6(3) (Weil 13+14). For each pair of a faithful degree-(q^n-1)/2 and a
# non-faithful degree-(q^n+1)/2 character whose sum has |value|^2 a power of 3 at every class, report it.
LoadPackage("ctbllib");
for c in [["2.U4(2)",4,5,2],["2.S6(3)",13,14,3]] do
  t:=CharacterTable(c[1]); irr:=Irr(t); ok:=0; total:=0;
  A:=Filtered(irr,x->x[1]=c[2]); B:=Filtered(irr,x->x[1]=c[3]);
  for x in A do for y in B do
    s:=x+y; total:=total+1;
    v:=List(s,z->z*GaloisCyc(z,-1));
    if ForAll(v,w->IsRat(w) and w>0 and ForAny([0..2*c[4]],k->w=3^k)) then ok:=ok+1;
      Print(c[1]," Weil pair ",x[1],"+",y[1],": |chi_W|^2 values = ",Set(v),"\n"); fi;
  od; od;
  Print(c[1],": ",ok," of ",total," (deg ",c[2],",",c[3],") pairs have |sum|^2 in {3^k} at every class\n");
od;
QUIT;
