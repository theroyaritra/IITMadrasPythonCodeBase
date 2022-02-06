def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(n):
        psum = psum + L[i] * (x_0 ** i)
    return psum

def poly_zeros(L, a, b):
    zeros = [ ]
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros
x=[]    
x=poly_zeros([-180,-144,101,52,-18,-4,1],0,4)
print(len(x))