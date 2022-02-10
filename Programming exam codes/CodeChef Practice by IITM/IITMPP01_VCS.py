# https://www.codechef.com/IITMPP01/problems/VCS
def keepcount(l1,l2):
    c1,c2=0,0
    l=[]
    for i in range(1,n+1):
        if i in l1 and i in l2:
            c1+=1
        elif i not in l1 and i not in l2:
            c2+=1
    l.append(c1)
    l.append(c2)
    return l

t=int(input())
d={}
for i in range(t):
    s1=input().split()
    n=int(s1[0]) #Number of source files in project
    m=int(s1[1]) #Number of ignored source files in project
    k=int(s1[2]) #Number of tracked source files in project
    ignored=[]
    tracked=[]
    s2=input().split()
    for e in s2:
        ignored.append(int(e))
    s3=input().split()
    for e in s3:
        tracked.append(int(e))
    d[i]=keepcount(ignored,tracked)
for keys in d:
    print(d[keys][0]," ",d[keys][1])