import json
from sklearn.linear_model import SGDClassifier

# Load the user vectors
f = open("data/vectors.tsv", "r")
user_vectors = json.load(f)
f.close()

# Build the training set
X = [user_vectors['Richie_Kotzen.tsv'], user_vectors['AlexSkolnick.tsv'], user_vectors['greghoweguitar.tsv'],
	 user_vectors['JBONAMASSA.tsv'], user_vectors['tonymacalpine.tsv'], user_vectors['peterframpton.tsv'], user_vectors['vurnt22.tsv'],
	 user_vectors['mitsuhiko.tsv'], user_vectors['chrismcdonough.tsv'], user_vectors['zeeg.tsv'],
	 user_vectors['kantrn.tsv'], user_vectors['alex_gaynor.tsv'], user_vectors['pumpichank.tsv'], user_vectors['jpellerin.tsv']]
y = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# Train the classifier
clf = SGDClassifier(loss="hinge")
clf.fit(X, y)

# Build the test set
Xtest = [user_vectors['stevelukather.tsv'], user_vectors['chickenfootjoe.tsv'], user_vectors['daveweiner.tsv'],
		 user_vectors['raymondh.tsv'], user_vectors['kennethreitz.tsv'], user_vectors['gsiegman.tsv']]
# # Apply PCA for dimensionality reduction
# Xtest_r = pca.fit(X).transform(Xtest)

# Predict

print clf.predict(Xtest)