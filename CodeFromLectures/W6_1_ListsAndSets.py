x= [1,2,3,4,5,6,'aritra',77,85,3]
y={5,9,8,7,5,52,-78}
print(x,type(x)) #List can have repeated elements
print(y,type(y)) #Set can not have repeated elements
l=list(range(100))
s=set(range(100))
print(l)
print(s)
# Searching is easier in set than in list
# But, it takes the computer much more time to process and produce a set than a list as set takes a lot more memory space than list
import numpy
import sys
l0=[]
l1=[0]
l2=[0,1]
print(sys.getsizeof(l0)) # Amount of space allocated to the list l0 in bytes
print(sys.getsizeof(l2))

print(sys.getsizeof(s)) # 8408 bytes! Set for same elemets is allocated much larger space than its counterpart list
# Note: s[1],s[0] won't work! There is no first, second element etc. in a set. Set object is not subscriptable.
print(sys.getsizeof(l)) # Only 856 bytes allocated
s1={'amit','aritra','dhanwanth','ayan','abhijit'}
s1.add('sudarshan')
print(s1)
print('Sandesh' in s1)

x[4]=154
print(x) #Similar kind of replacement of an element is not possible in a set
print(set(x))