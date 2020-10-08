"""
Loops give an advantage for doing same job more than once.
So we do not need to write same statements for same operations.

In general while loop used for doin some operations
when the conditions are  safisfied.

"""
number=1
while(number<=10):
    if(number==10):
        print(number)
    else:
        print(number,end="-")
    number+=1


#****************************************************************
message=""

while(message!="quit"):
    message=input("Enter the massage you can exit with quit message:  ")
    print(message)

#You must be aware of upper lower case Quit does not provide exit operation.
#We can also made same operation above with flag.
my_flag=True
message=""
while(my_flag):
   
    message=input("Enter the massage you can exit with quit message:  ")
    if(message=="quit"):
        my_flag=False
    else:
        print(message)


#****************************************************************
"""
while(5>3):
    print("5 greater than 3 ")

#You can quit the infinite loop with ctrl+c
"""
#****************************************************************
#Using break comment
num1=1
while(num1 <= 10):    
    print(num1,end="-")
    if(num1==5):
        break
    num1+=1
#when the program recognize break command it exit from loop
print()
#****************************************************************
#Using continue comment
number1=1
while(number1<10):    
    number1=1+number1
    if((number1 % 2)==0):
        continue

    print(number1,end="-")
#when the program recognize continue command it pass that condtion
#****************************************************************    

