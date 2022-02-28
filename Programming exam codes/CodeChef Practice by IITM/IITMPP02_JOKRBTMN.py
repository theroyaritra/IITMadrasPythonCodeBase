x=[]
for t in range(int(input())):
    n, m, l = input().split(' ')
    list_of_lists = {}
    for i in  range(0, int(m)):
        input_list = input().split(' ')[1:]
        for j in input_list:
            list_of_lists[j] = i
    strip = input().split(' ')

    current = list_of_lists[strip[0]]
    count  = 1
    for i in strip:
        if list_of_lists[i] != current:
            count += 1
        current = list_of_lists[i]
    x.append(count)
for e in x:
    print(e)