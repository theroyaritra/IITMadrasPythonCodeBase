r=int(input('Enter the number of rows of the matrix: '))
c=int(input('Enter the number of coloumns of the matrix: '))
m1=[]
m2=[]
m3=[]
print('Now enter the elements of the first matrix row-wise :- ')
for i in range(r):
    x=[]
    for j in range(c):
        x.append(int(input()))
    m1.append(x)
print('Now enter the elements of the first matrix row-wise :- ')
for i in range(r):
    y=[]
    for j in range(c):
        y.append(int(input()))
    m2.append(y)
for i in range(r):
    z=[]
    for j in range(c):
        z.append(m1[i][j]+m2[i][j])
    m3.append(z)
print('The sum of the 2 given matrices is :-' )
print(m3)

''' Line 24 can be also replaced with this code for a better looking matrix output:-
for i in range(R):
    for j in range(C):
        print(m3[i][j], end = " ")
    print()

'''