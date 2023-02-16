# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

print('Enter number: ')
a = float(input())

# q=10123
# i=0
# while a != 0:
#     a = a%q
#     a = round(a)
#     q*10
#     i+=a
# print(i)

# q=10
# a = a%q
# a = round(a)
# #q*10
# #i+=a
# print(av)

print(a/10)
print(a//10)
print(round((a/10 - a//10)*10))