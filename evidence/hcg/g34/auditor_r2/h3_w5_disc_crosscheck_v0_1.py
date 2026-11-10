#!/usr/bin/env python3
"""Exact scalar-extension check of a supplied W5 Gram matrix; no G34 engine imports."""
import json, hashlib, pathlib
from sympy import Matrix, Rational, sqrt, simplify
p=pathlib.Path(__file__).with_name('g34_cert_tuple5_balanced.json')
d=json.loads(p.read_text(encoding='utf-8'))
w=(-1+sqrt(-3))/2
theta=1+2*w
M=Matrix([[Rational(str(x[0]))+Rational(str(x[1]))*w for x in row] for row in d['S_gram']])
assert M.shape==(8,8)
bar=lambda x: x.xreplace({sqrt(-3): -sqrt(-3)}) # not used for matrix check
# conjugate handles imaginary quadratic symbolic objects
assert all(simplify(M[i,j]+M[j,i].conjugate())==0 for i in range(8) for j in range(8))
h=theta*M
assert all(simplify(h[i,j]-h[j,i].conjugate())==0 for i in range(8) for j in range(8))
detS=simplify(M.det(method='domain-ge'))
deth=simplify(h.det(method='domain-ge'))
assert detS==3**9 and deth==3**13
norm_element=3**6*theta
norm=simplify(norm_element*norm_element.conjugate())
assert norm==deth
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(), 'field':'Q(w), w^2+w+1=0', 'theta':'1+2*w=sqrt(-3)', 'matrix_size':8,'skew_hermitian_S':True,'hermitian_h':True,'det_S':str(detS),'det_h':str(deth),'norm_witness':'3^6*(1+2*w)','norm_value':str(norm),'discriminant_class':'[1]'}
print(json.dumps(out,indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
