"""
Rules for naming variables in python:-
1) We can not use Python Keywords like 'for', 'and', 'while' etc. as variable names.
2) Only alphanumeric characters (all upper and lower case characters and integers from 0 to 9) and underscore(_) in variable names.
3) A variable name must be started with an alphabet or an underscore, but variable name cannot start with a number.
4) Variable names are case-sensitive.
"""
x,y=1,2 #multiple assignments
print(x,y)
a=b=c=10
print(a,b,c)
x,y=y,x #swapping values of variables
print(x,y) # Now x=2, y=1
del(a,b,c) #The variables a, b are deleted now
# print(c) or print(b) or print(a) will give error now since those variables are deleted.
x+=1 #means x=x+1
x*=2 #means x=x*2
x/=6 #means x=x/6
x-=6 #means x=x-6
print(x)
# Using 'in' operator to check if a particular string/character exists in another String:-
print('alpha' in 'A variable name can only contain alpha-numeric characters and underscores')
print('alpha' in 'A variable name must start with a letter or the underscore character')
print("----------------------------")
#Using Chaining operators (When we use multiple relational operators in a single statement, it is called Chaining Operator) to check validity of expressions:-
p=5
print(1<p<10)
print(10<p<20)
print(p < 10 < p*10 < 100)
print(10> p <=9)
print(5 == p > 4)
