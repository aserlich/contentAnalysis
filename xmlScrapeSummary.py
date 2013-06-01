"""
xmlScrape.py
#these are summaries of U.S. Bills
http://www.govtrack.us/data/us/103/bills/
Created by Aaron Erlich on 2013-01-23.
"""

import sys
import os
#import lxml.etree as xml
from bs4 import BeautifulSoup
import re
import pickle

path = #inserty your path
path = "/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/103HouseSummary"
os.chdir(path)
  
listing = [filename for filename in os.listdir(path) if re.search(r'(.*\.xml$)', filename) != None] #remove unwanted filenames only get .xml	
#get all the files
len(listing)
listing[0] #check for invisible files
print("There are {0} bills in this file" .format(len(listing))) #tell me how many bills there are
#reply = int(raw_input("Enter then number of bills you want to look at: "))
reply = 500
listing = listing[0:reply]

bills = [] #create a container to store all the bills
for infile in listing:
	input = open(infile, 'r') 
	bills.append(BeautifulSoup(input.read())) #append each read file into a bill and prepare for scraping
	print infile

# bills2 =[]
# for bill in bills:
# 	bills2.append(bill.get_text)
	
print(bills[2].prettify()) # lets look at the  XML structure of some bills
print(bills[4].prettify()) # lets look at the  XML structure of some bills

testSoup1 = bills[4]
testSoup2 = bills[2]

testSoup1.summary #only gives you the first one of these tags
testSoup2.summary

testSoup1.findAll("summary") #returns all of the tags
testSoup2.findAll("summary")	

type(testSoup2.findAll("summary")) #the object returned is a list

testSoup1.findAll("titles") #returns all of the tags
testSoup1.titles
testSoup1.titles.contents #we can look at all the children (nested documents within title)
#note that contents is not a tag (it's like a method)
#there is title -- so bills can have multiple titles

#You can also go the other way
testSoup1.title.parent #shows the parents

#this is nested
testSoup1.titles.title

testSoup1.findAll(["titles", "summary"]) #can search multiple elements
testSoup1.findAll(type="official") #can also search attributes

#you know that each bill only as one "actions" tag - so we use find to return the 1 actions tag in each bill but only the tag <action>
#then we find all the children that are text  and return that
actions = [bill.find('actions').findChildren('action') for bill in bills]
actions[0][1] #second action under first bill
#then we get the string that is part of action under actions for each of these bills 
texts = [item.text for action in actions for item in action]
texts[0]
actions[0][0]
texts[1]
actions[0][1]

allTags = []
tagsT = [[myTags.name for myTags in bill.findAll(re.compile(r".*?"))] for bill in bills] #returns a list with each element being all unique tags in the document
tagsT = [item for sublist in tagsT for item in sublist]
uniqueTags = list(set(tagsT))#get unique convert back
uniqueTags.sort()

print("These are the unique tags in your bill set: ")
print(uniqueTags)

#take the string in the bill summary and strip it
billSummaries = [bill.summary.string.strip() for bill in bills]

pattern = r'([1-2][0-9][0-9][0-9])' #look for all years mentioned in the 19th or 20th century
pattern2 = r'(^([1-9]|1[012])[- /.]([1-9]|[12][0-9]|3[01])[- /.](199[34])(--.*?\.))' #match and validate dates at the begining of a line in order to remove
#this patter parses the mont the data and the year so to get the text we need the fourth group
#we want to remove the date and the word Introduced, so we need the 5th element to get all of the text

re.split(pattern2, billSummaries[1])[6] #so the 6th element has our summary
#could also remove titles if I wanted to. 

billSummaries = [re.split(pattern2, summary)[6] for summary in billSummaries] 

# for j,summary in enumerate(summaries2):
# 	if len(summary) != 6:
# 		print(j)

years = [re.findall(pattern, summary) for summary in billSummaries] #maybe some bills are there differences between past and future oriented bills?

#two ways of storing files
#let's change the directory
#os.mkdir("/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/103HouseText")
os.chdir("/Volumes/Optibay-1TB/Python/scrapingCode/immigCongRec/")
os.chdir("/Volumes/Optibay-1TB/Python/scrapingCode/billSummaries/")

f = open('103HouseSummary.txt', 'w')
for summary in billSummaries:
	f.write("%s\r" % summary.encode("utf-8"))  #separate each bill with a \r feed to separate from the \ns we need to deal with later.


for i,summary in enumerate(billSummaries):
	fname = ''.join([listing[i].split('.',1)[0],'.txt'])
	f = open(fname,'w')
	f.write("%s" % summary.encode("utf-8"))  #	#separate each bill with a \r feed to separate from the \ns we need to deal with later.

#if you just storing for later use by a computer program use pickle
P = open('summary.pkl', 'wb')
pickle.dump(billSummaries, P)

#we need to strip white space more appropriately