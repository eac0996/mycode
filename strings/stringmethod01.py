#!/usr/bin/env python3

#create a small string
lilstring = "Alta3 research offers classes on Python3 training"
newlist = lilstring.split(" ") #this returns a new list split at every space
print(newlist)

#create a list of strings
myiplist = ["192", "168", "0", "12"]
#set singleip as the result of joining the list around the "."
singleip = ".".join(myiplist)
#display single ip
print(singleip)
