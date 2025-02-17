# Python Lists 

# 1
my_list = [1, 2, 3, 4, 5]
print("\nOriginal List:", my_list)

# 2
my_list.append(6)  
print("After Append:", my_list)

my_list.remove(3)  
print("After Removal:", my_list)

# 3
unsorted_list = [5, 3, 8, 1, 2]
unsorted_list.sort()
print("Sorted List:", unsorted_list)

# 4
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)

# 5
length = len(my_list)
print("List Length:", length)


#  Python If...Else 

# 1
num = 10
if num > 5:
    print("\nNumber is greater than 5")

# 2
num = 3
if num > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")

# 3
num = 0
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 4
num = 7
if num > 0:
    print("Positive number")
    if num > 5:
        print("Greater than 5")

# 5
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)


#  Python While Loops 

# 1
i = 1
print("\nWhile Loop:")
while i <= 5:
    print(i)
    i += 1

# 2
i = 1
print("While Loop with Break:")
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# 3
i = 0
print("While Loop with Continue:")
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 4
i = 0
print("Infinite While Loop Stopped:")
while True:
    print("Running...")
    i += 1
    if i == 3:
        break

# 5
my_list = ["apple", "banana", "cherry"]
i = 0
print("While Loop Iterating Over a List:")
while i < len(my_list):
    print(my_list[i])
    i += 1


#  Python For Loops 

# 1
print("\nFor Loop:")
for i in range(5):
    print(i)

# 2
fruits = ["apple", "banana", "cherry"]
print("For Loop Iterating Over a List:")
for fruit in fruits:
    print(fruit)

# 3
print("For Loop with Range:")
for i in range(1, 6):
    print(i)

# 4
print("Nested For Loop:")
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 5
print("For Loop with Else Clause:")
for i in range(3):
    print(i)
else:
    print("Loop finished")