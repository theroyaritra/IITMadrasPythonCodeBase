def myFunction1(x): #This x has a local scope within the myFunction1() method
    x=x*2
    print('Value of x in the 1st function is = ',x)

def myFunction2(x): #This x has a local scope within the myFunction2() method
    x=x*3
    print('Value of x in the 2nd function is = ',x)

def myFunction3(): # Note : We do not take any parameters in the function declaration when we want to use globally accessible value of x
    global x # By using the 'global' keyword and then typing the variable, we specify the computer to access the globally accessible value of x
    x=x*10
    print('Value of x in the 3rd function is = ',x)

x=5 #This variable x is globally accessible
print('Value of x before function call is = ', x)
myFunction1(x)
myFunction2(x)
print('Value of x after 1st and 2nd function calls is = ', x)
myFunction3()
print('Value of x after 3rd function call is = ', x)