class Person: #Here, Person is the parent class or super class
    def __init__(self,name,age,Aadhar):
        self.name=name
        self.age=age
        self._AadharNumber=Aadhar # The ._ is used to indicate private attributes or member that are protected and not accessible from outside.

    def display(self):
        print("Name : ",self.name," Age : ", self.age," Aadhar Number : ",self._AadharNumber)

#m=Person("Aritra Roy",21,'9841-5225-8775')
#m.display()