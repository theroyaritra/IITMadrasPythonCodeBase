# 3 types of errors that are exception, and can be handled with Exception Handling are : 1) Divide by 0, 2) Variable not defined, 3) File Not Found. There are many more (nearly 30) exceptions that can be handled in python.
# https://www.programiz.com/python-programming/exception-handling

a=int(input())
b=int(input())
try:
    f=open('abc.txt','r')
    c=a/b
    print(d)
    print(c)
    f.close()
except ZeroDivisionError:
    print("Invalid Input - Division by 0 is not possible")
except NameError:
    print("Variable not Defined!")
except FileNotFoundError:
    print("File not Found!")
except:
    print("Something went wrong!")
else:
    print("Nothing Went Wrong")
finally:
    #f.close()
    print("This is finally block which will be always executed even if there are no exceptions to handle!")
