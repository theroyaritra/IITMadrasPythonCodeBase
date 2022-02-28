f=open("directory.txt","r")
flag=False
s=f.readline()
p=int(input("Enter the number that you want to find in the directory : "))
while(s!=''):
    n=int(s)
    if(n==p):
        flag=True
        print("The number {} was found in the directory".format(n))
        break
    s=f.readline()
if(flag==False):
    print("The number {} was not found in the directory!".format(p))
f.close()