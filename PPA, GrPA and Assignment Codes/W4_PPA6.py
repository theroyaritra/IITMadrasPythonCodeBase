# Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.
s=input().split(',')
m=[]
for i in s:
    m.append(i)
for j in range(len(m)-1, -1,-1):
    if (j!=0):
        print(m[j],end=',')
    else:
        print(m[j])