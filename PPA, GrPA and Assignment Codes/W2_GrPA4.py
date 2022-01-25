n1,dob1,n2,dob2=input(),input(),input(),input()
d1,d2=int(dob1[0:2]),int(dob2[0:2])
m1,m2=int(dob1[3:5]),int(dob2[3:5])
y1,y2=int(dob1[6:10]),int(dob2[6:10])
if(dob1==dob2):
    if(n1<n2):
        print(n1)
    else:
        print(n2)
else:
    if(y1>y2) or (y1==y2 and m1>m2) or (y1==y2 and m1==m2 and d1>d2):
        print(n1)
    else:
        print(n2)