n=int(input())
station_dict={}
for i in range(n):
    train_name=input()
    m=int(input())
    x={}
    for j in range(m):
        s=input().split(',')
        x[s[0]]=int(s[1])
    station_dict[train_name]=x

#print(station_dict)

