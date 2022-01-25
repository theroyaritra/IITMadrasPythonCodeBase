'''
Accept a positive integer n as input and print a "number arrow" of size n. For example, n = 5 should produce the following output:
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1

You can assume that n is greater than or equal to 2 for all test cases.
Hint: range(5, 0, -1) is the sequence 5, 4, 3, 2, 1
'''
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        if(j < i):
            print(j, end=',')
        else:
            print(j, end='')
    print()
for k in range(n-1, 0, -1):
    for l in range(1, k+1):
        if(l < k):
            print(l, end=',')
        else:
            print(l, end='')
    print()
