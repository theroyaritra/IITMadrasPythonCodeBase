import time
import W8_3_Search as w
import W8_4_BinarySearchImplementation as bin
def sum(a):
    s=0
    for i in range(a):
        s=s+i
    return s
a=time.time()
print(sum(100000))
b=time.time()
print(b-a) #This gives us the time in seconds that the program took to execute : print(sum(100000)) including the sum function within it

l=[1,2,3,4,5,6,7,8,9,10]
begin,end=0,9
mid=(begin+end)//2 #gives us midpoint of a list
print(w.obvious_search(l,5))
print("\n")
m=list(range(1000000))

# Now we note the time taken for linear search and binary search:-
a=time.time()
print(w.obvious_search(m,98598956))
print(w.obvious_search(m,985095))
b=time.time()
print(b-a)

m=list(range(1000000))
a=time.time()
print(bin.binary_search1(m,98598956))
print(bin.binary_search1(m,985095))
b=time.time()
print(b-a)
#We observe that binary search takes much less time than linear search.

