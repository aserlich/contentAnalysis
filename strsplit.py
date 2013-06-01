"""
Created by Aaron Erlich in 2013.
"""

import re
import nltk

"I don't wanna go to school, but I have to, but I don't want to".split("but")

andorsent = "I either want to go the the movie or go to the park and swim"

#won't work you will need to use re
andorsent.split("and", "or") 

re.split(r'and|or', andorsent) # works

punctuation = r'(?:\.|:|;)'
punctuation2 = r'(?:\.|:|;)(?=\s{1,2}[A-Z]|\Z)' #?= is a lookahead assertion 

#will match punctuation only it is followed by a an \s chararcter and then a capital letter or the end of the string
puncSent = "However, the world is not great;\
 rather it is small and petty. There are three reasons\
-- at least according to me: 1)people 2)people 3)people."

re.split(punctuation, puncSent)

puncSent2 = "Fancy Grad Student holds a Ph.D. in Computer Science from MIT. He does machine learning."
puncSent3 = "Hi! I am Mr. John Doe and I hold a Ph.D. in Computer Science from MIT. I do machine learning."
puncSent4 = "Hi! I am Mr. John Doe, and I did Computer Science from MIT, and graduated with a Ph.D. I do machine learning."

re.split(r'\..*\.', puncSent2) #won't do that great

re.split(punctuation, puncSent2)
re.split(punctuation2, puncSent2) #better?
re.split(punctuation2, puncSent3)

#nltk offers a pre-trained english language punctuation tokenizer
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sent_detector.tokenize(puncSent3.strip())

#compare and contrast capture groups
emailRE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE) #compile for faster processing and tell to ignore case
emailRE2 = re.compile(r"(\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6})\b", re.IGNORECASE) #compile for faster processing and tell to ignore case and capture
emailRE3 = re.compile(r"\b([A-Z0-9._%+-]+)@([A-Z0-9.-]+\.[A-Z]{2,6})\b", re.IGNORECASE) #compile for faster processing and tell to ignore case and capture

someEmail = "csssgrads@u.washington.edu For more details please contact me \
polgrads@uw.edu Please forward this opportunity to appropriate interested parties \
megobrebs@yahoogroups.com Anyone found any coconut milk, syrup, powder locally?"

emailRE.split(someEmail)
emailRE2.split(someEmail)

emailRE3.findall(someEmail)
emailRE3.split(someEmail)

#Understand how regex is greedy
billTitle = '<H1>Senate Bill 32</H1>'
re.split(r'<(.*)>', billTitle)
re.split(r'<(.*?)>', billTitle)

#deal with blanks
someText = ['\n', "hello\n", "\nGood-bye", "\n"]

newList =[]
for i in someText:
  if len(i.strip()) >0: #if it's not blank
    newList.append(i.strip()) #append it with no leading or trailing blanks

# ##Figure out a regex for matching by-lines in Newspaper articles
# #Ny times format
# MAIDUGURI, Nigeria — ipsum lorum
# MAGESCQ, France — ipsum lorum
# KABUL, Afghanistan – ipsum lorum
# 
# ##Match & remove either but not any other text.  
# # &#8211; 
# # &#105;
# 
# #Try exercises 1-3
# http://regex.sketchengine.co.uk/
