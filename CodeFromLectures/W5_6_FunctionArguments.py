# Keyword arguments:-
def calculate(c,b,a):
    return(a+b-c)
print(calculate(a=20,b=30,c=40))

def DefCalc(c, a= 20, b=40): #Default arguments are set for a and b
    return (a*b-c)
print(DefCalc(50)) #Here a,b has default values and c=50
print(DefCalc(10,50)) #Here c=10, a=50 and b has default value
print(DefCalc(10,50,30)) #All default values are replaced with c=10, a=50, b=30
print(DefCalc(10,b=60,a=50))