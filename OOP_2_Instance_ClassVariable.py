class Student:
    """
    We can add some properties which are same for every object we add such variable 
    to the class and named as class variables

    """
    school_name="X high school"
    number_of_student=0
    def __init__(self,name,age,grade):
        #The object that will be created has three attributes name age and grade.
        self.name=name
        self.age=age
        self.grade=grade
        #The below code written with Student because number_of_student is a class variable
        Student.number_of_student +=1
    def average(self):
        return sum(self.grade)/len(self.grade)
    
    def schoolName(self):
        # We can not write as f"The school name is {school_name}" because
        #we try to see the scholl name via object
        return f"The school name is {self.school_name}"


print(Student.number_of_student)
student_1=Student("Alperen",25,[80,75,95,100])
student_2=Student("Ali",26,[60,45,80,95])
print(Student.number_of_student)
print(student_1.average())
print(student_2.average())
student_1.name="Ahmet"
print(student_1.name)
print()

print(student_1.school_name)
print(student_2.school_name)
print(Student.school_name)

print()
print(student_1.schoolName())
#The values and properties of a class or object can be printed as follow.
print(student_1.__dict__)
#print(Student.__dict__)

