l=[1,58,12,-98,589,58,61,70]
l.sort() #Its easy to do sorting using the built in sort() function
print(l)
#Now comes the obvious sort:-
a=[4,10,95,-87,-569,2614,45,98,95,4]
x=[]
while(len(a)>0):
    min=a[0]
    for i in range(len(a)):
        if(a[i]<min):
            min=a[i]
    x.append(min)
    a.remove(min)
print(x)
