import json


# Словник із практичної роботи №3
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


# Назви JSON-файлів
json_file = "teams.json"
result_file = "search_team.json"


def save_to_json(data, filename):
    """Збереження даних у JSON-файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"Дані успішно збережено у файл '{filename}'.")
        return True

    except (OSError, TypeError) as error:
        print(f"Помилка під час збереження файлу: {error}")
        return False


def read_from_json(filename):
    """Читання даних із JSON-файлу."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None

    except json.JSONDecodeError:
        print(f"Помилка: файл '{filename}' містить некоректний JSON.")
        return None

    except OSError as error:
        print(f"Помилка під час читання файлу: {error}")
        return None


def print_json_data(data):
    """Виведення JSON-даних на екран."""
    print("\nВміст JSON-файлу:")
    print("-" * 40)

    print(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4
        )
    )


def search_team(data, team_name):
    """Пошук команди за її назвою."""
    for team, points in data.items():
        if team.lower() == team_name.lower():
            return {
                team: points
            }

    return None


def main():
    """Основна функція програми."""

    print("=" * 50)
    print("ПЕРЕТВОРЕННЯ СЛОВНИКА У JSON")
    print("=" * 50)

    # Збереження словника у JSON-файл
    if not save_to_json(teams, json_file):
        return

    # Читання даних із JSON-файлу
    data = read_from_json(json_file)

    if data is None:
        return

    # Виведення вмісту JSON-файлу
    print_json_data(data)

    # Введення назви команди для пошуку
    team_name = input(
        "\nВведіть назву команди для пошуку: "
    ).strip()

    # Перевірка введення
    if not team_name:
        print("Помилка: назву команди не введено.")
        return

    # Пошук команди
    result = search_team(data, team_name)

    if result is None:
        print(f"Команду '{team_name}' не знайдено.")
        return

    # Виведення результату пошуку
    print("\nРезультат пошуку:")
    print("-" * 40)

    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=4
        )
    )

    # Збереження результату пошуку
    save_to_json(result, result_file)


# Запуск програми
if __name__ == "__main__":
    main()