n=input()
f=True
c=0
for e in n:
    if(e=='l' or e=='o'):
        f=False
        c=c+1
if(f):
    print("No mistakes")
else:
    print(c,"mistakes")
    x=n.replace('l','1')
    x=x.replace('o','0')
    print(x)