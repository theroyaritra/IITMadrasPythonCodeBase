n=input().split(',')
l=[]
for e in n:
    l.append(int(e))
x=int(len(n)/2)
left,right=0,0
for i in range(x):
    left=left+l[i]
    right=right+l[x+i]
if(left>right):
    print("left-heavy")
elif(right>left):
    print("right-heavy")
else:
    print("balanced")