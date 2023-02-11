# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("Ender qarter number: ")
coord = int(input())

if coord > 4 or coord < 1:
    print("Error!")
elif coord == 1:
    print("x = (0, +∞) and y = (0, + ∞)")
elif coord == 2:
    print("x = (-∞, 0) and y = (0, + ∞)")
elif coord == 3:
    print("x = (-∞, 0) and y = (-∞, 0)")
else:
    print("x = (0, +∞) and y = (-∞, 0)")
