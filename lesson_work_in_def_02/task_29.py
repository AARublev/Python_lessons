# Множества

colors = {'red', 'green', 'blue'} # некое множество
print(colors)

colors.add('red') # добавление значения, но оно не добавиться т.к. это значение в мн-ве уже есть
print(colors) # {'red', 'green', 'blue'}
colors.add('gray') # добавление значения
print(colors) # {'red', 'green', 'blue', 'gray'}

colors.remove('red') # удаление значения
print(colors) # {'green', 'blue', 'gray'}

colors.discard('red') # удаление значения которого нет в мн-ве, но ошибку программа не выдаст
print(colors) # {'green', 'blue', 'gray'}

colors.clear() # очистить мн-во
print(colors) # {}

a = {1, 2, 3, 5, 8}
b = {2, 5, 8 ,13, 21}
c = a.copy() # создаем комию мн-ва
u = a.union(b) # объеденение {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # пересечение i = {8, 2, 5}
dl = a.difference(b)    # dl = {1, 3}
dr = b.difference(a)    # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a) # неизменяемое мн-во (замороженное мн-во)