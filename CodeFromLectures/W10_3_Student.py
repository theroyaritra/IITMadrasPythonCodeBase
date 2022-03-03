from W10_3_Person import Person #Thus we import class Person from file W10_3_Person.py
class Student(Person): #class Student inherits the attributes of parent class Person
    def __init__(self,name,age,marks,Aadhar):
        super().__init__(name,age,Aadhar)
        self.marks=marks
    
    def display(self):
        super().display()
        print("Marks = ", self.marks)

s=Student('Sandesh YM',19,90,'8554-7554-1221')
s.display()