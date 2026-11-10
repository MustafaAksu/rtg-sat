IN=/home/claude/g34/blind_in/HCG_H4_BLIND_CHALLENGE_v0_1/BLIND_INPUT
for c in NEW01 NEW02 NEW03 NEW04; do for t in 0 1 2; do
  python3 h4sel/holdout_post/cert_dump_tree.py $IN/${c}_roots.json $IN/${c}_trees.json h4sel/holdout_post/cert_${c}_${t}.json $t >/dev/null
  python3 h4sel/theorem/check_edgeform_identity.py h4sel/holdout_post/cert_${c}_${t}.json | tr '\n' ' '; echo
done; done
