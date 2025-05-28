# 1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი 
# წინადადება და გასპლიტეთ სადაც იქნება “ა”.
def splitt():
    sentence = " მე ვარ პროგრამისტი და ვწავლობ გოას აკადემიაში."
    result = sentence.split("ა")
    return result

# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია. ეს სია უნდა იყოს სტრინგებით 
# სავსე. თქვენი მიზანია რომ ეს სია გაერთიანოთ და მათ შიგნით იყოს * სიმბოლო გაერთიანების დროს.

def join_function(words):
    return "*".join(words)

# codewars 

# 1)
def split_in_parts(s, part_length):
    result = ''
    for i in range(0, len(s), part_length):
        result += s[i:i+part_length] + ' '
    return result.strip()

# 2)

def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positive = 0
    negative= 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i

    return [positive, negative]

# 3)
def print_array(arr):
    list= []
    for i in arr:
        list.append(str(i))
    return ",".join(list)
