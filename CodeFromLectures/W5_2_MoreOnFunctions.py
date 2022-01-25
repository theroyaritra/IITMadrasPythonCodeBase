#In Python, Functions can also process lists as both input and output
def first_element(l):
    return l[0]
def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if(l[i]<mini):
            mini=l[i]
    return mini
def list_max(l):
    maxi=l[0]
    for i in range(len(l)):
        if(l[i]> maxi):
            maxi=l[i]
    return maxi
def append_before(a,b): #To append list b before list a
    m=b+a
    return m
    '''
    #Sudarshan sir's more complicated way:-
    newl=[]
    for i in range(len(b)):
        newl.append(b[i])
    for i in range(len(a)):
        newl.append(a[i])
    return newl
    '''
def list_average(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    avg=sum/len(l)
    return(avg)
x=[]
for i in range(5):
    n=int(input())
    x.append(n)
print (x)
print('The first element of the list you have input is =', first_element(x))
print('The minimum value in the list you have input is = ', list_min(x))
print('The maximum value in the list you have input is = ', list_max(x))
p=[45,84,-9854,-63]
print(append_before(p,x))
print("The average of all elements in the new list is = ", list_average(append_before(p,x)))