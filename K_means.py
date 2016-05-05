from PCA import *

tissue_names,pca_out,color_map = PCAfy(Data,124)

kmeans = KMeans(n_clusters=32)

kmeans_out = kmeans.fit(pca_out.transpose())

centers = kmeans_out.cluster_centers_
labels  = kmeans_out.labels_

a = [set([]) for _ in np.unique(labels)]

for i in range(len(labels)):
    idx = labels[i]
    a[idx].add(parsed_names[i])

b = [str(s) for s in a]

print("\n".join(b))