#Using nested for loop, find all prime numbers less than the entered number:-
n=int(input('Enter a number till which you want to find all prime numbers'))
if(n>2):
    print(2, end=' ')
for i in range(3,n):
    flag=False
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
        else:
            flag=True
    if(flag==True):
        print(i, end=' ')
#Find the length of the longest word from a set of words entered by user:- [Each word input stops when user inputs -1]
print()
word=input()
maxLen=0
while(word!='-1'):
    c=0
    for letter in word:
        c=c+1
    if(c>maxLen):
        maxLen=c
        longest=word
    word=input('Enter another word : ')
print('The length of the longest word "', longest,'" is = ', maxLen)
