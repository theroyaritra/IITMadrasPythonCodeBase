'''
Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
'''
''' Code using 1st logic:-
s=input().lower()
x=''
if(s.isalpha()):
    x=x.join(sorted(s))
print(x)
'''
#Code using another logic:-
A=sorted(input().lower())
for i in range(len(A)):
    print(A[i],end='')