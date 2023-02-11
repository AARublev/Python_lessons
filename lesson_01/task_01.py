# тип данных переменная
# int, float, boolean, str, list,  None
# type -  позволяет узнать тип данных

value = None  # присвоить "пустое" значение для дальнейшего использования
print(type(value)) # тип NoneType
a = 123
b = 1.23
print(type(a)) # функция type для того чтобы узнать тип данных
print(type(b))
value = 12334.2
print(type(value))
s = 'Hello world'
print(s)

print(a, b, value, "--", "string")
print("{} - {} - {}".format(a, b, value)) # формат
print("\n")
print(f"{a} - {b} - {value}")  # итнтерполяция
print("\n")
print("{1} - {2} - {0}".format(a, b, value))  # изменение порядка

f = True  # Логические переменные
t = False
print(f, t)

list = [1, 2, 3]  # список (массив), list = [] - пустой список
liststr = ["string_1", "string_2", "string_3"]  # список строк
print(list, "\n", liststr, "\n", 10, 22)
