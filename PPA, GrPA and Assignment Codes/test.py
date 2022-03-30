word="([{}])"
word=")([]"
for i in range(len(word)):
  if(word[i]=='(' and ')' not in word[i:]) or (word[i]=='{' and '}' not in word[i:]) or (word[i]=='[' and ']' not in word[i:]):
    print(word[i:],False)
  else:
    print(True)