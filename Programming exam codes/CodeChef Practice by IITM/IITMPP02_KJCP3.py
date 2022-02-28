t=int(input())
x=[]
for i in range(t):
    n=int(input())
    l,l1,l2=[],[],[]
    s1=input().split(' ')
    for e in s1:
        l1.append(int(e))
    s2=input().split(' ')
    for e in s2:
        l2.append(int(e))
    l1.sort()
    l2.sort()
    for i in range(n):
        l.append(l1[i])
        l.append(l2[i])
    x.append(l)
for e in x:
    for i in range(len(e)):
        print(e[i],end=' ')
    print()