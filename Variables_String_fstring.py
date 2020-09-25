
my_string="Alperen's first example "

#We add the first string to the second string

#my_another_string="Hello world "+my_string

my_another_string=f"Hello world {my_string}"

""""
*The above line can also done by using f'str'comment : my_another_string=f"Hello world {my_string}"

*The above line can also done by using print(my_another_string.format(my_string)) 
but second string must be configured my_another_string="Hello world {}"

"""

print(my_another_string)

