"""
*We can think that ecery physical thing as a object.Such as car,book ,dictionary etc.

*We say attribute when the object has properties the color ,model or age can be attribute of an object in car class.

*Functions that objects can do are called method.

*We use classes as a template of  objects that will be created.

*For example we have car class and the object is special brand car such as BMW


"""
class Car:
    #When we have a function in a class we named as  method  def __init__() is a method.
    def __init__(self ,brand ,model ,year):
    #When a object is created the __init__ method directly works and do some opetaions inside of the method.
    #It used for the initialize the created object.
        self.brand=brand
        self.model=model
        self.year=year
    #We use self parameter to specify the object which created at that time.
    def brandmodel(self):
        return f"The car brand {self.brand} and model of the car {self.model}"


#When the object is created from a class it is named as instantiation and object is called instant.

car_1=Car("BMW","i5","2015")
car_2=Car("Audi","x6","2018")
print(car_1.brand)
print(car_2.year)
print(car_1.brandmodel())
#*****************************************************************************************************************************
class Movie:
    def __init__(self,name,director):
        self.name=name #It can be written  self.alperen=name but to be clear we use parameter name.
        self.director=director


movie_1=Movie("Full Metal jacket","Kubrick")
movie_2=Movie("Babel","Irrarutu")
print(movie_1.director)
print(movie_2.director)

#*****************************************************************************************************************************