s = 'good'
print(s*5)  # Replication of a String (Here String s has been replicated 5 times)
print(s[0]*5)
# Comparison of Strings:-
x = 'India'
y = 'apple'
print(x == 'India')
# Relational operators are case-sensitive while comparing between strings
print(x == 'india')
# Computer starts comparing strings character by character. 0th letter of the 2 strings will be compared first.
print(x >= y)
print(y > 'one')  # a is not greater than o in alphabetical order
print('four' < 'ten')  # f is less than t in alphabetical order
# First character is same. But 2nd character b is less than z in alphabetical order
print('ab' < 'az')
# First 2 characters are same. But 3rd character c is not greater than f in alphabetical order
print('abc' > 'abf')
# First 5 characters are equal but when 5th character 'f' of first string is compared to nothing in second character, first string is declared greater than second string.
print('abcdef' > 'abcde')
# Negative indexing of String:-
m = 'Aritra Roy'
print(m[-1])
print(m[-2])
print(m[-3])
print(m[-4])
print(m[-5])
print(m[-6])
print(m[-7])
print(m[-8])
print(m[-9])
print(m[-10])
# We observe that negative index of String denotes its characters in the reverse order
# Finding length of string using len function:-
print('Length of the string m is = ', len(m))
