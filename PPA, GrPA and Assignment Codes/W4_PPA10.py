'''
Accept two square matrices A and B of dimensions n x n as input and compute their sum A + B.

The first line will contain the integer n. This is followed by 2n lines. Each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. Each of the last nn lines is a sequence of comma-separated integers that denotes one row of the matrix B.

Your output should again be a sequence of n lines, where each line is a sequence of comma-separated integer that denotes a row of the matrix A + B.


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
    x = []
    for j in range(n):
        x.append(matrix1[i][j]+matrix2[i][j])
    final.append(x)
for i in range(n):
    for j in range(n):
        if(j != n-1):
            print(final[i][j], end=",")
        else:
            print(final[i][j])
