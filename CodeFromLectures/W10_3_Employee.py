from W10_3_Person import Person #Thus we import class Person from file W10_3_Person.py
class Employee(Person): #class Employee inherits the attributes of parent class Person
    count=0
    def __init__(self,name,age,Aadhar,salary):
        super().__init__(name,age,Aadhar)
        self.salary=salary

    def display(self):#Here we observe a case of method overriding
        print(self.name,self.age,self._AadharNumber,self.salary)

e=Employee('Aritra Roy', 24, '8554-7559-6993', 2400000)
e.display()