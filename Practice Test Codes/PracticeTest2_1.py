n=int(input())
s,p,r,e=[],[],[],[]
for i in range(n):
    if(i in e or i==0):
        s.append(i+1)
    if(i in s):
        p.append(i+1)
    if(i in p):
        r.append(i+1)
    if(i in r):
        e.append(i+1)
if(n in s):
    print("Sapphire")
elif(n in p):
    print("Peridot")
elif(n in r):
    print("Ruby")
elif(n in e):
    print("Emerald")