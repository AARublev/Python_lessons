# списки

list1 = [1, 2, 3, 4, 5]
list2 = list1
list1[0] = 123 # меняет значение в 2-х списках 
list2[1] = 345 # еняет значение в 2-х списках 

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

# удаление элементов в списке
print('delete (.pop)')
print(list1.pop())
print('len = ', len(list1))
print(list1)
print()
print(list1.pop())
print('len = ', len(list1))
print(list1)

# удаление конкретных элементов в списке
print()
print(list1.pop(1))
print(list1)

# вставить элемент на нужную позицию
print()
print(list1.insert(1, 21))
print(list1)
print(list1.append(999)) # добавление в конец
print(list1)