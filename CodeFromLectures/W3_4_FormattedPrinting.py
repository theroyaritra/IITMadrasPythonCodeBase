for x in range(10):
	print(x, end=', ') # end is used to print in a single line according to our requirements
print() # Now we go to next line
print('To print today\'s date:- ')
d=int(input('Enter the day of the month: '))
m=int(input('Enter the month number: '))
y=int(input('Enter the year: '))
print('Today\'s date is : ', end=' ')
print(d,m,y,sep='/') # sep decides the seperator character between variables to be printed

# Printing multiplication table using Formatted Printing in 3 possible ways:- [Change the commented code to practice the other 2 methods]
num=int(input('Enter the number whose multiplication table you want to print: '))
for i in range(1,11):
	# print(f'{num} x {i} = {num * i}') #1st way
	# print('{0} x {1} = {2}'.format(num,i,num*i)) #2nd way : Using format function
	print('%d x %d = %d' % (num,i,num*i)) #3rd way: Using String Modulo operator

#Printing the value of pi in 3 ways of formatted printing:- [Using format specifiers]
pi=22/7
print(f'Value of pi is = {pi:.4f}') # :.4f ensures only 4 decimal places will be printed
print('Value of pi is = {0:.3f}'.format(pi))
print('Value of pi is = %.2f' % (pi)) # %.2f ensures only 2 decimal places will be printed

#Printing a right-aligned pattern:- [using formatted printing and format specifiers]
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
# 5d here specifies that we want to use minimum 5 integers (specified by d) in a print statement

