class Person: #Here, Person is the parent class or super class
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

class Student(Person): #class Student inherits the attributes of parent class Person
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    
    def display(self):
        super().display()
        print(self.marks)

class Employee(Person): #class Employee inherits the attributes of parent class Person
    count=0
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def display(self):#Here we observe a case of method overriding
        print(self.name,self.age,self.salary)

s=Student('Sandesh YM',19,90)
s.display()

e=Employee('Aritra Roy', 24, 2400000)
e.display()