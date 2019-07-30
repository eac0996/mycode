#!/usr/bin/env python3
hostname = input('What value should we set for the host name? ')

##we use string.lower to return a lower case string

if hostname.lower() == "mtg":
    print('The host name was found to be mtg')
    print('The host name matches the expected config')


elif hostname.lower() != "mtg:":
    print('Invalid input')
    
print('Exiting the script')


