def number_grid(m, n):
    f = open('numgrid.csv', 'w')
    x = 1
    line = ''
    while x <= m * n:
        line = line + str(x)
        if x % n == 0:
            if x != m * n:
                line = line + '\n'
            f.write(line)
            line = ''
        else:
            line = line + ','
        x = x + 1
    f.close()