# Better Factorial Program:- [To fit all possible test cases]
num=int(input('Enter a number whose factorial you want to find: '))
fact=1
original=num
if(num<0):
	print('Undefined')
else:
	while(num>0):
		fact=fact*num
		num=num-1
	print('The factorial of the number ', original, 'is = ', fact)

# Program to find number of digits in given number:-
print('This is a program to find number of digits in given number:-')
n=abs(int(input('Enter the number whose number of digits you want to find'))) #Takes absolute value of the user-input number
digits=1
while(n>9):
	n=n//10 #Remember the // (floor division) operator only returns the integer part of quotient on division
	digits+=1
print('The number has ', digits, ' digit(s)')

# Program to reverse the digits of a given number and check if number is palindrome or not:-
print('This is a program to reverse the digits of a given number:-')
num2=(int(input('Enter the number which you want to be printed in the reverse order'))) 
absolute=abs(num2) #Takes absolute value of the user-input number
rev=0
while(absolute>0):
	last=absolute%10
	rev=rev*10+last
	absolute=absolute//10
if(num2>=0):
	result=rev
else:
	result=rev-2*rev #Or, we can simply write result = (0-rev)
print(result) 
if(num2==result):
	print('The number ', num2, 'is a palindrome number.')
else:
	print('The number ', num2, 'is not a palindrome number.')