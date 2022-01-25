b1 = True
b2 = False
print('Data types of b1 and b2 are : ', type(b1), 'and', type(b2))
# Converting one data type into another:-
a = int(5.695)  # Converting decimal (float) into integer
b = int('10')  # Converting String into integer
c = float('9')  # Converting integer to float
d = float('10.567')  # Converting String to float
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
# Type conversion to and from boolean data type:-
m = bool(10)  # Converting integer to boolean
n = bool(0)  # Converting 0 to boolean
o = bool(-10.25)  # Converting floating point value to boolean
p = bool(0.00)
q = bool('India')  # Converting String to boolean
r = bool('10.4')
s = bool('-52.6')
t = bool('0')
e = bool('')  # Converting empty String to boolean
print(m, type(m))
print(n, type(n))
print(o, type(o))
print(p, type(p))
# Note : In boolean, 0 means False and rest any other number means True value. In boolean, any String value is converted to True value, except the empty String.
print(q, type(q))
print(r, type(r))
print(s, type(s))
print(t, type(t))
print(e, type(e))
