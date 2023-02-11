# Списки.
# Список - пронумерованная, изменяемая коллекция объектов

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1,2,3,4,5]
print(type(numbers))  # изначальный тип list

ran = range(1, 6)  # range списокм не является
print(type(ran))  # имеет тип range
numbers_2 = list(ran)  # приведение типа range к типу list
print(type(numbers_2))

numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
print(f"{len(numbers)} len")  # получить кол-во элементов через интерполяцию

for i in numbers:
    i *= 2
    print(i)  # [20, 4, 6, 8, 10]
print(numbers)  # [10,2,3,4,5] #Внимание! список при этом не изменится
# Нужно создать новый список

# РАСШИРЕННЫЙ ФУНКЦИОНАЛ РАБОТЫ СО СПИСКАМИ

colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # либо так: del colors[0] # удалить элемент