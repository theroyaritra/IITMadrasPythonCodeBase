n=int(input())
s=input()
krushi,mansi='',''
for i in range(len(s)):
    if(i%2==0):
        krushi+=s[i]
    else:
        mansi+=s[i]
a={'U':(0,1),'D':(0,-1),'R':(+1,0),'L':(-1,0)}
k,m=[(0,0)],[(0,0)]
for e in krushi:
    for i in range(len(k)):
        p=(a[e][0]+k[i][0],a[e][1]+k[i][1])
    k.append(p)
for e in mansi:
    for j in range(len(m)):
        q=(a[e][0]+m[j][0],a[e][1]+m[j][1])
    m.append(q)
x=set(k+m)
print(len(x))
