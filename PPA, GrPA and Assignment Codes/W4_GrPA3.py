'''
Accept two square matrices AA and BB of dimensions nxn as input and compute their product AB.

The first line of the input will contain the integer nn. This is followed by 2n lines. Out of these, each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. Each of the last nn lines is a sequence of comma-separated integers that denotes one row of the matrix B.

Your output should again be a sequence of nn lines, where each line is a sequence of comma-separated integers that denotes a row of the matrix AB.
'''
n = int(input())
matrix1 = []
matrix2 = []
final = []
for i in range(n):
    m1 = []
    x = input().split(',')
    for j in x:
        m1.append(int(j))
    matrix1.append(m1)    
for k in range(n):
    m2 = []
    x = input().split(',')
    for l in x:
        m2.append(int(l))
    matrix2.append(m2)

for i in range(n):
    m3 = []
    for j in x:
        m3.append(0)
    final.append(m3)
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            final[i][j] += matrix1[i][k] * matrix2[k][j]
        if j != n - 1:
            print(final[i][j], end = ',')
        else:
            print(final[i][j])
