
print("Hello World") #Print statement + comment

#declaring a variable
name = "Kj"
boolean = True

print("Hello " + name) #variable in print
print(f"Hello {name}") #f string

print("Hello"+" World") # string concatenation

print("Hello"*3) #string copy

#if - elif- else
if boolean:
    print(True)

else:
    print("False")

x = True if 1>0 else False  #conditional expression
print(x)
#typecasting
name = "Kj"
num = 19
floating = 18.9
boolean = True

print(f"Type of name is {type(name)}")
print(f"Type of num is {type(num)}")
print(f"Type of floating is {type(floating)}")
print(f"Type of boolean is {type(boolean)}")

print(f"{int(floating)}")

# Empty string to bool returns False

#input prompt
age = input("Enter ur age: ")

print(f"Age is {age}")

#math
#round(), abs(), max(), min()
#import math
#math.pi, math.e, math.sqrt

#logical Operators
# or, and, not

#while loop
count = 0
while count<5:
    count+=1
    print(count)

#for loop
for i in range(5):
    print(i)    # 0 based indexing

for i in range(0,10,2):     #start, stop, step
    print(i)                #stop not included, step can also be negative to count downwards

#string methods
name = input("enter a string: ")
print(f"The string is {len(name)} characters long")
print(f"the string has first o at {name.find('o')}") #find first occurence
print(f"The last o is at {name.rfind('o')}") #find last occurence

#print(help(str)) #shows all functions associated with string data type