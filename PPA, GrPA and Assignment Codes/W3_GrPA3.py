a = input()
x,y=0,0
dist=0
b=''
if(a == 'START'):
    while(b != 'STOP'):
        b=input()
        if(b=='UP'):
            y+=1
        elif(b=='DOWN'):
            y-=1
        elif(b=='RIGHT'):
            x+=1
        elif(b=='LEFT'):
            x-=1
    dist=abs(x)+abs(y)
print(dist)