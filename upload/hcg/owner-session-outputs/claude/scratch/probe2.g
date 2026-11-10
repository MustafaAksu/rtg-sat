LoadPackage("ctbllib");
t := CharacterTable("PSL", 2, 47); Print("generic PSL(2,47): ", t <> fail, "\n");
t := CharacterTable("PSL", 2, 49); Print("generic PSL(2,49): ", t <> fail, "\n");
t := CharacterTable("SL", 2, 97); Print("generic SL(2,97): ", t <> fail, "\n");
QUIT;
