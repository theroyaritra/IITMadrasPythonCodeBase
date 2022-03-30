#Using lambda function to shorten function code-blocks into single line code:-
add = lambda x,y:x+y
substract=lambda x,y:x-y
divide=lambda x,y:x/y
multiply=lambda x,y:x*y

print(add)
print(type(substract))
print(add(8,10))
print(divide(15000,30))
print(multiply(81,9))
print(substract(50,9))

#Using enumerate function and zip function:-
fruits=['mango','apple','banana','guava','pear','grape','watermelon','kiwi','avocado']
size=[5,5,6,5,4,5,10,4,7]
for fruit in enumerate(fruits):
    print(fruit)

print(dict(zip(fruits,size)))

#Using maps in python:-
a=[1,2,3,4,5,6,7,8,9,10]
b=[100,90,80,70,60,50,40,30,20,10]
def increment(x):
    return x+1
c=map(substract,a,b) #substract is already a predefined function here
d=map(increment,a)
print(list(c))
print(list(d))

#Using map and filter functions to compute square root of all +ve integers in a given list:-
import math
x=[25,-16,9,81,-100,625]
def is_positive(a):
    if(a>=0):
        return a
SquareRoot=lambda u:math.sqrt(u)
e=map(SquareRoot,filter(is_positive,x)) # Or, we could have used 'lambda u:u>0,x' within the filter() function and completely gotten rid of the is_positive() function.
print(list(e))