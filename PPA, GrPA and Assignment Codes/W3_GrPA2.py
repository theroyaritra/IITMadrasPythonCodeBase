'''
Accept a positive integer n, with n > 1, as input from the user and print all the prime factors of n in ascending order.
'''
n=int(input())
if(n>1):
    for i in range(2,n+1):
        if(n%i==0):
            flag=False
            for j in range(2,i):
                if(i%j==0):
                    flag=True
            if(flag==False):
                print(i)