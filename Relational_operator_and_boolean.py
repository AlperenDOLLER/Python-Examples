#Python has another variable types which are boolean variables and true act as  1 and false act as 0 
bool1=True
bool2=False
print(type(bool1),bool1)
print(type(bool2),bool2)

a=2
print(a>bool1)
print(a<bool1)

"""
Relational operators
<       strictly less than
<=      less than or equal
>       strictly greater than
>=      greater than or equal
==      equal
!=      not equal
is      object identity
is not  negated object identity

"""
print(3<5)
print(3<=5)
print(3>5)
print(3>=5)
print(1==True)
print(1!=5)
print("1"!=1)

a=["ahmet","mehmet"]
b=["ahmet","mehmet"]

print(a==b)
print(a is b)
a=5
b=a
print(a==b)
print(a is b)

#And or not operators

print(32>28 and 17 <25)

print(32>28 or 17 >25)

print(not(32>28 and 17 <25))
