# cook your dish here
from sys import maxsize

def distinct(n):
    a=str(n)
    f=True
    x={}
    if(len(a)==1):
        f==True
    else:
        for e in a:
            if(e not in x):
                x[e]=1
            else:
                x[e]+=1
        m=list(x.values())
        m.sort(reverse=True)
        if(m[0]!=1):
            f=False
    return f

for j in range(int(input())):
    x=int(input())
    for i in range(x+1,maxsize):
        if(distinct(i)):
            print(i)
            break
