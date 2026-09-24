teams = {
    "Динамо": 27,
    "Шахтар": 24,
    "Зоря": 21,
    "Ворскла": 18,
    "Полісся": 16,
    "Карпати": 14,
    "Олександрія": 12,
    "Колос": 9,
    "Чорноморець": 6
}


def print_teams(teams):
    print("\nСписок команд:")
    for team in teams:
        print(team, "-", teams[team], "балів")

def add_team(teams, team, points):
    if team in teams:
        print("Помилка! Така команда вже існує.")
    else:
        teams[team] = points
        print("Команду", team, "додано.")

def delete_team(teams, team):
    if team in teams:
        del teams[team]
        print("Команду", team, "видалено.")
    else:
        print("Помилка! Такої команди немає у словнику.")

def print_sorted(teams):
    print("\nКоманди за алфавітом:")
    for team in sorted(teams):
        print(team, "-", teams[team], "балів")

def solve_task(teams):
    print("\nРозв'язання завдання")

    try:
        new_team = input("Введіть назву десятої команди: ")

        if new_team in teams:
            print("Помилка! Така команда вже існує.")
            return

        points = int(input("Введіть кількість балів цієї команди: "))

        if points < 0:
            print("Помилка! Кількість балів не може бути від'ємною.")
            return

        place = 1

        for team in teams:
            if teams[team] > points:
                place += 1

        if place == 1 or place == len(teams) + 1:
            print("Помилка! Команда не повинна бути першою або останньою.")
            return

        print("\nМісце команди", new_team, ":", place)

        print("Команди, які набрали менше балів:")

        found = False

        for team in teams:
            if teams[team] < points:
                print(team)
                found = True

        if not found:
            print("Таких команд немає.")

    except ValueError:
        print("Помилка! Кількість балів потрібно вводити числом.")


while True:
    print("\nМЕНЮ")
    print("1 - Вивести всі команди")
    print("2 - Додати команду")
    print("3 - Видалити команду")
    print("4 - Вивести команди за відсортованими ключами")
    print("5 - Розв'язати завдання варіанта")
    print("0 - Вийти")

    choice = input("Оберіть пункт меню: ")

    if choice == "1":
        print_teams(teams)

    elif choice == "2":
        try:
            team = input("Введіть назву команди: ")
            points = int(input("Введіть кількість балів: "))

            if points < 0:
                print("Помилка! Кількість балів не може бути від'ємною.")
            else:
                add_team(teams, team, points)

        except ValueError:
            print("Помилка! Кількість балів потрібно вводити числом.")

    elif choice == "3":
        team = input("Введіть назву команди, яку потрібно видалити: ")
        delete_team(teams, team)

    elif choice == "4":
        print_sorted(teams)

    elif choice == "5":
        solve_task(teams)

    elif choice == "0":
        print("Програму завершено.")
        break

    else:
        print("Помилка! Виберіть пункт меню від 0 до 5.")