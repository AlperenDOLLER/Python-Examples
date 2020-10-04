#If we want to list not to be changeable the tuple type provide this.Tuple is unchangeable list.

capitals=("ankara","tahran","madrid","tiflis")
print(type(capitals))
print(capitals)
print(len(capitals))

#tuple elements have index
print(capitals.index("tahran"))
print(capitals[-2:])

#We can't change elements of the tuple but we can change whole tuple
print(capitals)
capitals=("berlin","roma","brusesels")
print(capitals)

#to the specified element in tuple or not
print("berlin" in capitals)

"""
Set elemenets are out of order.The elements does not have index
The elements of set can be just once we can not add same element to the set 

"""

cities={"izmir","ankara","eskişehir","kars","istanbul","eskişehir"}

print(type(cities))

#There are two eskişehir but set does not show one of them 
print(cities)

#adding new element to the set
cities.add("gaziantep")
print(cities)

#adding more one  new elements to the set
cities.update(["edirne","kars"])
print(cities)

#removing specified element
cities.remove("kars")
print(cities)