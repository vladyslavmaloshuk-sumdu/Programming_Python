from module1 import calculate_y
from module2 import multiples_of_three


while True:
    print()
    print("Меню:")
    print("1 - Обчислити значення y")
    print("2 - Знайти числа, кратні 3")
    print("0 - Вийти з програми")

    choice = input("Виберіть функцію: ")

    if choice == "1":
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        x = float(input("Введіть x: "))

        y = calculate_y(a, b, x)

        print("Значення y =", y)

    elif choice == "2":
        numbers = multiples_of_three()

        print("Цілі числа, кратні 3, у діапазоні від 30 до 60:")
        print(*numbers)
        print("Кількість чисел =", len(numbers))

    elif choice == "0":
        print("Програму завершено.")
        break

    else:
        print("Помилка! Виберіть 1, 2 або 0.")