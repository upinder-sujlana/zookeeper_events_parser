#! /usr/bin/python

"""
   A quick script to grab all the events from the zkEvents.log and print the events in a clean fashion.
   This is usefull in the Hyperflex Environment to check the cluster events with zookeeper point of view.
"""
__author__ = "Upinder Sujlana"


import re
import json
from datetime import datetime

zkeventsList=[]
listOfDictionaries=[]

regex = r"\{(.*?)\}"

with open("/var/log/springpath/zkEvents.log") as handle:
    zkeventsList=handle.readlines()

for line in zkeventsList:
    if "data:" in line:
        m=re.search(regex, line, re.MULTILINE | re.DOTALL)
        listOfDictionaries.append(json.loads(m.group(0)))



for item in listOfDictionaries:
    for key,value in item.items():
        if key=='timestamp':
            print ("Timestamp   :- " + datetime.fromtimestamp(int(value)/1000).strftime("%Y-%m-%d %I:%M:%S")    )
        elif key=='description':
            print ("Description :- " + value)
        elif key=='id':
            print ("Id          :- " + value)
        else:
            print ("")
    print ("******************************************************************************************\n")
        

