num = int(input("please enter whole number:"))
for i in range(0,num + 1):
    print(i)

count_numbers = int(input("please enter how many numbers do you want to input: "))
sum_numbers = 0

for i in range(1, count_numbers+1):
    sum_num =int(input("please enter number" + str(i)+ ": "))
    sum_numbers = sum_numbers + sum_num
    
print(sum_numbers)


result = 0
i = 0
while i <= 20:
    result += i
    i= i+2
  
print(result)        

      