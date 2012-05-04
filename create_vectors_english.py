#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
"""
import urllib
import urllib2
import requests
import json

def flatten(line):
    """
    """
    line = line.lower()
    line = line.replace('á', 'a')
    line = line.replace('é', 'e')
    line = line.replace('í', 'i')
    line = line.replace('ó', 'o')
    line = line.replace('ú', 'u')
    line = line.replace('à', 'a')
    line = line.replace('è', 'e')
    line = line.replace('ì', 'i')
    line = line.replace('ò', 'o')
    line = line.replace('ù', 'u')
    line = line.replace('Á', 'a')
    line = line.replace('É', 'e')
    line = line.replace('Í', 'i')
    line = line.replace('Ó', 'o')
    line = line.replace('Ú', 'u')
    line = line.replace('!', '')
    line = line.replace('¡', '')
    line = line.replace('¿', '')
    line = line.replace('?', '')
    line = line.replace('.', '')
    line = line.replace(';', '')
    line = line.replace(',', '')
    line = line.replace('"', '')
    line = line.replace('\'', '')
    line = line.replace('\\', '')
    line = line.replace('/', '')
    line = line.replace('&', '')
    line = line.replace('%', '')
    line = line.replace('#', '')
    line = line.replace('|', '')
    line = line.replace('ñ', ' ')
    return line
    
def getConcepts(text):
    """
    """
    params = {"text":text, "inlinks_threshold":20}  
    response = requests.get("http://labs:9910/", params=params).content
    concepts = json.loads(response)['results'].keys()
    return concepts
    
all_concepts = []
user_concepts = {}
user_vectors = {}
threshold = 4

# users = ['greghoweguitar.tsv', 'chickenfootjoe.tsv', 'Richie_Kotzen.tsv', 'stevelukather.tsv', 'AlexSkolnick.tsv',
#          'mitsuhiko.tsv', 'zeeg.tsv', 'raymondh.tsv', 'chrismcdonough.tsv', 'kennethreitz.tsv']

users = ['greghoweguitar', 'chickenfootjoe', 'Richie_Kotzen', 'stevelukather', 'AlexSkolnick',
         'daveweiner', 'JBONAMASSA', 'tonymacalpine', 'peterframpton', 'vurnt22',
         'mitsuhiko', 'zeeg', 'raymondh', 'chrismcdonough', 'kennethreitz',
         'gsiegman', 'kantrn', 'alex_gaynor', 'pumpichank', 'jpellerin']


for user in users:
    print "Analyzing user %s" % user
    user_concepts[user] = {}
    f = open("data/%s.tsv" % user, "r")    
    for line in f:
        text = flatten(line)
        concepts = getConcepts(text)
        for concept in concepts:
            if not concept in all_concepts:
                all_concepts.append(concept)
            user_concepts[user][concept] = user_concepts[user].get(concept, 0) + 1
    # Delete concepts below a threshold
    for k, v in user_concepts[user].items():
        if v <= threshold:
            del user_concepts[user][k]
    print user_concepts[user]
    print ''
    
# Delete empty/users concepts from the index
all_concepts_filter = list(all_concepts)
for k in all_concepts:
    for user in users:
        if k in user_concepts[user].keys():
            try:
                print ' - Removing %s' % k
                all_concepts_filter.remove(k)
            except:
                pass
print len(all_concepts)
print len(all_concepts_filter)

for user in users:
    print "Creating vector for user %s" % user
    user_vectors['%s.tsv' % user] = []
    for concept in all_concepts_filter:
        user_vectors['%s.tsv' % user].append(user_concepts[user].get(concept, 0))

f_vectors= file('data/vectors.tsv', 'a')
vectors_json = json.dumps(user_vectors)
f_vectors.write(vectors_json)
f_vectors.close

