from PCA import *

tissue_names,pca_out,color_map = PCAfy(Data, 3)

colortissue = [color_map[tissue] for tissue in parsed_names]

fig = pylab.figure()
ax = Axes3D(fig)

ax.scatter(*pca_out,c=colortissue)
plt.show()

