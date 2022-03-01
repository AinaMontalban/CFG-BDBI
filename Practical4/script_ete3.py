from ete3 import PhyloTree
from ete3 import Tree

import os
import re
# Loads an example tree

nw = """
(XP_003683083.1_hypothetical_protein_TDEL_0H00130_Torulaspora_del:0.7797,
((XP_025343676.1_hypothetical_protein_CXQ85_002454_Candida_haemulo:0.04887,
XP_028889402.1_uncharacterized_protein_CJI97_002130_Candida_auri:0.06341)
1:0.3071,
(((((XP_001482281.1_hypothetical_protein_PGUG_05301_Meyerozyma_guilli:0.2415,
(XP_015467038.1_hypothetical_protein_AC631_03306_Debaryomyces_fab:0.2264,
XP_457922.1_DEHA2C05390p_Debaryomyces_hansenii_CBS767:0.08596)1:0.2151)
0.38:0.0392,
((XP_001386550.1_Siderophore_Iron_Transport_partial_Scheffersomyce:0.1785,
XP_020065007.1_MFS_general_substrate_transporter_Suhomyces_tanza:0.1806)
0.029:0.0482,
XP_003866135.1_hypothetical_protein_CORT_0A03060_Candida_orthops:0.2507)
0.97:0.1048)0.91:0.06825,
XP_020076543.1_MFS_general_substrate_transporter_Hyphopichia_bur:0.4185)
0.25:0.0319,
(XP_018710827.1_MFS_general_substrate_transporter_Metschnikowia_b:0.2892,
XP_002618211.1_hypothetical_protein_CLUG_01670_Clavispora_lusita:0.1372)
0.99:0.08972)0.85:0.05838,
(((XP_025336135.1_uncharacterized_protein_CXQ87_003032_Candida_duob:0.03204,
XP_024712458.1_hypothetical_protein_C7M61_004162_Candida_pseudoh:0.02587)
1:0.06701,
XP_028889567.1_uncharacterized_protein_CJI97_002301_Candida_auri:0.08708)
0.28:0.04712,
XP_025343816.1_hypothetical_protein_CXQ85_002600_Candida_haemulo:0.1227)1:0.1805)
0.96:0.0916):0.04893);
"""



t = PhyloTree(nw)
print(t)
		# Get the tree's root
root = t.get_tree_root()
print(root)

# To obtain all the evolutionary events involving a given leaf node we
# use get_my_evol_events method
matches = t.search_nodes(name="XP_028889402.1_uncharacterized_protein_CJI97_002130_Candida_auri")
candauris_seq = matches[0]
# Obtains its evolutionary events
candev = candauris_seq.get_my_evol_events()
print "Events detected that involve CJI97_002301_Candida_auri"
for ev in candev:
    if ev.etype == "S":
        print '   ORTHOLOGY RELATIONSHIP:', ','.join(ev.in_seqs), "<====>", ','.join(ev.out_seqs)
    elif ev.etype == "D":
        print '   PARALOGY RELATIONSHIP:', ','.join(ev.in_seqs), "<====>", ','.join(ev.out_seqs)
events = t.get_descendant_evol_events()
t.show()
	

