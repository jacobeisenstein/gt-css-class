from __future__ import print_function

from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk
import sys
import os

tagger = StanfordNERTagger('stanford-ner-2017-06-09/classifiers/english.conll.4class.distsim.crf.ser.gz',
                           path_to_jar='stanford-ner-2017-06-09/stanford-ner.jar')

print(sys.argv[1])

with open(sys.argv[1]) as fin:
    current_entity = []
    entities = []
    for line in fin:
        for token,tag in tagger.tag(word_tokenize(line)):
            if tag != 'O':
                current_entity.append((token,tag))
            else:
                if current_entity != []:
                    entities.append(current_entity)
                    current_entity = []
    if current_entity != []:
        entities.append(current_entity)

with open(os.path.splitext(sys.argv[1])[0]+'.ne','w') as fout:
    for entity in entities:
        print('%s_%s'%(' '.join([tok for tok,tag in entity]),entity[0][1]),file=fout)
