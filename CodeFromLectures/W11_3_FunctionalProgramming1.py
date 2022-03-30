# About Iterators and Generators:-

fruits=['mango','apple','banana','guava','pear','grape','watermelon']
#for fruit in fruits:
    #print(fruit)
basket=iter(fruits) #Only works for all iterable entities like Strings, Lists, Tuples. Here basket is an iterator created using the 'iter()' function
print(basket)
print(next(basket))
print(next(basket))
print(next(basket))

def square(limit):
    x=0
    while x<limit:
        yield x*x  #yield keyword is used to convert a regular python function into a generator
        yield x**3
        x+=1

a=square(8) #a is an iterator here
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))