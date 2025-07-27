#In this program, we cluster companies' D&A systems based on their 
# people, technology, process scores.
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[0.06099, 0.15847,0.0415], [0.06561, 0.18730,0.04178],\
[0.05400,0.16964,0.4922], [0.12262, 0.15938,0.05888], \
[0.15989, 0.24314,0.05878], [0.18366, 0.20412,0.07166], \
[0.20847,0.27025,0.08089],[0.19912,0.41569,0.09000],\
    [0.21254,0.44223,0.07839]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
kmeans.predict([[0.06099, 0.15847,0.0415], \
    [0.06561, 0.18730,0.04178],[0.05400,0.16964,0.4922]])