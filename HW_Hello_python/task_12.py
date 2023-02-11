# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            result = not (x or y or z)
            result_two = not x and not y and not z
            if result == result_two:
                print('λ = (', x, y, z, '),', '¬(X ⋁ Y ⋁ Z)', '=', result, '==', 'λ = (', int(not x), int(not y), int(not z), ')', '¬X ⋀ ¬Y ⋀ ¬Z =', result_two)
            else:
                print('λ = (', x, y, z, '),', '¬(X ⋁ Y ⋁ Z)', '=', result, '!=', 'λ = (', int(not x), int(not y), int(not z), ')', '¬X ⋀ ¬Y ⋀ ¬Z =', result_two)
                

                

