# + as concatenation operator in lists:-
l1=[1,2,3]
l2=[10,20,30]
l12=l1+l2
l21=l2+l1
print(l12, l21,"\n")

#Repeating elements in lists with * :-
l1=[0]*5
l2=[1,2,3]*5
print(l1, l2)

#Relational operators and their usages with lists:-
l1=[1,2,3]
l2=[1,2,3]
l3=[1,3,2]
print(l1==l2)
print(l2==l3)
print(l2<l3,"\n")

print([1,2]<[2,1])
print([1]<[1,2,3])
print([2,3]<[3])
print([]<[1])

#Mutability in lists:- [Lists are mutable unlike Strings, Tuples]
list1=[1,2,3]
list2=list1
list1[0]=100
print("\n",list1, list2) #We just updated the value of 0th element in list to 100. But we observe that even the 0th element in list2 has been changed to 100 as well!
print(list2 is list1) #Returns True => list2 and list1 belong to the same memory location

# 4 ways of creating copy of a list, that will create a new memory location:-
list1=[1,2,3,4]
l2=list(list1)
l3=list1[:]
l4=list1.copy()
l5=list1 #not a seperate copy though
print()
print(l2,l3,l4,l5)

print(list1 is list1) # Returns True => l5 and list1 belong to the same memory location
print(l2 is list1) # Return False => l2 and list1 belong to different memory locations
print(l3 is list1) # Return False => l3 and list1 belong to different memory locations
print(l4 is list1) # Return False => l4 and list1 belong to different memory locations
print(l5 is list1) # Returns True => l5 and list1 belong to the same memory location
print()

#Passing lists through functions:- [In case of lists, its call by reference while in case of normal integers its call by value]
def add(x,y):
    x.append(1)
    y=y+1
    return x,y
x=[5]
y=5
print(add(x,y))
print(x,y,"\n")

# Some more list methods:-
list1.insert(2,65) #append() adds the element to the last of the list, while insert() inserts the element at the specified index
print(list1)

list1.pop(2) #remove() removes specified element from the list, whereas pop() removes the element at the specified index
print(list1)
newlist=[52,85,96,-85,-65,20,415,623,554,-988,14]
newlist2=["ari","JaiHind!","KyaRee","hmm","India","TussiGreatHo"]

newlist.sort() #sort() sorts the list (of either only numbers or only Strings as well) in ascending order
print(newlist)
newlist.reverse() # reverse() just reverses the list
print(newlist) 
#Note that we can use sort() and then reverse() methods to sort a list in descending order as well!
newlist2.sort()
print(newlist2)
newlist2.reverse()
print(newlist2)
''' This is also a more effective method to sort lists in descending order:-
newlist2.sort(reverse=True)
print(newlist2)
'''