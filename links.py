#A Small hack to get the links

from sys import argv
import re

#Unpack the variables from command line arguments
script, key = argv

filename = "/Users/FelixPaul/Programming/Learn Python/LPHW/links.txt"
#create a fileobject
fileObj = open(filename,'r')
#Retreive the data
listOfItems = []
for line in fileObj:
    listOfItems.append(line)

#convert the list to Key value Dictionary and the delimiter being ":",
#using comprehension
keyValue = dict(items.split(':') for items in listOfItems)

#clear up the items from dictionary by stripping of \r and \n,
#using Dict comprehension

newkeyValue = {k.strip().lower():v.strip() for k,v in keyValue.items()}

#check for the key and only if it exist provide the value and display the available key
if key in newkeyValue:
    print newkeyValue [key]
else:
    print "Key does not exist"
    print "These are the available key :"
    for key in newkeyValue.keys():
        print key
#this is to test git flow
