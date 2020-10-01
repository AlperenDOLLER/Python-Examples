cities=["tahran","barcelona","semerkand","napoli"]

#to learn the index of the specified context.if the context does not in the list the error occur
print(cities.index("semerkand")) #print(cities.index("ankara"))

#to check the specified context is in the list or not .The comment return boolean True or False
print("kayseri" in cities)
print("tahran" in cities)

#converting string to the list

numbers="one,two,three,four,five"
print(numbers)
my_list=numbers.split(",")
print(my_list)

#the for loop.The space before the experresions in the loop is important if we do not put that space python does not add the comment

for city in cities:
    print(f"The city I want to visit : {city} ")
print("You are  out of the for loop ")  # this comment printed after the for loop because it is not in the loop

#print the number 1 to 9 with the help of for loop
for number in range(1,10):
    print(number)
#Or in the list
number=list(range(1,11))
print(number)

#Even numbers between 1 and 20
number=0
print()
for number in range(2,21,2):
    print(number)