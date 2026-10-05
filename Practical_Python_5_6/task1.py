import csv


# Основні параметри програми
input_file = "gdp_per_capita.csv"
output_file = "search_results.csv"


def read_csv_data(filename):
    """Читання даних із CSV-файлу."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Помилка: CSV-файл не містить заголовків.")
                return None

            data = list(reader)

            if not data:
                print("Помилка: CSV-файл не містить даних.")
                return None

            return data

    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None

    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{filename}'.")
        return None

    except OSError as error:
        print(f"Помилка під час відкриття файлу: {error}")
        return None


def search_countries(data, countries):
    """Пошук країн у даних."""
    results = []

    for row in data:
        country = row.get("Country", "").strip()

        for searched_country in countries:
            if country.lower() == searched_country.lower():
                results.append(row)
                break

    return results


def save_results(results, filename):
    """Збереження результатів пошуку у новий CSV-файл."""
    try:
        if not results:
            print("Немає результатів для збереження.")
            return False

        fieldnames = [
            "Country",
            "Year",
            "GDP per capita (current US$)"
        ]

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for row in results:
                writer.writerow({
                    "Country": row.get("Country", ""),
                    "Year": row.get("Year", ""),
                    "GDP per capita (current US$)": row.get(
                        "GDP per capita (current US$)",
                        ""
                    )
                })

        print(f"Результати успішно збережено у файл '{filename}'.")
        return True

    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{filename}'.")
        return False

    except OSError as error:
        print(f"Помилка під час збереження файлу: {error}")
        return False


def main():
    """Основна функція програми."""
    print("=" * 60)
    print("ПОШУК ДАНИХ ПРО ВВП НА ДУШУ НАСЕЛЕННЯ")
    print("=" * 60)

    # Читання даних із CSV
    data = read_csv_data(input_file)

    if data is None:
        return

    # Введення назв країн
    user_input = input(
        "\nВведіть назви країн через кому: "
    ).strip()

    if not user_input:
        print("Помилка: назву країни не введено.")
        return

    countries = [
        country.strip()
        for country in user_input.split(",")
        if country.strip()
    ]

    if not countries:
        print("Помилка: введено некоректні дані.")
        return

    # Пошук країн
    results = search_countries(data, countries)

    # Виведення результатів
    print("\nРезультати пошуку:")
    print("-" * 60)

    if results:
        for row in results:
            print(
                f"{row['Country']}: "
                f"{row['GDP per capita (current US$)']} US$ "
                f"({row['Year']})"
            )

        # Збереження результатів
        save_results(results, output_file)

    else:
        print("Жодної із введених країн не знайдено.")


# Запуск програми
if __name__ == "__main__":
    main()