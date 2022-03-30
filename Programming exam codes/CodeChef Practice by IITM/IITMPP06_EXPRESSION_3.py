# cook your dish here
for i in range(int(input())):
    a,b,c=[int(x) for x in input().split()]
    if(a+b+c==0 or -a+b+c==0 or -a-b-c==0 or a-b-c==0 or a-b+c==0 or a+b-c==0 or -a-b+c==0 or a-b-c==0):
        print("Yes")
    else:
        print("No")