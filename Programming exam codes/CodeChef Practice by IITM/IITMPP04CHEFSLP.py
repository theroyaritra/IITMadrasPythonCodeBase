for i in range(int(input())):
    n,l,x=[int(x) for x in input().split(' ')]
    r=n-l
    pair=min(l,r)
    money=pair*x
    print(money)