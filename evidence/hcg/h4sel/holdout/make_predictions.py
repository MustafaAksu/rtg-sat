"""Holdout predictions for HCG_H4_BLIND_CHALLENGE_v0_1 using ONLY edgeform_predict.py (root/tree data).
No monodromy, braid or cocycle routine is imported or run."""
import json, sys, hashlib
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0,'/home/claude/g34/h4sel/holdout')
import edgeform_predict as P
IN='/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT'
def laminar(cv):
    for a,b in cv:
        for c,d in cv:
            if not (b<c or d<a or (a<=c and d<=b) or (c<=a and b<=d)): return False
    return True
out={'protocol':'HCG_H4_BLIND_CHALLENGE_v0_1','predictor':'edgeform_predict.py (predict(), beta_rows())',
     'predictor_sha256':hashlib.sha256(open('/home/claude/g34/h4sel/holdout/edgeform_predict.py','rb').read()).hexdigest(),
     'input_manifest_sha256':hashlib.sha256(open(IN+'/INPUT_MANIFEST.json','rb').read()).hexdigest(),
     'hermitian_coordinates':'for a K-basis of L (nullspace RREF basis of the 6x10 root matrix): 4 diagonal entries (rational), then for p<q the pair (x,y) of B[p][q]=x+y*w; 16 rational coordinates. Left-nullspace relations are independent of this choice.',
     'left_nullspace_normalization':'basis of {q in Q^17 : sum_e q_e B_e = 0}, given as the rows of the reduced row echelon form (pivot entries 1), coefficients indexed by the curve order of the input tree JSON',
     'cases':[]}
for c in ['NEW01','NEW02','NEW03','NEW04']:
    roots=json.load(open(f'{IN}/{c}_roots.json'))['generating_reflection_roots']
    trees=json.load(open(f'{IN}/{c}_trees.json'))['curves']
    V=[[(F(str(a)),F(str(b))) for a,b in v] for v in roots]
    for ti,cv in enumerate(trees):
        cv=[tuple(x) for x in cv]
        assert len(cv)==17 and laminar(cv) and all((2*i-1,2*i) in cv for i in range(1,11)) and all(a%2==1 and b%2==0 for a,b in cv)
        dL,qr,kr=P.predict(roots,cv)
        rows=P.beta_rows(roots,cv)
        M=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in r] for r in rows])   # 17 x 16
        ns=M.T.nullspace()          # q with q^T M = 0
        if ns:
            R=sp.Matrix.hstack(*ns).T.rref()[0]
            basis=[[str(R[i,j]) for j in range(R.shape[1])] for i in range(R.shape[0]) if any(R[i,j]!=0 for j in range(R.shape[1]))]
        else: basis=[]
        # root-span K-dimension
        rootspan=6 if dL==4 else 10-dL
        assert len(basis)==17-qr
        out['cases'].append({'case_id':c,'tree_index':ti,'curves':[list(x) for x in cv],'root_span_K_dim':rootspan,
            'dimK_L':dL,'predicted_individual_K_ranks':kr,'predicted_Q_span_rank':qr,
            'predicted_H4':qr==16,'left_nullspace_rref':basis})
        print(c,ti,'rootspan',rootspan,'Qrank',qr,'K-ranks',kr,'nullity',len(basis))
json.dump(out,open('/home/claude/g34/h4sel/holdout/H4_HOLDOUT_PREDICTIONS.json','w'),indent=1)
