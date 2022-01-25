# Understanding for loop syntax in Python:-
j = int(input('Enter number of times you want for loop to run: '))
for i in range(j):
    print(i, "Hello India")
    print("Happy Independence Day")
    if(i % 2 == 0):
        print(i, 'Jai Hind!')
    else:
        print(i, 'Bharat Mata Ki Jai!')

# Program to add the sum of first n natural numbers:-
print("This is a Program to add the sum of first n natural numbers:-")
n = int(input('Enter the value of n: '))
sum = 0
for i in range(1, n+1):  # This means the loop runs from 1,2,3,..,n
    sum = sum+i
print('The sum of first ', n, 'numbers is = ', sum)

# Program to print multiplication table of a natural number:-
print("This is a program to print multiplication table for a natural number from 1 to 10")
num = int(
    input('Enter the number whose multiplication table you want to be printed: '))
for i in range(1, 11):  # Loop runs from 1,2,...,10
    product = num*i
    print(num, ' * ', i, ' = ', product)

# 2 Programs demonstrating for loop with 3 parameters as range i.e. (initial value, end value, step/iteration) :-
print(' This is a program to print only odd numbers from 1 to 10 without using if statement:-')
for i in range(1, 11, 2):  # Loop runs from 1,3,5,7,9
    print(i)
print('This is a program to reverse print even numbers within 20 and 0:-')
for i in range(20, -1, -2):  # Loop runs from 20,18,16,...,0
    print(i)

# Demonstration of For loop without range or For-Each Loop :-
print('Demonstration of For loop without range or For-Each Loop :-')
country = 'India'
for letter in country:
    print(letter)
