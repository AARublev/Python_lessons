# Строки
# help(text.institle) # модуль help вызываетсправку по функции

text = "съешь еще этих мягких французских булок"
# print(len(text))  # длина 39
# print("еще" in text)  # True # in для проверки наличие построки в строке
# print(text.isdigit())  # False # ф-ия для проверки явл ли все символы числами
# print(text.islower())  # True # ф-ия для проверки явл ли все символы строки символами нижнего регистра
# print(text.replase("еще", "ЕЩЕ"))  # ф-ия для замены одного на дргое

# for c in text:
#     print(c)

# Срезы:
print(text[0]) 
print(text[1]) 
print(text[len(text)-1]) 
print(text[-5]) 
print(text[:]) 
print(text[:2]) 
print(text[len(text)-2:]) 
print(text[0:len(text):6]) 
print(text[::6]) 
new_text = text[2:9] + text[-5] + text[:2] #...
print(new_text)





