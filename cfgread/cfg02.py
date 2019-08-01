#!/usr/bin/env python3
######EXPLORE READ######
##Create file object in "r"ead mode
configfile = open("vlanconfig.cfg","r")

##display the file to the screen - .read()
configblog = configfile.read()

##Break configblog across line boundaries (removes \n)
configlist = configblog.splitlines()

##Display list with no \n
print(configlist)

##Close file
configfile.close()
