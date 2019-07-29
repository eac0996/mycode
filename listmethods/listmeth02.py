#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns') #this will add d,n,s to the end of list
protoa.append('dns') #this will add d,n,s to protoa list
print(proto)
proto2 = [22, 80, 443, 53] #list of common ports
proto.extend(proto2) #pass proto2 as an extend method
print(proto)
protoa.append(proto2)
print(protoa)
