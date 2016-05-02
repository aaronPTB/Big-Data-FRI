import numpy as np
import pandas as pd
from pandas import DataFrame

transcript_df = DataFrame.from_csv('transcript_rna_tissue.tsv', sep='\t', header=0).transpose()

