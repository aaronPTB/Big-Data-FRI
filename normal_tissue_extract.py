import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib as mpl
import random
from sets import Set
transcript_df = DataFrame.from_csv('transcript_rna_tissue.tsv', sep='\t', header=0)
transcript_df = transcript_df.rename(columns=lambda x: x.split('.')[0])
transcript_df = transcript_df.transpose()

df_names = transcript_df.index.values
tissue_names = Set([])
for name in df_names:
  tissue_names.add(name.split('.')[0])
color_map = {}
for name in tissue_names:
  color_map[name] = (random.random(), random.random(), random.random())


