x1, y1, x2, y2, x3 = float(input()), float(input()), float(input()), float(input()), float(input())
if(x2-x1 != 0):
    slope = (y2-y1)/(x2-x1)
    if(slope > 0):
        y3 = y1+(((x3-x1)*(y2-y1))/(x2-x1))
        print(y3)
        print("Positive Slope")
    elif(slope == 0):
        y3 = y1+(((x3-x1)*(y2-y1))/(x2-x1))
        print(y3)
        print("Horizontal Line")
    elif(slope < 0):
        y3 = y1+(((x3-x1)*(y2-y1))/(x2-x1))
        print(y3)
        print("Negative Slope")
else:
    print("Vertical Line")
