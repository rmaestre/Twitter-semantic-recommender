import json

f = open("../data/vectors.tsv", "r")
user_vectors = json.load(f)
f.close()

fd_out = open("../data/vectors_flat.tsv", "w")
for user in user_vectors:
    vector_string = ''
    for item in user_vectors[user]:
        vector_string += "%s\t" % item
    print vector_string
    fd_out.write("%s\n" % vector_string)
fd_out.close()