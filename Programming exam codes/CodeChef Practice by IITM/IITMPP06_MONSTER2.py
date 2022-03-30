for i in range(int(input())):
    a,b,x,y=[int(x) for x in input().split()]
    if(y>=x):
        print(0)
        continue
    m,n=0,0
    m=b//y
    if(b%y!=0):
        m=m+1
    n=a//(x-y)
    if(a%(x-y)!=0):
        n=n+1
    if(m>n):
        print(1)
    else:
        print(0)
    