from normal_tissue_extract import transcript_df

import matplotlib.pyplot as plt
import numpy as np

from sklearn import decomposition
from sklearn import datasets

#print(transcript_df.shape)

Data=transcript_df[1:]
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
    
    pca = decomposition.PCA(n_components=2)
    pca.fit(exp_lvl)
    df_PCA = pca.transform(exp_lvl)
    
    return(tissue_names,df_PCA.transpose()[0],df_PCA.transpose()[1],color_map)
    




tissue_names,X,Y,color_map=PCAfy(Data)

colortissue=[color_map[tissue] for tissue in tissue_names]

plt.scatter(X,Y,color=colortissue)

    
