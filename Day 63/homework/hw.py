#codewars
#1
def better_than_average(class_points, your_points):
    
    total = sum(class_points) + your_points
    all_students = len(class_points) + 1
    average = total / all_students
    return your_points > average

#2
def kata_13_december(lst): 
    # Fix this code
    for i in lst[:]:
        if i %2==0: 
            lst.remove(i)
    return lst

#3
def get_drink_by_profession(param):
    param = param.lower()  
    if param == "jabroni":
        return "Patron Tequila"
    elif param == "school counselor":
        return "Anything with Alcohol"
    elif param == "programmer":
        return "Hipster Craft Beer"
    elif param == "bike gang member":
        return "Moonshine"
    elif param == "politician":
        return "Your tax dollars"
    elif param == "rapper":
        return "Cristal"
    else:
        return "Beer"

#4
def square_sum(numbers):
    sum= 0
    for num in numbers:
        sum += num * num
    return sum

#5
def cookie(x):
    if type(x) == str:
        name = "Zach"
        
    elif type(x) == int or type(x) == float:
        name = "Monica"
    else:
        name = "the dog"
    return "Who ate the last cookie? It was " + name + "!"

