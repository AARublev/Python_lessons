# patch = 'file.txt' # создали путь
# data = open(patch, 'r') # открыли в режиме чтения
# for line in data:
#     print(line) # читаем все строки
# data.close()


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    elif x == 'we':
        return 'Строка'
    else:
        return