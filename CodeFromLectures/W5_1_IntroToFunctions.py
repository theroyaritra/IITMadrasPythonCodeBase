def add(a,b):
    ans=a+b
    return (ans)
def sub(a,b):
    ans=a-b
    return (ans)
def discount(cost,d):
    ans=cost-(cost*(d/100))
    return (ans)
print(add(4,5)+sub(100,3)+discount(1200,8))
