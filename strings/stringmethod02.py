#!/usr/bin/env python3
"""Alta3 Research | | Author: RZFeeser@alta3.com"""
def main():
    """Run-time code"""
    #create a small string
    lilstring = "Alta3 research offers classes on Python coding"
    newlist = lilstring.split(" ") #this returns a new list
    print(newlist)

    #create a list of strings
    myiplist = ["192", "168", "0", "12"]
    singleip = ".".join(myiplist)
    #displays single ip
    print(singleip)

    #call our main function
main()

