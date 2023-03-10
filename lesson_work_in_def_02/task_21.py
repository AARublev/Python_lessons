# работа с файлами

# 'a' - открытие для добовления данных
# 'r' - открытие для чтения данных
# 'w' - открытие для записи данных

# 'w+' 'r+'

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # текстовую переменную data связываем с файлом (если файла нет, то он создается)
data.writelines(colors) # writelines позволяет записать что-то в файл
data.write('\nLINE 2\n')
data.write('\nLINE 3\n')
data.close() # разрыв подключения файловой переменной с файлом написки (делается для избежания утечек памяти)

# другой вариант записи файлов:
# with open('file.txt', 'w') as data:
#     data.write('line123\n')
#     data.write('line2234\n')
# после завершения работы с этим блоком, произойдет разрыв связи,
# так что data.close() не нужен

exit() # позволяет не выполнить код после расположения данной функции