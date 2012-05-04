import json
from numpy import array
from scipy.cluster.vq import kmeans2, vq, whiten

f = open("data/vectors.tsv", "r")
user_vectors = json.load(f)
f.close()

# Kmeans is not a good choice. Results are very dependant on which point are chosen to
# initialize the cluster centroids.
print "Calculating centroids for vectors"
features = array(user_vectors.values())
centroids, labels = kmeans2(whiten(features), 2, minit="points")
print labels
users = user_vectors.keys()
for (counter, label) in enumerate(labels):
	print "%s:%s" % (users[counter], label)
print "--------------------------"
