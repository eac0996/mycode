#!/usr/bin/env python3
######EXPLORE READ######
##Create file object in "r"ead mode
configfile = open("vlanconfig.cfg","r")

##display the file to the screen - .read()
print(configfile.read())

##close file
configfile.close()

######EXPLORE READLINES######
##re-create file object to explore new method
configfile = open("vlanconfig.cfg","r")


##Make a list of file lines
configlist = configfile.readlines()
print(configlist)

##Iterate through configlist for x in configlist:
for x in configlist:
    print(x)

##Close file
configfile.close()


