import random
l = []
for i in range(30):
    l.append(random.randint(1, 365))
l.sort()
print(l)
i=c=0
while(i <= len(l)-2):
    if(l[i+1] == l[i]):
        print(l[i], "repeats")
        c += 1
    i = i+1
if(c == 0):
    print('There is no repitition')
