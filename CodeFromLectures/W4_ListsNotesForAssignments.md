
# Lists: Input | Output
How do we accept a list of numbers as input from the user?

Input is always going to be a string. split is a string method that can used to break a string into a list of substrings. For example:

~~~py
line = '1 2 3 4'
output = line.split(' ')
print(output)
~~~
This gives the following output:-
~~~
['1', '2', '3', '4']
~~~
The string '1 2 3 4' has been split using a space. With this idea in place, we can go ahead and populate a list of numbers.
~~~py
line = '1 2 3 4'
num_str = line.split(' ')       # list of numbers represented as strings
numbers = [ ]                   
for item in num_str:
    numbers.append(int(item))   # convert string to int and append to list
print(numbers)
~~~
This gives the following output:-
~~~
[1, 2, 3, 4]
~~~
We can also accept comma separated inputs:-
~~~py
line = '1,2,3,4,5'
for item in line.split(','):    # line.split(',') is a list
    numbers.append(int(item))
print(numbers)
~~~
This gives the following output:-
~~~
[1, 2, 3, 4, 5]
~~~
# Lists: Membership
To check for membership of an element x in a list L, you can use the in keyword:-
~~~py
L = [1, 2, 3, 4, 5]
x = 2
print(x in L)
~~~
This prints True as the output.