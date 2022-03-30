a,b=10,20
'''
if a<b:
    small=a
else:
    b
'''
#Using Ternary Operator to write an if-else code-block in a single line and it has same time complexity as if-else code-block:-
small=a if a<b else b
print(small)

x=5
'''
while(a>0):
    print(a)
    a=a-1
'''
#To convert a while loop to a single line of code:-
while x>0: print(x); x-=1

#List Comprehension:-
fruits=['mango','apple','banana','guava','pear','grape','watermelon']
newlist=[fruit.capitalize() for fruit in fruits if 'n' in fruit] #We print all those fruit names in the list fruits (after capitalizing their first letters) names, only if the letter n is in them
print(newlist)
