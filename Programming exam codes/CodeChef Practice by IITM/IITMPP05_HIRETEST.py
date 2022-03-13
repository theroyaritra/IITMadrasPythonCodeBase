# cook your dish here
for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    x,y=[int(a) for a in input().split()]
    l=[]
    for j in range(n):
        l.append(input())
    result=''
    for each in l:
        if(each.count('F')>=x) or (each.count('F')==x-1 and each.count('P')>=y):
            result+='1'
        else:
            result+='0'
    print(result)