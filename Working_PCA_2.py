from normal_tissue_extract import transcript_df

import matplotlib.pyplot as plt
import numpy as np

from sklearn import decomposition
from sklearn import datasets

#print(transcript_df.shape)

Data=transcript_df[1:]
Data=np.log2(Data.fillna(0) + 1)
print("Data Set created")
Data = Data.transpose()
clustered_types = Data[Data.values > 176] 
Data = Data.transpose()

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
    


names = Data.index.values
parsed_names = []
for name in names:
   parsed_names.append(name.split('.')[0])

tissue_names,X,Y,color_map=PCAfy(Data)
clustered_types = Y[Y > 176]
colortissue=[color_map[tissue] for tissue in parsed_names]

## labeling for tissue types
fig, ax = plt.subplots()
last_name = 'empty'
X_index = 0
Y_index = 0
for name1 in names:
  if(name1!=last_name):
    print(last_name)
    last_name = name1
    ax.annotate(name1, xy=(X[X_index],Y[Y_index]), xytext=(-1,1), 
            textcoords='offset points', ha='center', va='bottom',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))
  
  X_index += 1
  Y_index += 1
## end labeling
plt.scatter(X,Y,color=colortissue)

plt.show()    

