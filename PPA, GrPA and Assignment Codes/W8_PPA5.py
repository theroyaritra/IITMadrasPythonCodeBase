def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

print(palindrome("mom"))
print(palindrome("random"))
print(palindrome("a"))
print(palindrome("ab"))
print(palindrome("aba"))
print(palindrome("abcba"))
print(palindrome("malayalam"))