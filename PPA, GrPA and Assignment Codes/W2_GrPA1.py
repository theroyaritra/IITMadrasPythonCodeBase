import math
b, p, h = int(input()), int(input()), int(input())
calc1 = (math.pow(b, 2)+math.pow(p, 2)) == (math.pow(h, 2))
calc2 = (math.pow(b, 2)+math.pow(h, 2)) == (math.pow(p, 2))
calc3 = (math.pow(h, 2)+math.pow(p, 2)) == (math.pow(b, 2))
if(b > 0 and p > 0 and h > 0):
    if calc1 or calc2 or calc3:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
