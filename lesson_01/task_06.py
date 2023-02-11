# цикл while
# Цикл позволяет выполнить блок операторов какое-то количество раз

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# Управляющая конструкция: while-else
# while condition:
#     operator 1
#     operator2
#     ...
#     operator n
# else: # начинает работать после того как заканчиваетсыя while
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print("Пожалуй хватит!")
print(inverted)
