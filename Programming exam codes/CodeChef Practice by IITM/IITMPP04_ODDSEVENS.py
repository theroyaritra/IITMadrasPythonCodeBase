for i in range(int(input())):
    a,b=[int(x) for x in input().split(' ')]
    sum=a+b
    if(sum%2==0):
        print("Bob")
    else:
        print("Alice")