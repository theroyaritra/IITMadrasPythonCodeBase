#Set is an unordered entity. Set is not subscriptable as well.
#Set itself is mutable but every value inside a set has to be hashable and immutable. Hence we cannot add a list or a dictionary or a tuple containing a list or a dictionary to a set.
#We can iterate over a set.

A= {1,2,3,4,5,1,2,3,5} #A[0] or A[1] is undefined
print(A)
B={1,2,3,4,3,5}
C={1,3,5}
D={1,2,3}
print(A.issubset(B))
print(C.issuperset(B))

C1=A|C #Union without using union method
print(A.union(C),C1)

C2=A&C #Intersection without using intersection method
print(A.intersection(C),C2)

D1=D.difference(C)
D2=D-C
print(D1,D2)

#Thus, we can use many other methods on sets.