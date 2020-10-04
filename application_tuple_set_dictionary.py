"""
creating empty list,tuple,set and dictionary

"""
list1=[]
list2=list()
print(type(list1),"\t\t", type(list2))

tuple1=()
tuple2=tuple()
print(type(tuple1),"\t", type(tuple2))

set1={}
#we can not create the empty set in such way 
set2=set()
print(type(set1),"\t\t", type(set2))

dictionary1={}
dictionary2=dict()
print(type(dictionary1),"\t\t",type(dictionary2))

"""
create a 3 elements dictionary with the integer values and print second element and mean of the values
"""

friends_age= {"alperen":24,"ahmet":36,"serkan":40}
print(friends_age["ahmet"])
print(sum(friends_age.values())/len(friends_age))

"""
my_dict={"odd_number":[1,2,3]}
take the square root of the values and update the dictionary

"""
my_dict={"odd_number":[1,3,5]}
my_dict["odd_number"]=[my_dict["odd_number"][0]**2,my_dict["odd_number"][1]**2,my_dict["odd_number"][2]**2]
print(my_dict)

"""
my_dict={"even_numbers":[2,4,6,8,10]}
take the square root of the values and update the dictionary

"""
my_dict={"even_numbers":[2,4,6,8,10,12,14]}
for k,v in my_dict.items():
    new_list=[]
    for value in v:
        new_list.append(value**2)
my_dict["even_numbers"]=new_list
print(my_dict)