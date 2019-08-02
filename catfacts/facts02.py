#!/usr/bin/env python3
"""Alta3 Research || Author" RZFeeser@alta3.com"""

#Imports always go at the top of code
import requests

def main():
    """Run time code"""
    #create r which is your request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    #display the methods available to our new object
    ##the json method will dump a json string into Pythonic data
    ###if we request the "all" key, we can strip off the outside {}//this is CRITICAL to parse the data
    print(r.json().get("all"))

main()
