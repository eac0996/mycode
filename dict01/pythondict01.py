#!/usr/bin/env python3
##create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

##display parts of the dictionary
print(switch['hostname'])
print(switch['ip'])

##request a fake key
##print(switch['lynx'])

##request a fake key with the .get() method
print("First test - .get()")
print(switch.get('lynx'))

print("Second test - .get()")
print(switch.get('lynx', "The key is in another castle!"))

print("Third test - .get()")
print(switch.get('version'))

print("Fourth test - .keys()")
print(switch.keys() )

print("Fifth test - .values()")
print(switch.values() )

print("Sixth test - .pop()")
switch.pop('version') #removes this key:value pair
print(switch.keys()) #notice the version value is gone
print(switch.values()) #notice value 1.2

print("Seventh test - ADD a new value")
switch['admin login'] = 'karl08'
print(switch.keys())
print(switch.values())

print("Eigth test - ADD a new value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())
