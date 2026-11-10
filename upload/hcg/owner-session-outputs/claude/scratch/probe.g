LoadPackage("ctbllib");
for nam in ["L2(43)","2.L2(43)","L2(89)","2.L2(89)"] do Print(nam, ": ", CharacterTable(nam) <> fail, "\n"); od;
t := CharacterTable("SL", 2, 43); Print("generic SL(2,43): ", t <> fail, " ", Size(t), "\n");
t := CharacterTable("SL", 2, 89); Print("generic SL(2,89): ", t <> fail, " ", Size(t), "\n");
QUIT;
