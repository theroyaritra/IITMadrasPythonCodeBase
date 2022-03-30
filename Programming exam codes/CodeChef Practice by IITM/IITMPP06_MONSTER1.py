# cook your dish here
for i in range(int(input())):
    h,x,y=[int(x) for x in input().split()]
    health=h
    c=0
    while(health>0):
        health=health+y
        health=health-x
        c=c+1
        if(health<=0 or c==50000):
            break
    if(health<=0):
        print(1)
    else:
        print(0)