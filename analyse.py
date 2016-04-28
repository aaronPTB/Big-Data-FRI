import numpy  as np
import pandas as pd

gene_data = pd.read_csv("rna_tissue.csv",header=0)
expr_lvl  = gene_data.transpose().ix[5]

expression_types = {"High":3,"Medium":2,"Low":1,"Not detected":0}

for level in expression_types.keys():
	expr_lvl[expr_lvl==level] = expression_types[level]

print expr_lvl