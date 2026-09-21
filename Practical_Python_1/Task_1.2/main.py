def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) +
              " ".join(str(j) for j in range(i, 0, -1)))

    for i in range(n, 0, -1):
        print(" " * (n - i) +
              " ".join(str(j) for j in range(1, i + 1)))


n = int(input("Введіть N від 1 до 10: "))

while n < 1 or n > 10:
    n = int(input("Помилка! Введіть N від 1 до 10: "))

print("\nРомб:")

pyramid(n)