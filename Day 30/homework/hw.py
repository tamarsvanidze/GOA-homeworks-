# პირველი დავალება
def num():
    num1 = int(input("enter your number; "))
    if num1 % 2 == 0 :
        print("this number is even")
    else:
        print("this number is odd") 

num()  
# მეორე დავალება
def number():
    num1 = int(input("enter your number; "))
    if num1 > 0 :
        print("this number is  positive")
    else:
        print("this number is  negative") 

number() 

#მესამე დავალება

def num2():
    num1 = int(input("enter your number; "))
    if num1 % 5 == 0 :
        print("this number is multiple of five")
    else:
        print("this number is not ultiple fo five") 


num2()

# მეოთხე დავაება

def user_age():
    age = int(input("enter your age; "))
    if age > 18 :
        print(" user is adult")
    else:
        print("user isnot adult") 

user_age()

#მეხუთე დავალება


def num3():
    num = int(input("enter your number; "))
    print(num *num)

num3()

#მეექვსე დავალება


def password():
    code = input("enter your password:")
    if len(code) == 8:
        print("registration get well")
    else:
        print(" try again ,password must be 8 simbols long") 

password()

# მეშვიდე დავალება

def num4():
    numbers = []
    for i in range(10):
        number = 0
    while number > 0:
        number = int(input("enter the number: "))
    numbers.append(number) 
    

    print(numbers)

num4()
          

    