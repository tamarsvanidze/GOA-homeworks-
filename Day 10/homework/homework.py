 #პირველი დავალება

academy =input("which programming academy do you study?")

if academy == ("GOA"):
    print("you are right")
else:
    print("you made wrong decision")   

 #მეორე დავალება
price = int(input("how much is this item worth?"))
budget = int(input("what is your budget?"))

if budget >= price:
    print("you can buy this item")
else:
    print("you need"+ " "+ str(price -budget ) + " "+ "GEL to buy this item")

# მესამე დავალება    
num = int(input("plrase enter your number:"))
if num >= 5:
    print(num * 2 )
else:
    print(num * 4)  

 # მეოთხე დავალება   
ticket_price = 10
user = int(input("how many tickets do you want?"))
if user < 5:
    print(ticket_price * user)

else:
    print((ticket_price* 30/100)*user)


# მეხუთე დავალება
num1 = int(input("please enter your first number:"))
num2 = int(input("please enter your second number:"))
math_operator = (input("please enter witch operator do you want:"))
if math_operator == "*":
    print(num1 * num2)
elif math_operator == "/" :
    print(num1 / num2)
elif math_operator == "+" :
    print(num1 + num2)  
elif math_operator == "-" :
    print(num1- num2)  


