#!/usr/bin/env python3
"""Alta3 Research  ||  Author: RZFeeser@alta3.com"""

#Function to push commands
def commandpush(devicecmd): #devicecmd = list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ...connecting with ' + coffeetime)
        #We'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffetime]:
            print('Attempting to send command__> ' + mycmds)
            #We'll learn to write code to send commands to devices here

#Start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "no shut"], "10.3.0.1":["interface eth1/5", "no shut"]}
    print("Welcome to the network device command pusher") #welcome message

    #get data set
    print("\nData set found\n") #replace with function call that reads in data from file

    #run
    commandpush(work2do) 
main()
    
#call function to push command
