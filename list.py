cities=["ankara","istanbul","eskişehir","izmir","afyon","mersin"]

print(cities)

"""
to print the n'th element of the list
the index of the list start at zero
"""
print(cities[2])

#the length of the list
print(len(cities))

#if we dont know the list length and we want to see last element or second last element
print(cities[-1])
print(cities[-2])

#to show the n'th elements of the list
print(cities[0:2]) #The same comment is print(cities[:2]) #not include the last n element print(cities[0:-n])

#to change the n'th element
cities[0]="adana"
print(cities)

#adding new element to the list
cities.append("bolu")
print(cities)

#add the new object to the specified location
cities.insert(2,"kütahya")
print(cities)

#delete the element in the specified index location .We cannot acces the element after we use the del comment
del cities[2]
print(cities)

#Delete with the list context
cities.remove("adana")
print(cities)

#to sort the list temporarily
print(sorted(cities))
print(cities)

#to sort the list in alphabetical manner #reverse of alphabetical manner cities.sort(reverse=True).this is permanet change
cities.sort()
print(cities)

number=[12,5,6,84,45]
print(min(number))
print(max(number))
print(sum(number))
print(sorted(number,reverse=True))