"""
For loops generaly used for acces to data in data stream or loops for 
specified number of turns

"""
numbers=[3,7,5,11]
print(numbers[0])
"""
we can print the elements of the list above way but if the list is to long
we must use loops for effective programming

"""
for number in numbers:
    print(number)

print()
#*************************************************************************
friends={"ahmet","ali","ayşe","adem"}
for friend in friends:
    print(friend)

print()

#**************************************************************************
my_string="alperenprojects"

for letter in my_string:
    print(letter.upper(),end=" ")

print()
#**************************************************************************
#To done some jop in range of specified number.10 does not included
for x in range(2,10):
    print(x,end=" ")

print()
#We can also specified the step size
for x in range(0,10,2):
    print(x,end=" ")

print()
print()
#**************************************************************************
friends={"ahmet":45,"ali":35,"ayşe":28,"adem":26}

for friend in friends.keys():
    print(friend)
print()   
for friend in friends.values():
    print(friend)
print()
for key,value in friends.items():
    print(key,value)

print()

#**************************************************************************
#Break and continue command in for loops
friends={"ahmet":45,"ali":35,"ayşe":28,"adem":26}

for friend in friends.keys():
    if(friend=="ayşe"):
        break
    print(friend)
print()   

for friend in friends.keys():
    if(friend=="ayşe"):
        continue
    print(friend)
print() 
#**************************************************************************
#Enumarete used for the writing index in the loop
friends=["ahmet","ali","ayşe","adem","tarık","serkan","fatma"]

for i,friend in enumerate(friends):
    print(i,friend)

#**************************************************************************