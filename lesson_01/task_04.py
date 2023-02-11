# Логические операции
# >, >=, >, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen


a = 1 > 4 or 5 > 2
print(a)

c = "qwd"
d = "qwd"
print(c == d)

e = [1, 2]
f = [1, 2]
print(e == f)

s1 = 1 < 3 < 5
print(s1)
s2 = 1 > 2 or 3 < 5
print(s2)

fun = [1, 2, 3, 4]
print(2 in fun)  # True т.к. 2-ка содержится в fun
print(not 6 in fun)

is_odd = not f[0] % 2  # проверка на четность. Вместо f[0] % 2 == 0
print(is_odd)
