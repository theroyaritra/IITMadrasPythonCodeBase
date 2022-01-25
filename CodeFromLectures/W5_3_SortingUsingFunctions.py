def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if(l[i] < mini):
            mini = l[i]
    return mini


def obvious_sort(l):
    x = []
    while(len(l) > 0):
        mini = list_min(l)
        x.append(mini)
        l.remove(mini)
    return x


p = [10, 8, 54, 9, 6, -8]
print(obvious_sort(p))
