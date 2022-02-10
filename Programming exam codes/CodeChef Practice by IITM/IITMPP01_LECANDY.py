# https://www.codechef.com/IITMPP01/problems/LECANDY
t=int(input())
f=[]
for i in range(t):
    sum=0
    s1=input().split()
    n,c=int(s1[0]),int(s1[1])
    s2=input().split()
    l2=[]
    for e in s2:
        l2.append(int(e))
    for i in range(n):
        sum=sum+l2[i]
    if(sum>c):
        f.append("No")
    else:
        f.append("Yes")
for e in f:
    print(e)
