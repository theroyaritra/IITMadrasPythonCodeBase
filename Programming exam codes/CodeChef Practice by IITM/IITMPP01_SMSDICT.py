# https://www.codechef.com/IITMPP01/problems/SMSDICT
def wordtonumber(w,lwords):
    s=''
    for i in range(0,len(w)):
        for j in range(2,10):
            if(w[i] in lwords[j]):
                s=s+str(j)
    return (int(s))

lwords={2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'],9:['w','x','y','z']}
m=int(input())
l=[]
for i in range(m):
    s=input()
    l.append(wordtonumber(s,lwords))
x=[]
for e in l:
    x.append(l.count(e))
max=x[0]
p=0
for i in range(len(x)):
    if(x[i]>max):
        max=x[i]
        p=i
print(l[p])