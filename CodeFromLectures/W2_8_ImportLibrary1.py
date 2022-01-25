print('First We import the math library:-')
import math
print(math.log(10))
print(math.cos(30))
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(10,3))

print('Now we shall import the random library:-')
import random
print(random.random()) #Gives us a random number between 0 and 1

print('Simulating coin toss using the random function of the random function in random library:- ')
a=random.random()
print (a)
if(a<0.5):
	print('Heads')
else:
	print('Tail')

print('Simulating Dice Roll of six-faced dice using random function:-')
print(random.randrange(1,7)) # Gives us a random integer between the specified range of integers excluding the upper range.

print('Simulating the sum of outcome out of rolling 2 six-faced dice simultaneously:- ')
dice1=random.randrange(1,7)
dice2=random.randrange(1,7)
total=dice1 + dice2
print('Your sum of the outcomes of a pair of dice is = ', total)
# You can verify central limit theorem by running the code multiple times and seeing the random outcome