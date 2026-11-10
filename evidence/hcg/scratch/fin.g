w := E(3); i3 := E(3) - E(3)^2; M := (1/i3) * [[1,1,1],[1,w,w^2],[1,w^2,w]];
G := Group([DiagonalMat([1,1,w]), M*DiagonalMat([1,1,w])*M^-1, DiagonalMat([-1,1,1])]);
Print("finite? ", IsFinite(G), "\n");
if IsFinite(G) then Print("size ", Size(G), "\n"); fi;
QUIT;
