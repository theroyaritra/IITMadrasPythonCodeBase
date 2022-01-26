names = input().split(',')
bdays = input().split(',')
n = len(names)
for i in range(n):
    bdays[i] = int(bdays[i])

common = [ ]
for i in range(n):
    for j in range(n):
        if ((i != j) and
            (bdays[i] == bdays[j]) and
            names[i] < names[j]):
            pair = [names[i], names[j]]
            common.append(pair)

print(common) #This line is not required in the actual code.