def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    l=len(word)
    f=True
    o=['(','[','{']
    fo=word.count('(')
    fc=word.count(')')
    so=word.count('{')
    sc=word.count('}')
    to=word.count('[')
    tc=word.count(']')
    if(fo!=fc and so!=sc and to!=tc):
        return False
    for i in range(l-1):
        if(word[i]=='[' and (word[i+1]!=']' or word[i+1] not in o)) or (word[i]=='{' and (word[i+1]!='}' or word[i+1] not in o)) or (word[i]=='(' and (word[i+1]!=')' or word[i+1] not in o)):
            return False
    for i in range(l):
        if(word[i]=='(' and ')' not in word[i:]) or (word[i]=='{' and '}' not in word[i:]) or (word[i]=='[' and ']' not in word[i:]):
            return False
    return f