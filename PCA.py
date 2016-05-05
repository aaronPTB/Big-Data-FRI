from Normal_tissue_extract import transcript_df

import matplotlib.pyplot as plt
import random
import numpy as np
import pylab
import re

from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn.cluster import KMeans
from scipy.spatial   import Voronoi, voronoi_plot_2d
#print(transcript_df.shape)

Data=transcript_df[1:]
Data=np.log2(Data.fillna(0) + 1)
print("Data Set created")



#exp_lvl=exp_lvl.transpose()
import random

#plt.plot(exp_lvl.mean().values)
def PCAfy(exp_lvl):
    
    names=exp_lvl.index.values
    tissue_names=set([])
    for name in names:
        tissue_names.add(name.split('.')[0])
    
    
    color_map = {}
    for name in tissue_names:
        color_map[name] = (random.random(), random.random(), random.random())        
    
    exp_lvl=exp_lvl.fillna(0)
    
    pca = decomposition.PCA(n_components=124)
    pca.fit(exp_lvl)
    df_PCA = pca.transform(exp_lvl)
    
    return(tissue_names,df_PCA.transpose(),color_map)
    


names = Data.index.values
parsed_names = []
for name in names:
   parsed_names.append(name.split('.')[0])
