for i in range(int(input())):
    n=int(input())
    l=list([int(x) for x in input().split()])
    if(n<=2):
        print(0)
        continue
    d={}
    for e in l:
        if(e in d):
            d[e]+=1 
        else:
            d[e]=1 
    m=max(d.values())
    if(m==1): 
        print(n-2) # When all numbers distinct, we can keep any 2 numbers and delete the others
    else:
        print(n-m)
            