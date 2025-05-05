#codewars

#1
def greet(name):
     return "Hello, " + name + " how are you doing today?"

#2
def litres(time):
    return time // 2

#3
def better_than_average(class_points, your_points):
    
    total = sum(class_points) + your_points
    all_students = len(class_points) + 1
    average = total / all_students
    return your_points > average

#4
def invert(lst):
    result = []
    for i in lst:
        result.append(-i)
    return result

#5
def minimum(arr):
    return min(arr)

def maximum(arr):
     return max(arr)