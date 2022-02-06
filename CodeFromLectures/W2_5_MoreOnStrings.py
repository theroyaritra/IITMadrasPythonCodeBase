alpha = 'abcdefghijklmnopqrstuvwxyz'  # Set of English alphabets in a String
i = 22
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
print("........................................")
j = 29
print(alpha[j % 26])
print(alpha[(j+1) % 26])
print(alpha[(j+2) % 26])
print("........................................")
# CEASER CIPHER - To output string with k-unit letter shift:- [Important programming concept useful in cryptography]
n = 'aritra'
t = ''
x = 0
k = 2  # The letter is to be shifted by k units on English alphabets
t = t+(alpha[(((alpha.index(n[x])) + k) % 26)])
t = t+(alpha[(((alpha.index(n[x+1])) + k) % 26)])
t = t+(alpha[(((alpha.index(n[x+2])) + k) % 26)])
t = t+(alpha[(((alpha.index(n[x+3])) + k) % 26)])
t = t+(alpha[(((alpha.index(n[x+4])) + k) % 26)])
t = t+(alpha[(((alpha.index(n[x+5])) + k) % 26)])
print(t)
