"""
Write a function which returns the square root of a variable.

"""
def squareroot(x):
    return x**2

number=int(input("Enter a variable : "))

print(f"The value is {number} and square root is {squareroot(number)}")

#*************************************************************************
"""
Write a lambda which returns the multiplication of two variables.

"""
y=lambda x,k: x*k

x=int(input("Enter first variable : "))
k=int(input("Enter second variable : "))

print(f"The result of the multiplications of {x} and {k} is {y(x,k)}")

#*************************************************************************
"""
Write a function which return a multiplication of given list elemets.

"""
def multiply(mylist):
    result=1
    for x in mylist:
        result=result*x
    return result

my_list=[1,2,3,4,5,6]

print(multiply(my_list))

#*************************************************************************
