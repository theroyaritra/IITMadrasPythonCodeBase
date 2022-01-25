''' Easy Solution using functions:-
def add(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input())
c=0
for j in range(1,n+1):
    c=c+add(j)
print(c)
'''
n=int(input())
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print (sum)