# Claude: finite test of the three-pseudoreflection lemma: if R1 R2 R3 is scalar for projective pseudoreflections
# (elements with an eigenvalue of multiplicity exactly 2), then R1, R2, R3 pairwise commute.
# Tested inside primitive finite subgroups of GL_3(C) containing many noncommuting pseudoreflections.
w := E(3); i3 := E(3)-E(3)^2;
M := (1/i3) * [[1,1,1],[1,w,w^2],[1,w^2,w]];
Norm1 := function(g) local f; f := First(Flat(g), x -> x <> 0); return g / f; end;   # projective key
IsProjPR := function(g)
  local n, k; n := Order(g);
  if g = g[1][1]*IdentityMat(3) then return false; fi;
  for k in [0..n-1] do
    if RankMat(g - E(n)^k*IdentityMat(3)) = 1 then return true; fi;
  od;
  return false;
end;
PRTest := function(name, gens)
  local G, pr, keys, cnt, bad, ncp, x, y, z0, key, pos, z;
  G := Group(gens);
  pr := Filtered(AsList(G), IsProjPR);
  keys := List(pr, Norm1); SortParallel(keys, pr);
  cnt := 0; bad := 0; ncp := 0;
  for x in pr do for y in pr do
    if x*y <> y*x then ncp := ncp + 1; fi;
    z0 := (x*y)^-1;
    if z0 = z0[1][1]*IdentityMat(3) then continue; fi;   # then z would have to be scalar: not a pseudoreflection
    key := Norm1(z0); pos := PositionSorted(keys, key);
    if pos <= Length(keys) and keys[pos] = key then
      z := pr[pos]; cnt := cnt + 1;
      if not (x*y = y*x and x*z = z*x and y*z = z*y) then bad := bad + 1; fi;
    fi;
  od; od;
  Print(name, ": |G|=", Size(G), " projective pseudoreflections=", Length(pr), " noncommuting ordered pairs=", ncp,
        " pairs (x,y) completed to scalar-product triples=", cnt, " non-commuting such triples=", bad, "\n");
end;
PRTest("Hessian-type <diag(1,1,w), M diag(1,1,w) M^-1>", [ DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1 ]);
PRTest("same + coordinate transposition", [ DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1, [[0,1,0],[1,0,0],[0,0,1]] ]);
PRTest("monomial G(3,1,3)", [ DiagonalMat([1,1,w]), [[0,1,0],[1,0,0],[0,0,1]], [[1,0,0],[0,0,1],[0,1,0]] ]);
QUIT;
