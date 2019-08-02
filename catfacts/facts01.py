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
    print(r.json())

main()
