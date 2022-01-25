#The code below is only valid for multiplication of square matrices:-
def initialize_matrix(dim):
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c

def dot_product(a,b):
    dim=len(a)
    ans=0
    for i in range(dim):
        ans=ans+(a[i]*b[i])
    return ans

def row(M,i):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l

def coloumn(M,j):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l

def mat_multiply(a,b):
    dim=len(a)
    c=initialize_matrix(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(a,i),coloumn(b,j))
    return c

m1=[]
m2=[]
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

print(mat_multiply(m1,m2))