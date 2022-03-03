class Student: #By convention, first letter of class name is always written in capital letters. We can also use Student() i.e. paranthesis after classname
    roll_no=None
    name=None
s0=Student() #Here, Student() is a constructor, which is used to construct the object s0
s0.roll_no=0
s0.name='Bhuvanesh'
print(s0.roll_no, " : ", s0.name)

s1=Student()
print(s1.roll_no,",",s1.name)

s2=Student()
s2.roll_no=2
s2.name='Harish'
print(s2.roll_no, " : ", s2.name)

s50=Student()
s50.name='Ashmita'
print(s50.roll_no, ":", s50.name)