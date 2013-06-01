#!/usr/bin/env python
# encoding: utf-8
"""
requests.py

Created by Aaron Erlich on 2013-02-06.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

http://congress.api.sunlightfoundation.com/hearings?

#store search params in a dictionary
query_params = { 
				'committee_id': 'HSIF',
		   		'congress': 'upper',
		   		'subject': 'Labor and Employment',
				'apikey': apikey,
		 		'term' : '2011-2012'}

import sys
import os
import requests #new library
import pprint

#need to look at the sunlight foundation's Open States website and look at what parameters they set
#Need to get your own API key from the Sunlight Foundation: It's free, so register
#in this examples we will look at Senate Bills from the Washington State Legislature about Labor and Employment (see subject) in ther 2011-2012 term

apikey = '55c451b40fc94e0ebf7502f8aa42faf4'

#store search params in a dictionary
query_params = { 
				'state': 'wa',
		   		'chamber': 'upper',
		   		'subject': 'Labor and Employment',
				'apikey': apikey,
		 		'term' : '2011-2012'}

query_params['chamber']
		
call_form = 'http://openstates.org/api/v1/bills/?' #default returns json http://json.org/
#i googled around forever only to see that they don't support xml
	
#instead of filling out complicated parameters we just do it this way
response = requests.get(call_form, params=query_params)
response.url #see the API call we made

type(response.text[0]) #not so useful
response.json()[0] #what does this look like?

responseJson = response.json() #get back a list of dictionaries
responseJson[0]['bill_id']

allLabor = [bill['bill_id'] for bill in responseJson]
allSession = [bill['session'] for bill in responseJson]
alltitle = [bill['title'] for bill in responseJson]

#This endpoint exists to get all information about a bill given its state/session/chamber and bill id.
#http://openstates.org/api/v1/bills/{STATE-ABBREV}/{SESSION}/{CHAMBER}/{BILL-ID}?apikey={YOUR_API_KEY}

