# Реализуйте алгоритм перемешивания списка.

import random

print("Enter n: ")
n = int(input())

list = []
for i in range(n * (-1), n):
    list.append(i)
print(list)


def fun_random(originl_list):
    new_list = originl_list[:]  # copy
    list_lenght = len(originl_list)
    for i in range(list_lenght):
        index_aleatory = random.randint(0, list_lenght - 1)  # random index
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list


result = fun_random(list)
print(result)
