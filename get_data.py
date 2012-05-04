import urllib
import urllib2
import json
from statlib import stats
import math as m
import time


def get_corpus(user_screenname):
    corpus = []
    f = urllib2.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?count=1000&screen_name=%s&include_entities=true" % user_screenname)
    f_response = f.read()
    twetts = json.loads(f_response)
    for twett in twetts:
        if 'text' in twett.keys():
            corpus.append(twett['text'])
    return corpus
    

#user = 'rmaestrem'
#user = 'jgpachon07'
#user = 'CARmeleOLMOS'
#user = '@Paulek6'
# user = 'runnersvszombie'

# users = ['greghoweguitar', 'chickenfootjoe', 'Richie_Kotzen', 'stevelukather', 'AlexSkolnick',
#          'mitsuhiko', 'zeeg', 'raymondh', 'chrismcdonough', 'kennethreitz']

users = ['daveweiner', 'JBONAMASSA', 'tonymacalpine', 'peterframpton', 'vurnt22',
         'gsiegman', 'kantrn', 'alex_gaynor', 'pumpichank', 'jpellerin']

for user in users:
    print "Retrieving tweets for %s" % user
    f_corpus= file('data/%s.tsv' % user , 'a')
    corpus = get_corpus(user) 
    for twett in corpus:
        f_corpus.write('%s\n' % (twett.encode('utf-8')))
    f_corpus.close


