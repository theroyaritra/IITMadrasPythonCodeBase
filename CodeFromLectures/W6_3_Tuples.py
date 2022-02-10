t=(108,5,7,9,65,20,19,2)
print("A tuple is unchangable or its immutable unlike lists, which are mutable. We can't append or remove elements from a tuple. We can find elements at particular indices in a tuple. ")
l=list(range(10))
print(l.__sizeof__()) #We observe that size of list of similar size is 120 bytes
t1=tuple(range(10))
print(t1.__sizeof__()) #We observe that size of tuple of similar size in 104 bytes and hence, tuples also consume much less memory than lists.
print(t1)

import string
#Some more applications of special string methods:-
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

s=string.ascii_letters
#s=set(s)
print(s)
alpha=tuple(list(s)) #So that we get ordered/sorted elements in the tuple. In list elements are in specific order, unlike sets or tuples. Here alpha is a tuple but the order of elements is not altered because we first convert the string to a list. Here we don't want alpha to change in any condition. So, we use tuple which is immutable.
print(alpha,"\n")

# We write a small code to print only those chracters in x that are present in alpha, in the form of a list:-
x="Karnataka West Bengal Jai Hind! 1#2$3%4^5& 6 Tamil Nadu Koi MIl gaya!@)(*+_"
l=list(x)
r=[]
for element in l:
    if element in alpha:
        r.append(element)
print(r,"\n")