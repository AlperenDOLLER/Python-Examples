"""
Functions are usde for divede the written code as parts.
They are responsible of some task which will be repeated in the code block.
They are two types of functions built in functions(which the program has 
this functions in advance) user define functions(which the user specify
and write for specific task)

"""

#def is the key word to create a function.
#func is user defined name.It is function name

def func():
    print("Hello World")

func()
print()
#************************************************************************

#Generaly functions are used for dynamic operations and gets arguments when it is called.
#The username called :parameter and Alperen is : argument
def my_function(username="User"):
    print(f"Hello {username}")   

"""
When the function is called without argument the error is occur
to avoid this we can use default assignment for parameter

"""
my_function()
#Argument has priority to the default value
my_function("Alperen")
my_function("Ramiz")

print()
#************************************************************************

def my_function1(username="User",age=25):
    print(f"Hello {username} your age is {age}")   

my_function1("Alperen")
my_function1("Ali",28)

print()

#************************************************************************
#Functions can return something
def func1():
    return 5+10

def func2():
    print(10+6)

result=func1()
print(f"The first function returns {result}")
"""
First function return integer 15 but it was not used any where to use the 
return function we must assign some variable and used it.
"""
func2()
#Second functions directly print the result in function block

print()
#************************************************************************
#Brackets must be used to run the functions if we dont use it it returns
#the address of the function