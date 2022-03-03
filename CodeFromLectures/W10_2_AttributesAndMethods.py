class Student:
    count=0
    def __init__(self,roll_no,name,total): # __init__ is 2 underscores followed by 'init' followed by 2 underscores and its used to initialize attributes of a class and parameters of the objects of the class. We must use self as the first parameter in every method within the class.
        self.roll_no=roll_no
        self.name=name
        self.total=total
    #self and __init__ are keywords here
    def display(self):
        print(self.roll_no,":",self.name, " : ", self.total)
    
    def result(self): #This is to add a behaviour to the objects inside the class
        if(self.total>90):
            print("Pass")
        else:
            print("Fail")
# Note : When any function is inside a class or belongs to a class, it is called as method. Eg: String methods and the above methods inside class Student
s0=Student(0,"Bhuvanesh",96) #Here, Student() is a constructor, which is used to construct the object s0
Student.count+=1
s0.display()
s0.result()

s1=Student(1,"Harish",85)
Student.count+=1
s1.display()
s1.result()

print(Student.count)