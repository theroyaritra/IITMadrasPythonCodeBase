# https://www.codechef.com/IITMPP01/problems/TLG
n=int(input())
d={}
for i in range(n):
    s=input().split()
    if (i==0):
        d[i]=[int(s[0]),int(s[1])]
    else:
        d[i]=[int(s[0])+d[i-1][0],int(s[1])+d[i-1][1]]
    diff=d[i][1]-d[i][0]
    if(d[i][0]<d[i][1]):
        d[i].append(diff)
        d[i].append(2)
    else:
        d[i].append(-diff)
        d[i].append(1)
l1,l2=[],[]
for key in d:
    l1.append(d[key][2])
    l2.append(d[key][3])
max=l1[0]
x=0
for i in range(len(l1)):
    if(l1[i]>max):
        max=l1[i]
        x=i
print(d)
print(l1)
print(l2)
print(l2[x]," ",max)
    
