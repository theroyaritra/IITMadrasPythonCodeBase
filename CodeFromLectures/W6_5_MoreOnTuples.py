#Packing and unpacking using tuples:-

t=1,2,3 #Packing
print(t,type(t))

x,y,z=t #Unpacking
print(x,y,z)

a=5
b=10
a,b=b,a #Internally packing and then unpacking happens
print(a,b)

#Tuples of single element and their comparison to list of single element:-
l=[10]
print(l,type(l))

t1=(10) #Whenever there is only 1 element in a tuple, python considers it as a single value (integer or anything else) and not a tuple
t2=(10,) #Now that we add a ',' after the single element in the (), python recognizes it as a tuple
print(t1,type(t1))
print(t2,type(t2))

#Creating tuples with lists and tuples inside them and manupulating lists inside tuples:-
t=([1,2],['a','b'],(4,5,85))
print(t)
'''
t[0]=(10,20) #Not possible as tuples are immutable
print(t) #Shows error as expected
'''
t[0][0]=10
t[1][0]='Aritra'
print(t)

#Hashable and non-Hashable:-
#If the values inside a tuple are also immutable then the tuple is considered as hashable and if the values inside a tuple are mutable then the tuple is considered as non-hashable.
tic1=(1,2,3) #Hashable
tic2=([1,2,3],) #Non-Hashable