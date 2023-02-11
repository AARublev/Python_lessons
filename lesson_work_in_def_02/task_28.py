# Словари
# Неупорядоченные коллекции произвольных 
# объектов с доступом по ключу

dicionary = {}  # пустой словарь
dicionary = \
    {   
        'up': 'вверх',  # up - это ключ, 'верх' - значение по ключу
        'left': 'влево',
        'down': 'вниз',
        'right': 'вправо'
    }
print(dicionary)
print(dicionary['left']) # влево
# типы ключей могут отличаться

print(dicionary.keys()) # вывод ключей

for k in dicionary.keys():
    print(k)

for v in dicionary: # пробежались по всему словарю и получили только ключи
    print(v)

print(dicionary.values()) # вывод значений

for k in dicionary.values():
    print(k)

for v in dicionary: # пробежались по всему словарю и получили только значения
    print(dicionary[v])

# изменяем что-то в словаре по определенному ключу
dicionary['up'] = 'new values'

