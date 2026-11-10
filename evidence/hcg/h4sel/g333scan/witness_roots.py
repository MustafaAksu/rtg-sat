import json
exec(open('/home/claude/g34/h4sel/toybraid/toy_braid_bfs.py').read().split("print('start best pair-tree rank:'")[0])
t=(0,0,1,2,5,6)
json.dump({'final_roots':[[ [str(x[0]),str(x[1])] for x in rep[l]] for l in t]},open('g333_witness_roots.json','w'))
print('witness roots:',[rep[l] for l in t])
