# HCG: portable raw character/power-map export. Independent reader consumes this JSON.
# This script was prepared by ChatGPT but NOT executed in the present environment.
# Run: gap -q -b export_all_candidate_characters.g
# Requires CTblLib. No network and no shell commands are used.
if LoadPackage("ctbllib") <> true then Error("CTblLib required"); fi;
ExportHCG := function()
    local outfile,cands,c,t,irs,inds,sel,center,ord,pows,ext,fus,
          row,chi,ab,v,a,b,i,j,k,first,firstchi,files;
    outfile := "all_candidate_character_data.json";
    cands := [["3.O7(3)",27],["3.G2(3)",27],["U4(2)",30],
              ["2.U4(2)",36],["3_2.U4(3)",36],["6.A7",36],
              ["6.L3(4)",36],["U4(2)",40],["S8(3)",41]];
    PrintTo(outfile,"{\"gap_version\":\"",GAPInfo.Version,"\",\"ctbllib_version\":\"",
            PackageInfo("ctbllib")[1].Version,"\",\"tables\":[");
    first:=true;
    for c in cands do
        t:=CharacterTable(c[1]);
        if t=fail then Error("Missing required table: ",c[1]); fi;
        irs:=Irr(t); inds:=Indicator(t,irs,2);
        sel:=Filtered([1..Length(irs)],i->irs[i][1]=c[2] and inds[i]=0
             and IsSubset(CF(3),Field(Rationals,irs[i]))
             and ClassPositionsOfKernel(irs[i])=[1]);
        if Length(sel)=0 then Error("No matching characters for ",c);fi;
        center:=ClassPositionsOfCentre(t);ord:=OrdersClassRepresentatives(t);
        if not first then AppendTo(outfile,",");fi;first:=false;
        AppendTo(outfile,"{\"name\":\"",c[1],"\",\"dimension\":",c[2],
          ",\"group_order\":\"",Size(t),"\",\"center\":",List(center,x->x-1),
          ",\"orders\":",ord,",\"powers\":[");
        for i in [1..Length(ord)] do
            if i>1 then AppendTo(outfile,",");fi;
            pows:=List([0..ord[i]-1],j->PowerMap(t,j,i)-1);
            AppendTo(outfile,pows);
        od;
        AppendTo(outfile,"],\"characters\":[");firstchi:=true;
        for row in sel do
            chi:=irs[row];
            if not firstchi then AppendTo(outfile,",");fi;firstchi:=false;
            AppendTo(outfile,"{\"row_id\":",row,",\"values\":[");
            for i in [1..Length(chi)] do
                v:=chi[i];b:=(v-GaloisCyc(v,-1))/(E(3)-E(3)^2);a:=v-b*E(3);
                if not IsRat(a) or not IsRat(b) then Error("Non-K character value");fi;
                if i>1 then AppendTo(outfile,",");fi;
                AppendTo(outfile,"[\"",a,"\",\"",b,"\"]");
            od;
            AppendTo(outfile,"]}");
        od;
        AppendTo(outfile,"]");
        if c[1]="3.O7(3)" then
            ext:=CharacterTable("3.O7(3).2");
            if ext=fail then Error("Missing outer extension table");fi;
            fus:=GetFusionMap(t,ext);
            if fus=fail then Error("Missing stored class fusion");fi;
            AppendTo(outfile,",\"outer_index\":",Size(ext)/Size(t),
                 ",\"outer_fusion\":",List(fus,x->x-1));
        fi;
        AppendTo(outfile,"}");
    od;
    AppendTo(outfile,"]}\n");
    Print("RAW CHARACTER EXPORT COMPLETE: ",outfile,"\n");
end;
ExportHCG();
QUIT;
