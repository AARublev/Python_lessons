# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

print("enter n: ")
n = int(input())

newlist = []
for i in range(1, n + 1):
    S = round((1 + 1 / i) ** i, 2)
    newlist.append(S)
print(newlist)
