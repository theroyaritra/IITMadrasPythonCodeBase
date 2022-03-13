# cook your dish here
import string
first=string.ascii_lowercase[0:13]
second=string.ascii_uppercase[13:26]
for i in range(int(input())):
    s=input().split()
    l=s[1:]
    f=False
    for each in l:
        z=[]
        for letter in each:
            if(letter in first):
                z.append('f')
            elif(letter in second):
                z.append('s')
            else:
                z.append('n')
        if('n' in z) or ('f' in z and 's' in z):
            f=False
            break
        else:
            f=True
    if(f):
        print('Yes')
    else:
        print('No')