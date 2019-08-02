#!/usr/bin/env python3
"""Alta3 Research || Author" RZFeeser@alta3.com"""

#Imports always go at the top of code
import requests

def main():
    """Run time code"""
    #create r which is your request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    
    #catfact is our iterable -- that means it will take on the values found within
    #r.json()["all"]...one after the next, which happens to be in a dictionary
    #the code within the loop says "from that dictionary, print the value associated with the key "x"
    for catfact in r.json()["all"]:
        print(catfact.get("text"))
    

main()
