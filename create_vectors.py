#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
"""
import urllib
import urllib2
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
    params = urllib.urlencode({"text": text, 
                                "inlinks_threshold": 20})  
    f = urllib2.urlopen("http://labs:9905/do_process", params)
    f_response = f.read()
    # Load json from response
    concepts = json.loads(f_response)
    return concepts
    
all_entities = {}
cont_all_entities = 0

users = ['carmen.tsv', 'jgpachon07.tsv', 'Paulek6.tsv', 'rmaestrem.tsv', 'runnersvszombie.tsv']
user_entities = {}
cont_users = 0
for user in users:
    f = open("data/%s" % user, "r")
    text = flatten(f.read())
    #text = text[0:1000]
    user_entities[cont_users] = getConcepts(text)
    for key in user_entities[cont_users]:
        if key not in all_entities:
            all_entities[key] = cont_all_entities
            cont_all_entities += 1
    f.close()
    cont_users += 1
    

coocurrences = {}
for entitie in all_entities:
    users_coo = []
    for user in user_entities:
        if entitie in user_entities[user]:
            users_coo.append(user)
    if len(users_coo) > 1:
        print users_coo
        n = len(users_coo)
        i = 0
        while i < n:
            c = i + 1
            while c < n:
                comp = (users_coo[i],users_coo[c])
                if comp not in coocurrences:
                    coocurrences[comp] = 1
                else:
                    coocurrences[comp] += 1
                c += 1
            i += 1
            
print coocurrences
fd_out = file('/tmp/test.tsv', 'w')
fd_out.close()
    
    
    
    
    
    
    
    
    
    
