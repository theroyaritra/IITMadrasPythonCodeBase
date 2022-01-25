l=[1,2,3,4,5]
print (l)
l.append(100)
l.append(2) #Even when 2 is already present in the list l, once again 2 will be appended
l.remove(2) #It will remove the first occurance of the element 2
print(l)
l.remove(2) #Now it removes the other remaining occurance of 2 as well
print(l)
x=[]
x.append(l) #A list inside a list or, an array within as array
print(x)
m=[10,20,30]
x.append(m) #2 lists l, m within the list x now
print(x)
t=[]
t.append(x)
t.append([50,60,70])
print(t) #1st element is the list x with 2 lists l,m within itself and 2nd element is the list [50,60,70]
print("Now, 1st element [index=0] of the list t is ", t[0]," and 2nd element [index=1] of the list t is ", t[1])
#Now we shall create/store and print a matrix (A matrix is like 2 dimensional array) M:-
M=[]
M.append([1,2,3])
M.append([4,5,6])
M.append([7,8,9])
print(M) #Now M is a 3x3 matrix
for i in range (3):
    for j in range (3):
        print("The element M[",i,"][",j,"] is = ", M[i][j])