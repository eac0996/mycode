#!/usr/bin/env python3
##sudo apt install python3-pip
##python3 -m pip install pyexcel 
##python3 -m pip install pyexcel-xls


import pyexcel
# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address\n")
    input_driver = input("What is the driver associated with this device?")
    d = {"IP": input_ip, "driver": input_driver}
    return d
            
	
#Runtime
mylistdict = [] #This is the list we turn to an Excel file
print("Hello!  This program will make you a *.xls file.")

while(True):
    mylistdict.append(get_ip_data())  #add an itel to the list, returned by get_ip_data
    keep_going = input("\nWould you like to add another value?  Enter to continue or press q to quit: ")
    if (keep_going.lower() == "q"):
        break
		
filename = input("\nWhat is the name of the *xls file? ")
pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")
print("The file " + filename + ".xls should be in your local directory")
