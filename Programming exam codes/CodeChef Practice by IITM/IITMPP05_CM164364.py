for i in range(int(input())):
    n,x=[int(x) for x in input().split()]
    l=list(map(int,input().split()))
    s=len(set(l))
    c=n-x
    print(min(c,s))