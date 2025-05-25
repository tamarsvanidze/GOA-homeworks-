# 1)ექმენით ცვლადი საცად შეინახავთ ერთ მთლიან წინადადებას,თქვენი 
# დავალება არის აქციოთ ეს წინადადება სიად სადაც მოთავსებული იქნება თითოეული სიტყვა 

sentence = "GOA is the best academy"
words_list = sentence.split() 
print(words_list)

#2)შექმენი სია სადაც მოთავსებული გექნება სტრინგები,შენი დავალებაა
#  ეს სია აქციო ერთ მთლიან წინადადებად(სტრინგად) და თითოეული სიტყვა
#  დაშორებული იყოს ერთმანეთისგან სფეისით

words = ["GOA", "is", "the", "best", "programming", "academy"]
sentence = " ".join(words)  
print(sentence)


#3)შექმენით წინადადება სადაც სიტყვები ერთმანეთისგან დაშორებული იქნება # -ით,თქვენი დავალებაა აქციოთ 
# ეს წინადადება სიად და სიიდან ისევ სტრინგად მაგრამ 
# სიიდან სტრინგად გადაქცევის დროს სიტყვები ერთმანეთისგან დაშორებულები იყვნენ $ -ით

sentence = "goa#is#the#best#academy"
list = sentence.split("#")  
new_sentence = "$".join(list)  
print(list)
print(new_sentence)

# codewars

# 1)
def vaporcode(s):
    result = ""
    for i in s:
        if i != " ":
            if i >= 'a' and i <= 'z':
                capital = chr(ord(i) - 32)
            else:
                capital = i
            result += capital + "  "
    return result.strip()

# 2)
def abbrev_name(name):
    i = 0
    while name[i] != ' ':
        i += 1
    first = name[0]
    second = name[i + 1]

    if 'a' <= first <= 'z':
        first = chr(ord(first) - 32)
    if 'a' <= second <= 'z':
        second = chr(ord(second) - 32)

    return first + '.' + second

