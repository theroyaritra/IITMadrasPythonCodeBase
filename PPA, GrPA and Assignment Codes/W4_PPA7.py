''' 
Accept a square matrix as input and store it in a variable named matrix. The first line of input will be, nn, the number of rows in the matrix. Each of the next nn lines will have a sequence of nn space-separated integers.
'''
matrix=[]
n=int(input())
for i in range(n):
    m=[]
    x=input().split(" ")
    for j in x:
        m.append(int(j))
    matrix.append(m)
print(matrix)