# Movie Ticket Scenario:-
birth_year = int(input('Please enter your year of birth'))
current_year = 2021
age = current_year-birth_year
if(age < 13):
    print('You are under-age and hence, can\'t watch this movie.')
    print('Wait until you are 13 years of age at least to watch this movie.')
else:
    print('You are old enough to watch the movie.')
    print('Don\'t forget to watch the prequels and sequels.')

print('Have a nice time')
# Even Odd Numbers Program:-
num = int(input('Enter an integer to check if it is even or not : '))
if(num % 2 == 0):
    print('Even number')
else:
    print('Odd number')

# Number Ending with 5 or 0 or anything else:-
n = int(input('Enter a number : '))
if(n % 5 == 0):
    if(n % 10 == 0):
        print('0')
    else:
        print('5')
else:
    print('Other')

# Marks Classification and Gradation of student:-
marks = int(input('Enter marks : '))
if(marks >= 0 and marks <= 100):
    if(marks >= 90):
        print('Grade A')
    elif(marks >= 80 and marks < 90):
        print('Grade B')
    elif(marks >= 70 and marks < 80):
        print('Grade C')
    elif(marks >= 60 and marks < 70):
        print('Grade D')
    else:
        print('Grade E')
else:
    print('Invalid Input')
