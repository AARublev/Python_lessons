# Управляющая конструкция for 

# for i in enumeration: #(счетчик)
#     operator 1
#     operator 2
#     ...
#     operator n 

for i in 1,2,3,4,5:
    print(i**2)
print('\n')
list = [1,2,3,4,5]
for i in list:
    print(i**3)

r = range(10) # создаем объект range
for i in r:   # range выдает набор или итератов от 0 до 10
    print(i)

# Другой вариант:
# for i in range(10):
#     print(i)

print('\n')
for i in range(2, 4): # 4 не включает
    print(i)

print('\n')
for i in range(1, 10, 2): # получаем нечетные числа от 1 до 9
    print(i)

print('\n')
for i in 'qwerty': # итерация строк
    print(i)

