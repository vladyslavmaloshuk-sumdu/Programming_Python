def expression(a, b):
    if a > b:
        x = a * b + 1
    elif a == b:
        x = 25
    else:
        x = (a - 5) / b

    return x

a = int(input("Введіть a: "))

while a <= 0:
    a = int(input("Введіть додатне число a: "))

b = int(input("Введіть b: "))

while b <= 0:
    b = int(input("Введіть додатне число b: "))

print("Результат обчислення X =", expression(a, b))