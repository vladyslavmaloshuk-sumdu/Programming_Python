sentence = input("Введіть речення: ")

words = sentence.split()

if len(words) < 7:
    print("Помилка: речення повинно містити щонайменше 7 слів.")
else:
    words[0], words[-1] = words[-1], words[0]

    print("Речення після заміни першого та останнього слів:")
    print(" ".join(words))