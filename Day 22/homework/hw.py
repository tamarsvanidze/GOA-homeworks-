# python syntax
print("Hello world !")

name = input("what is your name? ")
print(name)

# this is single line comment
"""
this is multi line comment
written more then one line
"""

for i in range(10):
    print(i)

# how to  make line break
print("hello\nworld")  #this will output hello world on diferent line
print(4 + 7)# this is rigth
#print(4 + "you") # that is wrong because we can not add strin a intenger
print("goa" + "academy")# this is rigth

name = "tako" # this is type of string
age = 15 # this is type of intenger
heigth = 156.9 # this is float

# swap variables
num1 = 4
num2= 7
temp = num1
num1 =num2
num2 = temp
print("the value of num1 after swapping:{}" . format(num1))
print("the value of num2 after swapping:{}" . format(num2))

#local variable 
name1 = "my name is tako"
print(name1)

# variable naming
# 1 variable can contain only letters, numbers and underscores.
hello123 = 67 # not error
#hello&*% = 67 # error
# 2 varable can start with a lrtter or underscore but not with a number
#spaces can not be allowed in variable

# python data types
intenger = 5
string = "hello"
float = 23.0
boolian = True

print(type(intenger))
print(type(string))
print(type(float))
print(type(boolian))

print(6 / 12.7) #aritmetic operations on different data types
print(144 // 12)
print(5.7 % 2)
print(67 * 5)

print(5 > 6.0)
print(7 == 7.0)
print(56 < 43.8)
print( 32 != 65.8)
print(8 >= 5.5)

# python numbers
# aritmetic operations
print(5 * 87) 
print(12 / 3)
print(22 // 7)
print(56 % 8)
# random number
import random
print(random.randrange(1,10))

 # square root

n =int(input("enter a number: "))
sr=n ** 0.5
print(sr)

import math

x= 4.5
result = math.floor(x)
print(result)

import math

x= 7.3
result = math.ceil(x)
print(result)

#python casting
#numm = float(5) # numm will be 5.0
m =int("5") # m will be 5

list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8,9]
tuples = tuple(list)

#print(int("tako")) #this is error cuz string with letters can not be integer

# python booleans
print(5 > 6) # it is false
print(7 == 7)# its true
print(56 < 43) #it`s false
print( 32 != 65)#it is true
print(8 >= 5)# it is true

print(15 == 14 and 18 > 15) # this will be false bc false and true will be false
print(65>=54 and 12 == 12) # this will be true bc true and true will be true
print(9 > 18 or 83 < 9) # this will be false bc false or false will be false
print(18 >= 2 or 49 < 17)#this will be true bc true or false will be true

if  100 >= 67:
    print(True)
else:
    print(False)

#python operators
#aritmetic operators
y = 2+ 5
z= 3 *9
w = 4 / 2
e = 7// 3
a = 76 % 6
p = 4 -2

# assigment operators
y = 6
y += 3
print(y)

y = 6
y -= 3
print(y)

y = 6
y *= 3
print(y)


y = 6
y /= 3
print(y)

y = 6
y %= 3
print(y)
#comparison operators
num3= 7
num4=8
print(num3 > num4)
print(num3 < num4)
print(num3 == num4)
print(num3 != num4)
print(num3 >= num4)
print(num3 <= num4)
 #logical operators
print(y > 4 and y == 6) # this is false
print(y != 7 or y > 67)# this is true

v = ["banana", "peach"]
c=["banana", "peach"]

o = v
print(v is o) # this will be true bc o is the same object as v
print(v is y) # this will be false
print(v is not o)#thiswill be false bc they are smae objects

# pythom lists
my_list = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]
print(my_list)
list1 = ["apple", "banana", "peach"]
list1.append("lemon")
list1.remove("banana")
print(list1)
list2 = ["teacher ", "student", "parent", "director"]
list2.sort()
print(list2)
fruits = [ "mango", "cherry", "kiwi", "apple", "banana"]
new_list = [ x for x in fruits if "a" in x]
print(new_list)
print(len(new_list))
# python if else

academy =input("which programming academy do you study?")

if academy == ("GOA"):
    print("you are right")
else:
    print("you made wrong decision") 

score= int(input("please enter your exem score: "))     
if score >= 85 and score <= 100:
    print("100% grant")
elif score>=55 and score< 85:
    print("70% grant")
elif score>= 35 and score<55:
    print("you didnot get grant")
else:
    print("you did not pass the exem")
# python while loops
results = 0
i = 0
while i <= 50:
    results += i
    i = i + 5

print(results)

i =1
while i < 8:
    print(i)
    if i == 4:
        break
    i += 1

i =1
while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)

num_list = [1, 2, 3, 4, 5, 6, 7, ] 
index = 0
while index < len(num_list) :
    print(num_list[index]) 
    index += 1
# python for loops

cars= ["bmw", "tesla", "ford", "porsche", "ferrari"]
for i in cars:
    print(i)
# interate over a list
listt = [7, 6, 5, 4, 9, ]  
for i in listt:
    print(i)  
# using range()  
for i in range(1,10) :
    print(i) 

# for loop with an else clause
for i in range(1, 20):
    print(i)
else:
    print("no break")   

#python funtions
def function():
    print( "this is a function") 

function()
# using parametrs
def greeting(name):
    print("hello my dear friend" + name)     
    
     

