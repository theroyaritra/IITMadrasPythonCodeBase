# Not an efficient or optimized code!
def check0(L):
    if(len(L)==0):
        return False
    else:
        if(L[0]==0):
            return True
        else:
            return check0(L[1:len(L)])  #You can also write it as "return check0(L[1:])"

print(check0([1,2,6,9,8,45,8]))
print(check0([45,-98,56,5.23,0,145,63,85]))