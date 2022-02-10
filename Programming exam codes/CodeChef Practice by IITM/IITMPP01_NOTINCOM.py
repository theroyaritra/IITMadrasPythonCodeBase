# https://www.codechef.com/IITMPP01/problems/NOTINCOM
t=int(input())
common=[]
for i in range(t):
    s=input().split()
    n=int(s[0])
    m=int(s[1])
    s1=input().split(' ')
    l1=[]
    for e in s1:
        l1.append(int(e))
    s2=input().split(' ')
    l2=[]
    for e in s2:
        l2.append(int(e))
    common.append(len(set(l1).intersection(set(l2))))
for e in common:
    print(e)

