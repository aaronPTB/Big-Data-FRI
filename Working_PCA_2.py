from PCA import *


tissue_names,XY_coords,color_map=PCAfy(Data,2)
X = XY_coords[0]
Y = XY_coords[1]
colortissue=[color_map[tissue] for tissue in parsed_names]
print(color_map)
print(tissue_names)
print(len(X))
print(len(Y))
print(len(colortissue))
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

