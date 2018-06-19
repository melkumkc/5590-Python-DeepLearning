import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # importing the clustering algorithm



arr = np.array ([[2,70],[2.1,98],[1.5,45],[1.75,78],[1.78,90],[1.8,90],[1.6,60],[2.1,110],[1.8,80], [1.6,65],[1.92,105],[1.6,62],[1.75,76], [1.5, 44], [1.8,89],[1.5,95],[1.7,88]]) # sample data of (Height, weight)
kmeans = KMeans (n_clusters= 3) # number of clusters to be used
kmeans.fit(arr)
centroids = kmeans.cluster_centers_ # calcualting the centroids

print (centroids) # displaying the centroid

print ("Cluster center 1: height = {} & weight = {}; Cluster center 2: height = {} & weight = {}; Cluster center 3: height = {} & weight = {}"
       .format(centroids[1][0],centroids[1][1],centroids[0][0],centroids[0][1],centroids[2][0],centroids[2][1]))
print ("Remark Height is given in meters and weight is in Kg")


plt.figure (figsize=(15,15), dpi=80) # setting fig size
plt.scatter(arr[:,0], arr[:,1]) # plotting the raw data
plt.hlines (centroids, xmin= 0, xmax=3) # plotting the cluster
for i in range (3):
    plt.scatter(centroids[i][0],centroids[i][1], marker = "x", linewidths=10)
plt.show()
