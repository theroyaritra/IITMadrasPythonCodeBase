matrix=[]
m=[]
n=int(input())
for i in range(n):
    z=[]
    z=input().split(' ')
    for j in range(n):
        m.append(int(z[j]))
    matrix.append(m[i][j])
print(matrix)