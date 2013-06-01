#!/usr/bin/env python
# encoding: utf-8
"""
wordNet.py
Created by Aaron Erlich on 2013-02-13.
"""

import sys
import os
import nltk
from nltk.corpus.reader import WordListCorpusReader

path = #insert your path
#path = "/Volumes/Optibay-1TB/Dropbox/Content_Wilker/Gonzalez_Project/Gonzalez_Keywords"
reader = WordListCorpusReader(path, ['crime.txt']) #make an nltk word list

crime = reader.words()
crime = [word.lower().strip() for word in crime]

from nltk.corpus import wordnet

#lemmas are the distinct meaning of the a word and all of each meaning's possible morphologies
#we see that lots of the student's words have both noun and verb meanings. Which does he care about?
#these words are polysemous -- they have similar but different meanings
for word in crime:
	print word
	print wordnet.synsets(word)
	print "\n"
	raw_input("Hit Enter")
	
[synset.lemma_names for synset in wordnet.synsets("stealing")]
	
#so we are looking for all the words under certain definitions of the word with the same morphological meaning
#That is, we are looking for synonymous lemmas. These are known as a synset
def examine_defs(word):
	for i, synset in enumerate(wordnet.synsets(word)):
		print word
		print('def %s : '  % (i)) + synset.definition 
		print synset.lemmas
		print synset.lemma_names
	print "\n"

examine_defs("stealing")
#for stealing we really only want def0 and def2

#superodinate and subordinate concepts
#words up and down the tree
wordnet.synsets("stealing")[0].hypernyms()
wordnet.synsets("stealing")[2].hypernyms()
wordnet.synsets("stealing")[0].hyponyms()
wordnet.synsets("stealing")[2].hyponyms()

#we can do network analysis on words and see where they are in the tree
wordnet.synset('larceny.n.01').min_depth() #n.01 is the legal definition and 10 steps from the top of the tree
larceny = wordnet.synset('larceny.n.01')
larcenyPaths = 	larceny.hypernym_paths()
len(larcenyPaths) #just one way up the tree #larceny is an entity whatever that is

map(examine_defs, crime)

#you can use the app -make sure to close down properly
nltk.app.wordnet()

#http://www.globalwordnet.org/
nltk.help.upenn_tagset('RB') # what do the tags mean

#one strategy is to print this all out and then delete stuff you don't need

#We do part of speech tagging at the level of sentence

sent1 = "This criminal element keeps on crossing the border in San Diego."
sent2 = "The person who come here is a criminal from Guatemala."

sent1word = nltk.word_tokenize(sent1)
sent2word = nltk.word_tokenize(sent2)
taggedsent = nltk.pos_tag(sent1word) #off the shelf tagger

#Chunk named entitites
#https://nltk.googlecode.com/svn/trunk/doc/api/nltk.chunk-module.html
nltk.ne_chunk(taggedsent)
nltk.pos_tag(sent2word)
nltk.help.upenn_tagset('JJ')

#from NLTK -- maybe you sjust need certain parts of speech
#see http://nltk.googlecode.com/svn/trunk/doc/book/ch05.html
patterns = [
 (r'.*ing$', 'VBG'),               # gerunds
 (r'.*ed$', 'VBD'),                # simple past
 (r'.*es$', 'VBZ'),                # 3rd singular present
 (r'.*ould$', 'MD'),               # modals
 (r'.*\'s$', 'NN$'),               # possessive nouns
 (r'.*s$', 'NNS'),                 # plural nouns
 (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
 (r'.*', 'NN')                     # nouns (default)]
 ]

regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(sent1word)
regexp_tagger.tag(sent2word)

#You can train your own TAGGER! -- What you most likely have to do
#Come to me if you need hep with this
#That's because you need probabilistic tagging based on context of documents
#Involves tagging all of the words in a test set of data an then training it -- same supervised learning concept

