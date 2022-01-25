'''
Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. Print this new string as output. You can assume that all input strings will be in lower case.
'''
first,second=input().lower(),input().lower()
end=''
for i in first:
    for j in second:
        if(i==j):
            second =second.replace(j,'')
            
print(second)