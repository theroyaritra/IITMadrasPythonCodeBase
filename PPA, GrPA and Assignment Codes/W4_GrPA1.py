'''
In the first line of input, accept a sequence of space-separated words. In the second line of input, accept a single word. If this word is not present in the sequence, print NO. If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.
'''
s1=input().split(' ')
s2=input()
x=s1.count(s2)
if (x>0):
    print('YES')
    print(x)
else:
    print('NO')

'''
Solution by IIT Madras:-
words = input().split(' ')
test = input()

if test not in words:
    print('NO')
else:
    print('YES')
    count = 0
    for word in words:
        if test == word:
            count += 1            
    print(count)
'''