m1=[]
m2=[]
m3=[]
r1=int(input('Enter the number of rows of the first matrix: '))
c1=int(input('Enter the number of coloumns of the first matrix: '))
print('Now enter the elements of the first matrix row-wise :- ')
for i in range(r1):
    x=[]
    for j in range(c1):
        x.append(int(input()))
    m1.append(x)
r2=int(input('Enter the number of rows of the second matrix: '))
c2=int(input('Enter the number of coloumns of the second matrix: '))
print('Now enter the elements of the second matrix row-wise :- ')
for i in range(r2):
    y=[]
    for j in range(c2):
        y.append(int(input()))
    m2.append(y)
if(c1==r2):
    z=[[0,0],[0,0]]
    for i in range(r1):
        #z=[]
        for j in range(c1):
            for k in range(c2):
                z[i][j]=z[i][j] + m1[i][k]*m2[k][j]
        #m3.append(z)
    print(z)
else:
    print('Matrix Multiplication is not possible in this case.')