"""
If we want to store data but we also want to see the informantions about the data
in such a situtuation we use dictionary and key:value pair.

"""
monster_1={"name":"salvador","power":10,"color":"red"}
print(type(monster_1))

#we use the key value instead of index 
print(monster_1)

print(monster_1["name"])

#Adding new value to the dictionary
monster_1["position"]=75
print(monster_1)

#Getting None repsonse instead of key error when the element does not exist 
print(monster_1.get("boy"))

#to change the elemnets of the dictionary
monster_1.update({"name":"SALVADOR","power":100})
print(monster_1)

#erasing the elemnt of the dictionary
del monster_1["color"]
print(monster_1)

#printing the keys or the values of the dictionary
print(monster_1.keys())
print(monster_1.values())

#printing the keys and the values of the dictionary
print(monster_1.items())

#printing the keys values and key:value pairs with the for loop
for key in monster_1.keys():
    print(key)
print()
for value in monster_1.values():
    print(value)
print()
for item in monster_1.items():
    print(item)

#Using dictionaries in a list.Comma is important in a list.
my_friends=[
    {"name":"alperen","age":"24","gender":"male"},
    {"name":"gökçe","age":"22","gender":"female"}
]

print(my_friends[0]["name"])