name="alperen software"

#The length of the string  
print(len(name))

#To sperate the print function with one line below print added 
print("")

#The x'th character of string 
print(name[0])

#Writing the specified length of string.The  print(name[:7]) comment same as below code
print(name[0:7])

"""
The mehods of the string.

"""
#Making the upper case  first letter of every single word 
print(name.title())
#Making the upper case  of every single word 
print(name.upper())
#Making the lower case  of every single word 
name="ALPEREN SOFTWARE"
print(name.lower())
#Count the the number of character which specified by writer
print(name.count("A"))
#find the the index of specified character
print(name.find("A"))
#Replace the specified word
print(name.replace("SOFTWARE","PROJECT"))

"""
We do not need to memorize all of these methods
python help us to find such methods with below comment
"""

print(dir(name))
#print(help(str))

#To learn the method 
print(help(str.count))
