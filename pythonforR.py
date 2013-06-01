#!/usr/bin/env python
# encoding: utf-8
"""
pythonforR.py
Created by Aaron Erlich on 2013-02-08.
"""

import sys
import os

#Chapter 1
#we cannot have a vector of strings in Python. 
PythonList1 = ['hello world', 'hello Seattle']
print PythonList1

item1 = 'hello world'
item2 = 'hello Seattle'

PythonList1_2 = [item1, item2]
print(PythonList1_2)

#It can be a list of lists
PythonList2 = [['hello world', 'hello Seattle'], 'hello Tokyo']
print PythonList1[0]
#the 1st 4 chars of elem 0
print PythonList1[0][0:4] 
#the 1st list and the 1st item in that list
print PythonList2[0][0] 
#1st char
print PythonList2[0][0][1]
#start at end 
print PythonList2[1][-1] 
#5th to end -> to end
print PythonList2[1][-5:]


#Create your own list with three sentences. Practice accessing different elements in your list

countryCodes = ['RUS', 'AFG', 'GER']
#semicolon starts the for loops
for i in countryCodes: 
  #indentation matters and you need a blank non-indented line after
  print i 

#we can also make Python more like R
for i,j in enumerate(countryCodes):
  print j + " is country number " + str(i)

#this will yield an error message
for i,j in enumerate(countryCodes):
  print j + " is country number " + i

##session 4
countryCodes = ['RUS', 'AFG', 'GER', 'USA', 'BRA', 'GER']
countryCodes.sort()
print countryCodes
countryCodes.remove('AFG') 
print countryCodes
#returns last and removes from list
countryCodes.pop() 
print countryCodes
#returns item in the second position and removes from list
countryCodes.pop(1) 
print countryCodes

##session 5
countryCodes = ['RUS', 'AFG', 'GER']
#the traditional for loop
for country in countryCodes: 
  country.lower()

print countryCodes #doesn't change list

#changes list
countryCodes2 =[ ]
for country in countryCodes: 
  countryCodes2.append(country.lower())
print countryCodes2

#list comprehension approaches
[country.lower() for country in countryCodes]
[country.lower() for country in countryCodes if country.startswith('G')]


##############
####Chapter 2
#############

oneCountry = "USA"
type(oneCountry)
oneCountry[0]

len(oneCountry)

#
oneCountry.lower()
oneCountry

oneCountry.split('S)
oneCountry

countryCodes = ['RUS', 'AFG', 'GER']
#semicolon starts the for loops
for country in countryCodes: 
  county.lower()

[country.lower() for country in countryCodes]
[country.lower() for country in countryCodes if country.startswith('G')]


"I don't wanna go to school, but I have to, but I don't want to".split("but")
#["I don't wanna go to school, ", ' I have to, ', " I don't want to"]

twoSchoolStatements = [
"I don't wanna go to school, but I have to, but I don't want to",
"I really wanna go to school, but I am sick, but I really don't have to"
]

lambda x: x.split("but"), twoSchoolStatements
def butSplit(x): return x.split("but")s

#functional programming - apply functions to sequences
#more powerful and faster than looping
mapWithDef = map(butSplit, twoSchoolStatements)
mapWithLambda = map(lambda x: x.split("but"), twoSchoolStatements)
pprint.pprint(mapWithDef)
pprint.pprint(mapWithLambda)

[x.split("but") for x in twoSchoolStatements]

#directories
#http://docs.python.org/2/library/os.html
os.chdir() #change directory *set working directory
os.getcwd() #get the current working directory
os.listdir() #return files in current working directory
os.mkdir()



##############
####Chapter 3
#############

KEN = {'DOI': 1963, 'pop': 40000000, "subnat": ['Kilifi', 'Nairobi']}
print(KEN['pop'])
print(KEN.keys())
print(KEN.values())

USA = {'DOI': 1776, 'pop': 300000000, "subnat": ['WA', 'ME']}
USA['flagname'] = "Stars and Strips"
USA['subnat'].append('OR')
print(USA['flagname'], USA['subnat'],)


countries = [USA, KEN] 
[2013-country['DOI'] for country in countries]


countryCodes = ('RUS', 'AFG', 'GER')
type(countryCodes)
countryCodes.append('GEO')
###Numbers
numbers = [1,45.3, 3.5]
for number in numbers:
	number in [1,3]
	print(type(number))

[number in [1,3] for number in numbers]
[number not in [1,3] for number in numbers]
[number for number in numbers if number in [1,3]]


oneNumber = 1
oneNumber += 1
oneNumber
oneNumber += 15.5
oneNUmber

SocialScience = "S"
SocialScience += "ocial"
SocialScience += " Science"
SocialScience

numbers = [1,45.3, 3.5]
for number in numbers:
	if number > 3 and number % .5 == 0:
		print(str(number) + " is greater than 3 and has a modulo of 0 when divided by .5")
	elif number > 45 or number/100 > .3:
		print("Big number " + str(number))
	else:
		print("Puny number " + str(number))
	
############
## Chapter 3
############

KEN = {'DOI': 1963, 'pop': 40000000, "subnat": ['Kilifi', 'Nairobi']}
print(KEN) #order not maintained
print(KEN['pop'])
print(KEN.keys())
print(KEN.values())

USA = {'DOI': 1776, 'pop': 300000000, "subnat": ['WA', 'ME']}
USA['flagname'] = "Stars and Strips" #add an element with the key "flagname"
USA['subnat'].append('OR')
print(USA['flagname'], USA['subnat'])

USA = {'DOI': 1776, 'pop': 300000000, "subnat": ['WA', 'ME']}
KEN = {'DOI': 1963, 'pop': 40000000, "subnat": ['Kilifi', 'Nairobi']}
countries = [USA, KEN] 
[2013-country['DOI'] for country in countries]

countryCodes = ('RUS', 'AFG', 'GER')
type(countryCodes)
countryCodes.append('GEO')
