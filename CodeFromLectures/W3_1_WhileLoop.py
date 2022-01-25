#Program 1:-
year=int(input('Enter the year of Independence of India: '))
while(year != 1947):
	print('You got it wrong. Please try again.')
	year=int(input())

print('Yeah! You got it right. India got independence in the year 1947')
# Program 2:-
print('Now we shall compute factorial using while loop.')
num=int(input('Enter the number whose factorial you want to find: '))
i=1
fact=1
while(i<=num):
	fact=fact*i
	i+=1

print('Factorial of the number', num, 'is = ', fact)

