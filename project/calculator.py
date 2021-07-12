val1 = float(input())
val2 = float(input())
op = str(input())

if op == '+':
    print(val1 + val2)
elif op == '-':
    print(val1 - val2)
elif op ==  '*':
    print(val1 * val2)
elif op == 'pow':
    print(val1 ** val2)
elif op == 'mod':
    if val2 == 0:
        print("Деление на 0!")
    else:
        print(val1 % val2)
elif op == 'div':
    if val2 == 0:
        print("Деление на 0!")
    else:
        print(val1 // val2)
elif op == '/':
    if val2 == 0:
        print("Деление на 0!")
    else:
        print(val1 / val2)
else:
    print("Неизвестная операция!")