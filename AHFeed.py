# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:55:50 2019

@author: lukep
"""

import json
import re
import urllib.request

client_id = 'a9b778f1a514493e81662fbdc84ac8d8' 
client_secret = 'Vuh3MxV2vaynh60mCg2GH05lcIV3GNXe' 
authorize_uri = 'https://{region}.battle.net/oauth/authorize' 
token_uri = 'https://{region}.battle.net/oauth/token'

# Load up the authorisation point and request a token with clientid and client credientials as args
requestURL = 'https://eu.battle.net/oauth/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
theResponse = urllib.request.urlopen(requestURL)
#print("Printing the request token response...")
#print(theResponse.read())
bytesValues = urllib.request.urlopen(requestURL).read()
bytesToJSON = bytesValues.decode('utf8').replace("'", '"')
data = json.loads(bytesToJSON)
accessToken = data.get("access_token")

# Use the accessToken we retrieved to make a test AH API call
# Create the call to the auction house API
server = 'bloodhoof'
locale = "en_EU"
ahAPIBase = 'https://eu.api.blizzard.com/wow/auction/data/' + server
queryParameters = '?locale=' + locale + '&jsonp=true&access_token=' + accessToken
requestURL = ahAPIBase + queryParameters

# Making the request
actualRequest = urllib.request.urlopen(requestURL)
#print("Printing the AH API response...")
#print(actualRequest.read())
# Get the location of the JSON which contains the AH data
bytesValues = urllib.request.urlopen(requestURL).read()
bytesToJSON = bytesValues.decode('utf8').replace("'", '"')
bytesToJSON = "[" + bytesToJSON + "]"
#print(bytesToJSON)
# Extract the auction data location between two delimiters and concatenate back together.
result = re.search('http://(.*).json', bytesToJSON)
fileLoc = 'http://' + result.group(1) + '.json'

# Get the actual AH response
dataResponse = urllib.request.urlopen(fileLoc).read()
#print(dataResponse.read())
auctionData = json.loads(urllib.request.urlopen(fileLoc).read())

#def dataParse(data):
#    
#    if type(data) is dict:
#        print('/n')
#        print('Found new dictionary!')
#        print('The keys are: ')
#        print(data.keys())
#        print('The values are')
#        print(data.values())
#        dataParse(data.values())
#    
#    # If the data type if a list, iterate over each element within in 
#    if type(data) is list: 
#        print('\n')
#        print('Found new list!')
#        print(data)
#        # Send list items to dataParse if they are dicts or lists
#        for element in data:
#            if type(element) is list or type(element) is dict:
#                dataParse(element)        
    

def dataParse(data):
    
    print(data)
    
    if type(data) is dict:
        print('/n')
        print('Found new dictionary')
        dataParse(data.values())
    
    # If the data type if a list, iterate over each element within in 
    if type(data) is list: 
        print('\n')
        print('Found new list!')
        # Send list items to dataParse if they are dicts or lists
        for element in data:
            if type(element) is list or type(element) is dict:
                dataParse(element)

for k, v in auctionData.items():
    print(k)
    print(v)