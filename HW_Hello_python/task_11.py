# 1. Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 => да
# - 7 => да
# - 1 => нет

print('Enter number: ')
a = int(input())

if a == 6 or a == 7:
    print(a, '=> YES')
elif a <= 0 or a > 7:
    print('Error. Enter natural number')
else:
    print(a, '=> NO')

