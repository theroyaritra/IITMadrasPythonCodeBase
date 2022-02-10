''' d={'key':'value'}
Every key in a dictionary must be unique although duplication is allowed in case of values.

Integers, Float, Boolean, Strings, Hashable Tuples and other immutable datatypes can be used as dictioanry keys.
Lists, Non-Hashable Tuples and Dictionaries can not be used as dictionary keys as they mutable.
Values can be of any datatype.

All properties of copying mutable datatypes like lists apply to dictionaries as well. That means, to copy a dictionary to new memory location we have to use .copy() method etc.
Dictionaries are only passed by call-by-reference through functions.
'''
d={0:12,1:45.365,2:96.52,3:"Aritra",4:[0.2564,45,True,"Hello World!"]}
print(d)
for key in d:
    print(key," ", d[key])

print(d.keys()) #Prints a list of all keys in the dictionary
print(d.values()) #Prints a list of all values in the dictionary
print(d.items()) # Prints a list of all elements in the dictionary as tuples of two i.e. Each key-value pair is a tuple.

