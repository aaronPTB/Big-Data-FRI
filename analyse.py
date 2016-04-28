import numpy  as np
import pandas as pd

gene_data = pd.read_csv("transcript_rna_tissue.tsv",delimiter="\t",header=0,index_col=0)

print gene_data
