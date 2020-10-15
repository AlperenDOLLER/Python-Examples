"""
instance methods , class methods and static methods 

"""

class Student :
    school_name="X high school"
    number_of_students=0

    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
        #Class variable will be used so before the variable Student must be used.
        Student.number_of_students +=1
    #The instance method takes parameter self to specify the object that will be used.
    def average (self):
        return sum(self.grades)/len(self.grades)
    
    #The class method specified with @classmethod and takes parameter cls for specify the class.
    @classmethod
    def display_school_name(cls,name_of_school):
        cls.school_name=name_of_school
    
    #The static method specified with @staticmethod and takes no parameter .
    #The static method does not change any variables of class or objects.
    @staticmethod
    def stc():
        return f"The message"

#Change the class variable with a class method
print(Student.school_name)
Student.display_school_name("Y High school")
student_1=Student("Mahmut",33,[14,26,72,84])
student_2=Student("Ayşe",35,[40,55,65,85])
print(Student.school_name)
print(student_1.average())
print(student_2.average())
#We can change the specific object class variable but change occur onlt that variable.
student_1.school_name="Z High School"
print(Student.school_name)
print(student_1.school_name)
print(student_2.school_name)
print(Student.stc())
print(student_1.stc())