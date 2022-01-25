import random
l = [11, 99, 88, 56, 25]
for i in range(100000):
    l.append(random.randint(1, 10000))
print(l)
print()
a=0
while(a > -1):
    a = int(input('Enter the number whose position(s) you want to find in the above list'))
    flag = 0
    print('The number ', a, 'is present at the following postion(s) of our list above:- ')
    for j in range(len(l)):
        if(l[j] == a):
            print(j)
            flag += 1
    if(flag == 0):
        print('Element is not found')
