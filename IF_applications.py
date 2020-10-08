"""
Decide the entered value was even or odd number.

"""
num1=int(input("Please enter an integer :  "))

if(num1%2==0):
    print(f"{num1} is an even  number ")
else:
    print(f"{num1} is a odd  number ")

"""
We can write above code lines in a line.
print(f"{num1} is an even  number ") if(num1%2==0) else print(f"{num1} is a odd  number ")

"""

#************************************************************

"""
Find the factorial of the any number entered by user.

"""
num2=int(input("Please enter an integer :  "))
result=1

if(num2<0):
    print(f"{num2} is a negatif number ")

elif(num2==0):
    print(f"The factorial of the {num2} is {result} ")

else:
    for x in range(1,num2+1):
        result=result*x
    print(f"The factorial of the {num2} is {result} ")


#************************************************************

"""
Print pass for  students who has grade greater than  or equal to  .
Print fail for students who has grade less than 50.

"""
students={"ahmet":58,"mehmet":78,"ebru":44,"pınar":90}

for key,value in students.items():
    if(value>=50):
        print(f"{key}  pass the exam  and the note is {value} ")
    else:
        print(f"{key}  fail the exam and the note is {value} ")


#************************************************************