import string
s=input()
d1,d2={},{}
a=string.ascii_lowercase
for i in range(1,14):
    d1[a[i-1]]=a[-i]
    d2[a[-i]]=a[i-1]   
encrypt=''
for e in s:
    if e in d1:
        encrypt+=d1[e]
    elif e in d2:
        encrypt+=d2[e]
    else:
        encrypt+=e
print(encrypt)
