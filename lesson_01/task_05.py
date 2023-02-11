# Управляющие конструкции (операторы ветвления)
# if, if-else

# if condition:
#     operator 1
#     operator 2
#     operator 3
#     ...
#     operator n
# else:
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m

# print('enter num A:')
a = int(input("a = "))
# print('enter num B:')
b = int(input("b = "))
if a > b:
    print(a)
else:
    print(b)

# if в связке с блоком elif
# if condition1:
#     operator
# elif condition2:
#     operator
# elif condition3:
#     operator
# else:
#     operator

username = input("Enter name: ")
if username == "Masha":
    print("Ok, she is Masha")
elif username == "Marina":
    print("I wos waiting for you, Masha")
elif username == "Ilnar":
    print("Ilnar is very good!")
else:
    print("Hello", username)
