# Codewars

# 1)
def is_opposite(s1,s2):
    if s1=="" and s2=="":
        return False
    a = s1.swapcase()
    
    if a == s2:
        return True
    else:
        return False
    

# 2)
def check_alive(health):
    if health > 0:
        return True
    else:
        return False  
    

# 3)

def count_char_occurrences(strng, char):
    count =0
    for i in strng:
        if i == char:
            count += 1
    return count  

# 4)
def remove(st):
    str = ""
    for i in st:
        if i != "!":
            str += i
        
        
    return str + "!"

# 5)
def array_diff(a, b):
    list = []
    
    for i in a:
        if i not in b:
            list.append(i)
            
    return list
    