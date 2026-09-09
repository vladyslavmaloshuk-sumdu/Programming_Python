def expression(a, b):
    if a > b:
        x = a * b + 1
    elif a == b:
        x = 25
    else:
        x = (a - 5) / b

    return x


def pyramid(n):
    for i in range(1, n + 1):
        print("  " * (n - i), end="")

        for j in range(i, 0, -1):
            print(j, end=" ")

        print()

    for i in range(1, n):
        print("  " * i, end="")

        for j in range(1, n - i + 1):
            print(j, end=" ")

        print()


a = int(input("Введіть a: "))

while a <= 0:
    a = int(input("Введіть додатне число a: "))


b = int(input("Введіть b: "))

while b <= 0:
    b = int(input("Введіть додатне число b: "))


print("Результат обчислення X =", expression(a, b))


n = int(input("Введіть N від 1 до 10: "))

while n < 1 or n > 10:
    n = int(input("Помилка! Введіть N від 1 до 10: "))


print("\nПіраміда:")
pyramid(n)