x = [1, 7, 3, 4]
y = [8, 6, 3, 2]
m = 0
if(len(x) == len(y)):
    for i in range(len(x)):
        m = m+x[i]*y[i]
    print(m)
else:
    print('The dot product is not possible as the 2 vectors are not of same sizes')
# In this case the dot product program doesn't work in case the 2 lists are not of same size
