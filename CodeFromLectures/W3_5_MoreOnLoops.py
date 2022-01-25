#For Each loop to find the number of digits in a number:-
num=abs(int(input()))
strNum=str(num)
digits = 0
for c in strNum:
    digits=digits+1
print(digits)
#Reversing a number using for each loop:-
num2=int(input())
absnum2=abs(num2)
str2=str(absnum2)
rev=''
for b in str2:
    rev=b+rev
if(num2>0):
    print(rev)
else:
    rev='-'+ rev
    print(rev)
#Checking for palindrome number using for each loop:- (Checking if variable 'num 2' input is palindrome or not)
if(rev==str(num2)):
    print(num2 ,' is a palindrome number')
else:
    print(num2 ,'is not a palindrome number')