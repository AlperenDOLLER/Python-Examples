"""
When subclass was created from parent class it takes all opportunities of
parent class.

"""

class Student :       
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    
    def average(self):

        return sum(self.grades)/len(self.grades)


student_1=Student("Alperen",25,[84,95,75,100])
student_2=Student("Ali",30,[95,85,70,90])
#When the sub class created the all properties of parent class linking directly with it.

class UniversityStudent(Student):
    
    def __init__(self,name,age,grades,university):
        #We say the compiler to take name, age and grades parameters from parent class.
        super().__init__(name,age,grades)
        self.university=university
        
    

u_student_1=UniversityStudent("Fatma",26,[85,65,75,95],"Esogu")

"""
We can access the parent class parameter with subclass 
but we can not access subclass parementer with parent class.

We can not create instance as below.
student_1=Student("Alperen",25,[84,95,75,100],"ODTU")

"""

print(u_student_1.university)
print(u_student_1.average())




