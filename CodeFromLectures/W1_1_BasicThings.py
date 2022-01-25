# Basic Introduction Stuff:-
print("Hello world," " Kaisa hein bro?", "Printing using double quote.")
print('Printing 10 using single quote.', 'Thats how we print')
a = 10  # Declaring variable
print(a)
a = a+1  # Incrementing value of variable
print(a)
# Taking user input of an integer and printing that number:-
print("Enter a number")
n = int(input())  # That's how we take user input of an integer
print("The number entered is = ", n)
# Combining input and print commands:-
name = str(input('What is your name? '))
age = int(input("What is your age? "))
place = str(input('Where do you live? '))
print('Good to know that you are only ', age, ' years old.')
# Area of circle with radius as user input:-
r = float(
    input('Enter the radius of the circle whose area you want to be calculated.'))
area = 3.14*r*r
print('Area of the circle is = ', area, " square units")
# Data Types:-
print('In this program, variable r is of type : ', type(r))
print('In this program, variable name is of type : ', type(name))
print('In this program, variable area is of type : ', type(area))
l = [10, 20, 30, 68, 732]
print(l)
print("First and last element of l : ",
      l[0], ",", l[4], " and Data type of an individual element of list is : ", type(l[2]))
print("l is of datatype : ", type(l))
