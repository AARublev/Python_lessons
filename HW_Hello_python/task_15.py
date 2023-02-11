# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from cmath import sqrt
import math

print("Enter X for 1: ")
x1 = int(input())
print("Enter Y for 1: ")
y1 = int(input())

print("Enter X for 2: ")
x2 = int(input())
print("Enter Y for 2: ")
y2 = int(input())


result = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

print(result)
