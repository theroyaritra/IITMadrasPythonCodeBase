# https://www.codechef.com/IITMPP01/problems/SNTFAC3
#The solution is correct but still it can't run successfully on codechef probably because the input testcases have multiple spaces in front of them. I haven't found a way to effective remove the spaces from the inputs and get a successfull execution. I have coded the same program with similar logic in JAVA and I was successful to get a full AC.
#It is a very important question.

t=int(input())
li=[]
for i in range(t):
    s=input().split(' ')
    m,n,k=int(s[0]),int(s[1]),int(s[2])
    l=[]
    for j in range(m):
        l.append(int(input()))
    l.sort()
    sum=0
    for x in range(0,k):
        l[x]=n-l[x]
    for x in range(0,m):
        sum+=l[x]
    li.append(sum)
for e in li:
    print(e)

