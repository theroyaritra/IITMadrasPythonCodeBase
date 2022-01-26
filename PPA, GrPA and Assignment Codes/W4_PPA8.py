'''
Accept a positive integer n as input and print the identity matrix of size n x n. Your output should have n lines, where each line is a sequence of n comma-separated integers that corresponds to one row of the matrix.
'''
n=int(input())
matrix=[]
x=[]
for i in range(n):
    x=[]
    for j in range(n):
        if(i==j):
            x.append(1)
        else:
            x.append(0)
    matrix.append(x)
for i in range(n):
    for j in range(n):
        if(j!=n-1):
            print(matrix[i][j],end=',')
        else:
            print(matrix[i][j])