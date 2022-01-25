a=input()
if(len(a)>=8 and len(a)<=32) and (a[0].isalpha()) and not(('=' in a) or ('/' in a) or ('\\' in a) or ("'" in a) or ('"' in a) or (' ' in a)):
    print('True')
else:
    print('False')