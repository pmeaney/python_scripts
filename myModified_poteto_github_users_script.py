'''
I was looking around for a way to process a batch of nginx access logs to extract dates and IP addresses.
I found this script from 2012 -- https://gist.github.com/poteto/2814239
The original version is python 2, below, I made some modifications, trying to make it python3 comaptible.
But I couldn't get working very quickly, so I decided to start from scratch.
'''


#!/usr/bin/python
# ip_lookup.py by poteto
#
# Batch processes many IP addresses, and traces their geolocation.
# The script outputs a .txt file which is then renamed to .csv, and is usable in Excel
#
# Use:
#   1. Save your user email and IP addresses in a .csv file
#        -  Each email and IP should be in its own column in Excel (or separated by commas)
#        -  Enter the name of your .csv file:
#
batch_filename = "ipaddresses.csv"
#
#   2. Go to http://www.ipinfodb.com/ip_location_api.php and get your own API key
#   3. Update the config with your API key:
#
key = "fa3aa04806975ebf92b42c9a7c0fe06f20bb40ec67c18de2f85b3de3fd157df8"
#
#   4. Run the script:
#   $ python ip_lookup.py


import xml.etree.ElementTree as ET
import urllib.request
import csv
import os
import time

# Process batch csv into list 'current_batch'
def get_batch(batch_filename):
    "Creates list containing all the email and IP addresses from your batch file"
    batch = csv.reader(open(batch_filename, 'r'), delimiter=',')
    return [[ip_addr] for ip_addr in batch]


def batch_process(batch):
    "Runs your batch file through the IPInfoDB API"
    try:
        i = 0
        output = open('output.txt', 'a')
        print(batch)
        for ip_addr in batch:
            print(ip_addr)
            response = urllib.request.urlopen(url + "&ip=" + str(ip_addr)).read()
            print(response)
            tree = ET.fromstring(response)
            output.write(str(email) + ",")
            for child in tree:
                if child.tag == 'ipAddress':
                    output.write(str(child.text) + ",")
                if child.tag == 'countryCode':
                    output.write(str(child.text) + ",")
                if child.tag == 'timeZone':
                    output.write(str(child.text) + "\n")
            i += 1
            print("\n" + str(i) + " of " + str(len(batch)) + ":\t" )
            # Without this pause (set to half second currently)
            # the script stops after the 2nd item, probably b/c of API limits
            time.sleep(.5) 
        output.close()
        os.rename('output.txt', 'output.csv')
        print("Complete.")
    except KeyboardInterrupt:
        output.close()
        print("\nExiting...")

base_url = "http://api.ipinfodb.com/v3/ip-city/?format=xml&key="
url = base_url + key
current_batch = get_batch(batch_filename)

print("Added " + str(len(current_batch)) + " entries from " + str(batch_filename) + "\n")
print("Working... This may take a while, please be patient.\n")

batch_process(current_batch)