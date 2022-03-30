# cook your dish here
for i in range(int(input())):
    p,x,y,z=[int(x) for x in input().split()]
    s=0
    if(z==1):
        s=p+(y/100)*p 
    else:
        s=p-(x/100)*p 
    print(s)