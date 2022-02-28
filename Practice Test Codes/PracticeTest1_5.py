'''
You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a substring in the given string. Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.
The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.
'''
s,a,b=input(),int(input()),int(input())
n=s[a:(b+1)]
p=len(s)-len(n)
c=n
if(p>0):
    while(len(s)>=len(c)):
        c=c+n
else:
    c=n
print (c)