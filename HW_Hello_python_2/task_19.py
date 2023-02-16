# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле task_19.txt в одной строке одно число.

print("num N:")
n = int(input())

newlist = []
for i in range(n * (-1), n + 1):
    newlist.append(i)
print(newlist)

task_19 = open("task_19", "w")
task_19.write(str(newlist))
task_19.close
