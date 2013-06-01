"""
tokenizeSummary.py
Created by Aaron Erlich on 2013-02-01.
"""

import sys
import os
import pickle
import nltk
import numpy
import scipy
import matplotlib
import textmining
import pandas
import string

path = #insert your path
os.chdir(path)
#os.chdir('/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/')
pkl_file = open('summary.pkl', 'rb')
billSummaries = pickle.load(pkl_file)

#There are lots of different ways to read in and deal with our texts and interact with the NLTK package
#We will cover several different ways

#normalize text
#lemmatize
#stem

#how do i convert to an nltk text?
#you can load the built in machine learned sentence tokenizer for English
sent_tokenize = nltk.data.load('tokenizers/punkt/english.pickle')

#####TOKENIZE###############
#tokenize by sentence - I will maintain the document structure because maybe we want it for something
bill_sents =[]
for bill in billSummaries:
	bill_sents.append(sent_tokenize.tokenize(bill))

bill_sents[1][-1]

#tokenize by word
from nltk.tokenize import word_tokenize #there are different word tokenizers -- this one keeps the period at the end of the sentence with the word
from nltk.tokenize import wordpunct_tokenize  #there are different word tokenizers -- this one doesn't
#see http://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
bill_words = [[word_tokenize(sent) for sent in bill] for bill in bill_sents]
bill_words[1][-1][:] # all words in last sentence of second bill


#LEMMATIZE/NORMALIZE##########
bill_words2 = [[[word.lower() for word in sent] for sent in bill] for bill in bill_words] #make it lowercase and keep structure
bill_words2[1][-1][:] #now lower case

from nltk.corpus import stopwords
print(stopwords.words('english')) # look at the stopwords
#we now remove all words that are shorter than 4 characters and which are not stopwords
bill_words3 = [[filter(lambda word: word not in stopwords.words('english') and len(word) >3, word) for word in bill] for bill in bill_words2]
bill_words3[1][-1][:] #now lower case and short words removed

#now we stem
Pstemmer = nltk.stem.PorterStemmer()
bill_words4 = [[[Pstemmer.stem(word) for word in sent] for sent in bill] for bill in bill_words3]
bill_words4[1]
bill_words4[1][-1][:]

#we have done this to maintain the structure -- but let's say we just want to look at all the bills together
allBills= ' '.join(billSummaries)
type(allBills)
allWords = wordpunct_tokenize(allBills)
allWords = [word.lower() for word in allWords]

#we can recognize parts of speech, proper names and man other things here if we wanted
allWords2 = filter(lambda word: word not in stopwords.words('english') and len(word) >3, allWords)
allWords3 =  [Pstemmer.stem(word) for word in allWords2]
sorted(set(allWords3))

billsVocab = sorted(set(allWords3))
len(sorted(set(allWords3))) #unique non-punctuation or abbreviation

len(allWords)
allWords3.count("withheld")
allWords3.count("withdrawn")
allWords3.count("worthless")
allWords3.count("solut")

from __future__ import division
len(allWords3)/len(set(allWords3)) #lexical diversity -- can compare

fd = nltk.FreqDist(allWords3) #create an nltk frequency distribution from our list
# a frequency distribtuion is similary to but of a special dictionary with keys as the words and counts as the values
type(fd)
fd.keys() #shows you all the words
fd.values() #shows you all the values
fd.plot(50, cumulative=True) #show the 50 most common words on a graph
fd.plot(50, cumulative=False) 
fd.tabulate(50) # I really should have removed the word title but since it's in all bills it's not really going to matter
fd.tabulate(10,20)
fd.hapaxes() #words (or what linguists call samples) that only occur once
fd.Nr(20) #number of words occurring exactly 20 times
fd.Nr(1)
fd.N() == len(allWords3)#same as length for list of all words
fd.B() #same as len(unique vocab)
fd.samples() #returns unique vocab
fd["worthless"] #returns the countt
fd.max()

counter = 0
#lets look at 200 of the most popular items and there counts
for i in range(20): #loop 10 times
	fd.tabulate(counter, counter+10)
	raw_input("Hit Enter")
	counter += 10
	
#############################################################
#or we might want to create an nltk corpus
#############################################################
from nltk.corpus import PlaintextCorpusReader
#http://nltk.googlecode.com/svn/trunk/doc/api/nltk.corpus.reader.plaintext.PlaintextCorpusReader-class.html
summaries_root = "/Volumes/Optibay-1TB/Python/scrapingCode/billSummaries/" #say where your text file is
billsCorpora = PlaintextCorpusReader(summaries_root, r'h[1-9].*\.txt') #read it into the corpora
dir(billsCorpora) # see what methods can be used on the corpora

rawBills = billsCorpora.raw() #all the rawtext
billsCorpora.fileids() #show the files in the corpora
billsCorpora.fileids()[0] #show the first fileid

billsCorpora.raw()[1:30]
len(billsCorpora.fileids()) #show how many files
len(billsCorpora.sents())

#billsCorpora.fileids('h1.txt')
billsCorpora.raw() #the whole corpora
billsCorpora.sents() #all of the sentences in the corpora
billsCorpora.sents()[1]
billsCorpora.words() #all of the words in all of the corpora
billsCorpora.words('h1.txt')  #all of the words in one corposa
twoBillsWords = billsCorpora.words(['h1.txt', 'h1447.txt'])
twoBillsWords[500:525] #not that puncutation is included and bills have not been lemmatized
billWords = billsCorpora.words()

#taken from NLTK blog -- and then modified. Create a frequency distribution from a corpus
def count_stems(corpus):
	stemmer = nltk.stem.PorterStemmer()
	stopset = set(nltk.corpus.stopwords.words('english')) | set(string.punctuation)
	fd = nltk.probability.FreqDist()
	for word in corpus.words():
		w = word.lower()
		if w in stopset: continue
		fd.inc(stemmer.stem(w))	
	return fd
	

#a very simple function to get dictionary counts
def make_count(corpus, wordSet):
	billCounts =[]
	for fileName in corpus.fileids():
		#print(fileName)
		counter =0
		docWords = corpus.words(fileName)
		for word in docWords:
			#print(word)
			w = word.lower()
			if w in wordSet: 
				# i could also use in the fd.inc approach here and it's proabably better-just showing another option. 
				print(w + " is in " + fileName)  
				counter+= 1
	 	billCounts.append(counter)
	return billCounts

from nltk.corpus.reader import WordListCorpusReader
path = "/Volumes/Optibay-1TB/Dropbox/Content_Wilker/Gonzalez_Project/Gonzalez_Keywords"
reader = WordListCorpusReader(path, ['crime.txt']) #make an nltk word list

crime = reader.words()
crime = [word.lower().strip() for word in crime]	

crimeSet = set([w.lower() for w in crime])
crimeCount = make_count(billsCorpora, crimeSet)

fd = count_stems(billsCorpora)

counter = 0
#lets look at 200 of the most popular items and there counts

#you could use the csv writer methods or this which is kind of hacky
mywordlist = numpy.asarray([billsCorpora.fileids(), crimeCount])
mywordlist[0][1] #name
mywordlist[1][1] #count

wordlistdf = pandas.DataFrame(mywordlist.transpose(), columns=["fileName", "count"])
wordlistdf['fileName'] #access a column
wordlistdf.fileName[5] #another way to access a column - now the fifth element
wordlistdf[:5] $access the rows with slicing

#change to your director
wordlistdf.to_csv('/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/crimeCounts.csv', index=True, header=True, sep=',')

a = numpy.asarray([fd.keys(), fd.values()])
df = pandas.DataFrame(a.transpose(), columns=["word", "count"])
df.to_csv('/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/billFrequencies.csv', index=True, header=True, sep=',')

#lots of ways to make a term document matrix -- let's choose the simplest
#often there are cutoffs for how often the word has to appear
bills5 = [[' '.join(sentence) for sentence in bill] for bill in bill_words4]

#http://text-processing.com/demo/tag/

tdm = textmining.TermDocumentMatrix()
for bill in bills5:
	tdm.add_doc(bill[0])

tdm.write_csv('CongMatrix.csv', cutoff=1)

#see Andrew Hall's page at Harvard for a slightly more complex implementaiton
# http://www.andrewbenjaminhall.com/wp-content/uploads/2011/12/Gen_TDM.txt