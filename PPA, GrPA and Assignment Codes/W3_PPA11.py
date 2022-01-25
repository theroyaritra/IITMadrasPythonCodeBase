n=int(input())
a=b=c=0
for x in range(1,n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            if(x**2 + y**2 == z**2):
                print(x,y,z,sep=",")
                a=x
                b=y
                c=z
if(a==0 and b==0 and c==0):
    print('NO SOLUTION')