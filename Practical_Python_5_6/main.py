import requests
import json
import csv


# Основні параметри програми
indicator = "NY.GDP.PCAP.CD"
year = "2019"

url = (
    f"https://api.worldbank.org/v2/country/all/"
    f"indicator/{indicator}?date={year}&format=json&per_page=500"
)

json_file = "gdp_per_capita.json"
csv_file = "gdp_per_capita.csv"


def get_data(url):
    """Отримання даних з API Світового банку."""
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # Перевірка коректності отриманих даних
            if not isinstance(data, list) or len(data) < 2:
                print("Помилка: отримано некоректні дані.")
                return None

            if not isinstance(data[1], list) or len(data[1]) == 0:
                print("Помилка: дані відсутні.")
                return None

            print("Дані успішно отримано.")
            return data

        else:
            print(
                "Помилка отримання даних. "
                f"Код відповіді сервера: {response.status_code}"
            )
            return None

    except requests.exceptions.RequestException as error:
        print(f"Помилка HTTP-запиту: {error}")
        return None

    except ValueError:
        print("Помилка: відповідь сервера не є коректним JSON.")
        return None


def save_json(data, filename):
    """Збереження отриманих даних у JSON-файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"JSON-файл успішно створено: {filename}")
        return True

    except (OSError, IOError) as error:
        print(f"Помилка під час збереження JSON-файлу: {error}")
        return False


def convert_to_csv(data, filename):
    """Перетворення JSON-даних у CSV та збереження файлу."""
    try:
        csv_data = []

        for item in data[1]:
            if (
                item.get("value") is not None
                and item.get("country") is not None
                and item.get("date") is not None
            ):
                csv_data.append([
                    item["country"]["value"],
                    item["date"],
                    item["value"]
                ])

        if not csv_data:
            print("Помилка: немає даних для створення CSV.")
            return False

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Country",
                "Year",
                "GDP per capita (current US$)"
            ])

            writer.writerows(csv_data)

        print(f"CSV-файл успішно створено: {filename}")
        return True

    except (OSError, IOError) as error:
        print(f"Помилка під час збереження CSV-файлу: {error}")
        return False

    except (KeyError, TypeError) as error:
        print(f"Помилка оброблення даних: {error}")
        return False


def print_results(data, json_filename, csv_filename):
    """Виведення результатів на екран."""
    try:
        print("\n" + "=" * 60)
        print("ЗМІСТ JSON-ФАЙЛУ")
        print("=" * 60)

        with open(json_filename, "r", encoding="utf-8") as file:
            json_content = json.load(file)

        # Виводимо перші 5 записів із JSON,
        # щоб не перевантажувати консоль
        for item in json_content[1][:5]:
            print(json.dumps(
                item,
                ensure_ascii=False,
                indent=4
            ))
            print()

        print("=" * 60)
        print("ЗМІСТ CSV-ФАЙЛУ")
        print("=" * 60)

        with open(
            csv_filename,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            for index, row in enumerate(reader):
                print(", ".join(row))

                # Заголовок + перші 5 рядків
                if index >= 5:
                    break

    except (OSError, IOError) as error:
        print(f"Помилка читання файлу: {error}")

    except (json.JSONDecodeError, csv.Error) as error:
        print(f"Помилка оброблення файлу: {error}")


def main():
    """Основна функція програми."""
    print("Отримання даних GDP per capita з API Світового банку")
    print(f"Рік: {year}")
    print(f"Код показника: {indicator}")
    print()

    # Отримання даних
    data = get_data(url)

    if data is None:
        print("Програму завершено через помилку отримання даних.")
        return

    # Збереження JSON
    if not save_json(data, json_file):
        print("Програму завершено через помилку збереження JSON.")
        return

    # Перетворення JSON у CSV
    if not convert_to_csv(data, csv_file):
        print("Програму завершено через помилку створення CSV.")
        return

    # Виведення результатів
    print_results(data, json_file, csv_file)

    print("\n" + "=" * 60)
    print("Роботу програми завершено успішно.")
    print("=" * 60)


# Запуск програми
if __name__ == "__main__":
    main()