'''
Accept a phone number as input. A valid phone number should satisfy the following constraints.
(1) The number should start with one of these digits: 6, 7, 8, 9
(2) The number should be exactly 10 digits long.
(3) No digit should appear more than 7 times in the number.
(4) No digit should appear more than 5 times in a row in the number.
If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.
Print the string valid if the phone number is valid. If not, print the string invalid.
'''
n,flag,Flag,f=input(),False,False,False
if len(n)==10 and (n[0]=='6' or n[0]=='7' or n[0]=='8' or n[0]=='9') and n.isnumeric():
    f=True
    for i in range(5):
        if n[i]==n[i+1]==n[i+2]==n[i+3]==n[i+4]==n[i+5]:
            flag=True
    for j in range(len(n)):
        if n.count(n[j])>7:
            Flag=True
if flag==True or Flag==True or f==False:
    print('invalid')
if flag==False and Flag==False and f==True:
    print('valid')