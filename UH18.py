"""
Python script for webscraping the City of Hamilton Events Calendar Website
(https://www.hamilton.ca/attractions/events-calendar) for information related
to events happening today. Intended to be run on a schedule that scrapes the
site every day. Creates a CSV and JSON for intended use with Google Fusion and 
Firebase, respectively. Please forgive the lack of modularity :)
"""
# coding: utf-8

# Necessary imports

from lxml import html
import requests
import datetime as dt
import csv
import pandas as pd
import json


# Takes today and creates a string that matches the format of dates on the CoH website

today = dt.datetime.now()
month = today.strftime("%B")
d = int(today.strftime("%d"))
if d < 10:
    day = today.strftime("%d")[1:]
else:
    day = today.strftime("%d")
year = today.strftime("%Y")
dateMDY = month + " " + day + ", " + year


# Retrieves the source code from the site and creates a correct HTML document stored in htmlElem

link = "https://www.hamilton.ca/attractions/events-calendar"
response = requests.get(link)
sourceCode = response.content
htmlElem = html.document_fromstring(sourceCode)


# Repeats this 2 more times to grab 12 events' worth of information

for i in range(1,3):
    link = "https://www.hamilton.ca/attractions/events-calendar?page=" + str(i)
    response = requests.get(link)
    sourceCode = response.content
    htmlElem.append(html.document_fromstring(sourceCode))


# Makes all the href's absolute because CoH uses relative links and we want to provide absolute links to the user

htmlElem.make_links_absolute("https://www.hamilton.ca")


# Grabs all elements with the event-date class and stores in dateElems
# Does string manipulation to produce a single date (e.g. in the cases of December 8, 2018 to December 9, 2018)

dateElems = htmlElem.find_class("event-date")
convertedDateElems = []
for el in dateElems:
    convertedDateElems.append(el.text_content().lstrip().split(" t")[0].rstrip())


# Grabs all elements with the event-title class and stores in titleElems

titleElems = htmlElem.find_class("event-title")


# Grabs all elements with the event-location-address class and stores in locElems
# More string manipulation to get the format we want

locElems = htmlElem.find_class("event-location-address")
convertedLocElems = []
for el in locElems:
    e = str(el.text_content().lstrip())
    locLastChar = e.index("\n")
    convertedLocElems.append(e[0:locLastChar].rstrip())


# Grabs all elements with the event-read-more address class and stores in linkElems
# Need to navigate the HTML element tree to specifically grab the href's

linkElems = htmlElem.find_class("event-read-more")
convertedLinkElems = []
for el in linkElems:
    convertedLinkElems.append((el.getchildren()[0].getchildren()[0].attrib.get('href')))


# We should (generally) have 4 lists of 12 elements at this point
# We are only interested in the events with a start date of today so we grab the list indices that meet this criteria

matchedDateIndices = []
for i in range(len(dateElems)):
    if str(convertedDateElems[i]) == dateMDY:
        matchedDateIndices.append(i)


# Writes all the corresponding information to a CSV

with open("todays_events.csv", mode="w", newline ='') as csv_file:
    fieldNames = ["name","date","address","link"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

    writer.writeheader()
    for i in range(len(matchedDateIndices)):
        writer.writerow({"name": str(titleElems[i].text_content()),
                        "date": str(convertedDateElems[i]),
                        "address": str(convertedLocElems[i]),
                        "link": str(convertedLinkElems[i])})

# Takes our CSV that we just wrote and converts to JSON

data = []
with open("todays_events.csv", mode="r") as f:
    next(f, None)
    reader = csv.DictReader(f,fieldnames=["name","date","address","link"])
    json.dump([row for row in reader], open('todays_events.json', 'w+'))


# Credit to Shane Lynn for this geocoder
# Takes an address and returns lat/long, which we need for Google Fusion maps

"""
Python script for batch geocoding of addresses using the Google Geocoding API.
This script allows for massive lists of addresses to be geocoded for free by pausing when the 
geocoder hits the free rate limit set by Google (2500 per day).  If you have an API key for paid
geocoding from Google, set it in the API key section.
Addresses for geocoding can be specified in a list of strings "addresses". In this script, addresses
come from a csv file with a column "Address". Adjust the code to your own requirements as needed.
After every 500 successul geocode operations, a temporary file with results is recorded in case of 
script failure / loss of connection later.
Addresses and data are held in memory, so this script may need to be adjusted to process files line
by line if you are processing millions of entries.
Shane Lynn
5th November 2016
"""

import logging
import time

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

#------------------ CONFIGURATION -------------------------------

# Set your Google API key here. 
# Even if using the free 2500 queries a day, its worth getting an API key since the rate limit is 50 / second.
# With API_KEY = None, you will run into a 2 second delay every 10 requests or so.
# With a "Google Maps Geocoding API" key from https://console.developers.google.com/apis/, 
# the daily limit will be 2500, but at a much faster rate.
# Example: API_KEY = 'AIzaSyC9azed9tLdjpZNjg2_kVePWvMIBq154eA'
API_KEY = 'AIzaSyBcQjg1mBpDh4MLzJyrS8nvpfxezVi6TcU'
# Backoff time sets how many minutes to wait between google pings when your API limit is hit
BACKOFF_TIME = 30
# Set your output file name here.
output_filename = './GEOCODED.csv'
# Set your input file here
input_filename = "./todays_events.csv"
# Specify the column name in your input data that contains addresses here
address_column_name = "address"
# Return Full Google Results? If True, full JSON results from Google are included in output
RETURN_FULL_RESULTS = False

#------------------ DATA LOADING --------------------------------


# Read the data to a Pandas Dataframe
data = pd.read_csv(input_filename, encoding='utf8')

if address_column_name not in data.columns:
    raise ValueError("Missing Address column in input data")


# Form a list of addresses for geocoding:
# Make a big list of all of the addresses to be processed.
addresses = data[address_column_name].tolist()


#addresses = (data["STREET_NO_1"] + ' ' + data["STREET_NAME"] + ', ' + data["COMMUNITY"] + ', Ontario, Canada').tolist()

#------------------    FUNCTION DEFINITIONS ------------------------

def get_google_results(address, api_key=None, return_full_response=False):
    """
    Get geocode results from Google Maps Geocoding API.
    
    Note, that in the case of multiple google geocode reuslts, this function returns details of the FIRST result.
    
    @param address: String address as accurate as possible. For Example "18 Grafton Street, Dublin, Ireland"
    @param api_key: String API key if present from google. 
                    If supplied, requests will use your allowance from the Google API. If not, you
                    will be limited to the free usage of 2500 requests per day.
    @param return_full_response: Boolean to indicate if you'd like to return the full response from google. This
                    is useful if you'd like additional location details for storage or parsing later.
    
    """
    # Set up your Geocoding url
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)
        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    results = results.json()

    # if there's no results or an error, return empty results.
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
        }
        
    # Append some other details:    
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    if return_full_response is True:
        output['response'] = results
    
    return output

#------------------ PROCESSING LOOP -----------------------------

# Ensure, before we start, that the API key is ok/valid, and internet access is ok
test_result = get_google_results("London, England", API_KEY, RETURN_FULL_RESULTS)
if (test_result['status'] != 'OK') or (test_result['formatted_address'] != 'London, UK'):
    logger.warning("There was an error when testing the Google Geocoder.")
    raise ConnectionError('Problem with test results from Google Geocode - check your API key and internet connection.')

# Create a list to hold results
results = []
# Go through each address in turn
for address in addresses:
    # While the address geocoding is not finished:
    geocoded = False
    while geocoded is not True:
        # Geocode the address with google
        try:
            geocode_result = get_google_results(address, API_KEY, return_full_response=RETURN_FULL_RESULTS)
        except Exception as e:
            logger.exception(e)
            logger.error("Major error with {}".format(address))
            logger.error("Skipping!")
            geocoded = True

        # If we're over the API limit, backoff for a while and try again later.
#        if geocode_result['status'] == 'OVER_QUERY_LIMIT':
 #           logger.info("Hit Query Limit! Backing off for a bit.")
  #          time.sleep(BACKOFF_TIME * 60) # sleep for 30 minutes
   #         geocoded = False
    #    else:
            # If we're ok with API use, save the results
            # Note that the results might be empty / non-ok - log this
        if geocode_result['status'] == 'OK':
                #print("Address Geocoded")
                #logger.warning("Error geocoding {}: {}".format(address, geocode_result['status']))
                #logger.debug("Geocoded: {}: {}".format(address, geocode_result['status']))
                results.append(geocode_result)           
                geocoded = True

    # Print status every 100 addresses
    if len(results) % 100 == 0:
        logger.info("Completed {} of {} address".format(len(results), len(addresses)))
    
    # Every 500 addresses, save progress to file(in case of a failure so you have something!)
    if len(results) % 500 == 0:
        pd.DataFrame(results).to_csv("{}_bak".format(output_filename))

# All done
logger.info("Finished geocoding all addresses")
# Write the full results to csv using the pandas library.
pd.DataFrame(results).to_csv(output_filename, encoding='utf8')


# We read in the geocoded CSV and the original CSV to create a reformatted CSV that matches the format of
# our parsed CSV's from CoH's open datasets
# If you couldn't tell, we worked on parts separately and then ended up having to make changes to conform to each other :P

df = pd.read_csv("GEOCODED.csv")
lats = df.latitude.tolist()
longs = df.longitude.tolist()

df = pd.read_csv("todays_events.csv")
names = df.name.tolist()
links = df.link.tolist()


# Pretty much an identical CSV write to above (line 100)

with open("todays_events_reformatted.csv", mode="w", newline ='') as csv_file:
    fieldNames = ["","latitude","longitude","name","description"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

    writer.writeheader()
    for i in range(len(lats)):
        writer.writerow({"": i,
                        "latitude": lats[i],
                        "longitude": longs[i],
                        "name": names[i],
                        "description": links[i]})


# This was our attempt to try and get data uploaded to Firestore but 
# we ran into dependency issues with firebase-adminsdk
# We were actually able to upload data through Python but ran out of time! :o
"""
import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore

cred = credentials.Certificate('./file.txt')
firebase_admin.initialize_app(cred)

db = firestore.client()


# In[18]:

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

"""