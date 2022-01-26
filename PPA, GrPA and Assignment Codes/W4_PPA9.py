''' 
The first line of input is a positive integer, n, that denotes the dimension of the matrix A. Each of the next nn lines contains a sequence of space-separated integers. The last line of the input contains the integer s.
Print the matrix s . A as output. Each row of the matrix must be printed as a sequence of space separated integers, one row on each line. There should not be any space after the last number on each line. If the expected output looks exactly like the actual output and still you are getting a wrong answer, it is because of the space at the end.
'''
n= int(input())
matrix=[]
for i in range(0,n):
    m=[]
    x=input().split(' ')
    for j in x:
        m.append(int(j))
    matrix.append(m)
s= int(input())
for i in range(n):
    for j in range(n):
        matrix[i][j]=s*matrix[i][j]
        if(j!=n-1):
            print(matrix[i][j],end=" ")
        else:
            print(matrix[i][j])
