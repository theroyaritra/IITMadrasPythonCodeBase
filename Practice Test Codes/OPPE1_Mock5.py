s=input().split(' ')
m=0
import operator
a={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
if(s[0]=='minus'):
    m= -int(a[s[1]])
elif(s[0]=='plus'):
    m= +int(a[s[1]])
sum,c=0,0
for i in range(len(s)):
    if(s[i]=='plus'):
        sum+=sum
print(m)