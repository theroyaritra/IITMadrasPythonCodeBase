for i in range(int(input())):
    n=int(input())
    s=input().split(' ')
    l=[]
    for i in range(n):
        l.append(int(s[i]))
    c=1
    for j in range(0,n-1):
        if(l[j+1]<l[j]):
            c+=1
        else:
            diff=l[j+1]-l[j]
            l[j+1]=l[j+1]-diff
    print(c)