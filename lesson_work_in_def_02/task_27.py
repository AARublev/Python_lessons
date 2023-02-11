# Кортежи
# Кортеж - это неизменяемый "Список"

# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple, обязательно ставить ',' для одного э-та
# t = (1)
# print(type(t))  # int, не явл кортеджем
# t = (28,9,1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)   # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)        # ('red', 'green', 'blue')

# a, b = 3, 4
# or
a = (3, 4, 5, 342)
print(a[0])  # 3
print(a[-1]) # 342

# a[0] = 12 # в списках работает, но не в кортеджах. кортедж неизменяемый

for item in a:  # цикл for перебирает кортедж
    print(item)

# Можно распоковать котедж в отдельные переменные

t = tuple(['red', 'green', 'blue']) # создали список и потом конвертировали его в кортедж
red, green, blue = t # распаковываем
print('r:{} g:{} b:{}'.format(red, green, blue)) # дальше работаем как с отдельными, независимыми переменными
# r:red g:green b:blue