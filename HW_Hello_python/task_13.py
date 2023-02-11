# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Ender X: ")
x = int(input())
print("Ender Y: ")
y = int(input())

if x == 0 or y == 0:
    print("origin or coordinate axis")
elif x > 0 and y > 0:
    print(("{}{}{} {}{} {} {}".format("x=", x, ";", "y=", y, "->", "1")))
elif x < 0 and y > 0:
    print(("{}{}{} {}{} {} {}".format("x=", x, ";", "y=", y, "->", "2")))
elif x < 0 and y < 0:
    print(("{}{}{} {}{} {} {}".format("x=", x, ";", "y=", y, "->", "3")))
else:
    print(("{}{}{} {}{} {} {}".format("x=", x, ";", "y=", y, "->", "4")))
