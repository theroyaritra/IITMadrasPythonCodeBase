s=input().split(',')
real_dict={}
for e in s:
    real_dict[e[0]]=[]
for e in s:
    real_dict[e[0]].append(e)
    
print(real_dict)