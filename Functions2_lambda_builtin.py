"""
Built in functions are functions that are available in pyhton in advance
the print,set,min and max functions are examples  of them.

"""
#Examples of built in functions
my_list=[1,4,7,8,9]
print(len(my_list))
print(sum(my_list))
print(max(my_list))

#************************************************************************
"""
Lambda functions are used for small anonymous functions we do not use 
function name in such functions.We can use as many arguments as we want.
But lambda must be done single operation.

"""
y=lambda a : a**2
print(y(6))

addfive=lambda a: a+5
print(addfive(25))
print(addfive(36))

#We can use more than one variable

summation=lambda a,b: a+b
print(summation(6,7))

subtraction=lambda a,b: a-b
print(subtraction(7,6))
#************************************************************************
