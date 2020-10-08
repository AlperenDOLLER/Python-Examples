"""
Specified operations must be than in some situtiaons 
so the "if" command specify that
We can specify some conditions for some operations that must done.

"""

#***************************************************************
my_list=["ahmet","mehmet","ali"]

if ("ahmet" in my_list):
    print("ahmet is in the my_list ")

#***************************************************************
age1=int(input("Enter your age in numerical form : "))

""""
There must be one tab space after the  
if command to specifty that the written code lines in if clause 
"""

if(age1 >=18):
    print("You can vote ")
else:
    print("You can not vote ")

#****************************************************************

age2=int(input("Enter your age in numerical form : "))

#We can more elif conditions
if(age2<=2):
    print("%80 discount ")
elif(age2<=10):
    print("%50 discount")
else:
    print("No discount ")

"""
Every integer return true except 0.
Empty list return false.
None returns false.
Empty tuple returns false.


"""

my_condition=[]
if(my_condition):
    print("The condition satisfied ")
else:
     print("The condition does not satisfied ")

my_condition={}
if(my_condition):
    print("The condition satisfied ")
else:
     print("The condition does not satisfied ")

my_condition=5
if(my_condition):
    print("The condition satisfied ")
else:
     print("The condition does not satisfied ")
