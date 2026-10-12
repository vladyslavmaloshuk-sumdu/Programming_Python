import csv
import os
import requests
import matplotlib.pyplot as plt


# Основні параметри програми
indicator = "NY.GDP.PCAP.CD"
start_year = 2000
end_year = 2024

csv_file = "gdp_per_capita.csv"

url = (
    "https://api.worldbank.org/v2/country/all/indicator/"
    + indicator
)


# Завантаження даних і створення CSV-файлу
def download_data():
    try:
        response = requests.get(
            url,
            params={
                "date": f"{start_year}:{end_year}",
                "format": "json",
                "per_page": 20000
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list) or len(data) < 2:
            print("Помилка отримання даних.")
            return False

        if not isinstance(data[1], list) or not data[1]:
            print("Дані відсутні.")
            return False

        with open(
            csv_file, "w", newline="", encoding="utf-8-sig"
        ) as file:
            writer = csv.writer(file)
            writer.writerow([
                "Country",
                "Year",
                "GDP per capita (current US$)"
            ])

            for item in data[1]:
                if (
                    item.get("value") is not None
                    and item.get("country") is not None
                    and item.get("date") is not None
                ):
                    writer.writerow([
                        item["country"]["value"],
                        item["date"],
                        item["value"]
                    ])

        print("Дані успішно збережено у CSV.")
        return True

    except (requests.exceptions.RequestException, ValueError) as error:
        print("Помилка завантаження даних:", error)
        return False

    except OSError as error:
        print("Помилка створення CSV-файлу:", error)
        return False


# Читання та оброблення CSV-файлу
def read_data():
    countries = {}

    try:
        with open(csv_file, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = [
                "Country",
                "Year",
                "GDP per capita (current US$)"
            ]

            if not reader.fieldnames or not all(
                column in reader.fieldnames
                for column in required_columns
            ):
                print("Помилка: неправильна структура CSV-файлу.")
                return None

            for row in reader:
                try:
                    country = row["Country"].strip()
                    year = int(row["Year"])
                    value = float(
                        row["GDP per capita (current US$)"]
                    )

                    if country and value >= 0:
                        if country not in countries:
                            countries[country] = {}

                        countries[country][year] = value

                except (ValueError, TypeError):
                    continue

        if not countries:
            print("У CSV-файлі немає коректних даних.")
            return None

        return countries

    except (OSError, csv.Error) as error:
        print("Помилка читання CSV-файлу:", error)
        return None


# Побудова лінійного графіка
def line_chart(data, country):
    if "Ukraine" not in data or country not in data:
        print("Не вдалося знайти дані для побудови графіка.")
        return

    common_years = sorted(
        set(data["Ukraine"]) & set(data[country])
    )

    if not common_years:
        print("Немає спільних років для порівняння.")
        return

    ukraine_values = [
        data["Ukraine"][year] for year in common_years
    ]
    country_values = [
        data[country][year] for year in common_years
    ]

    plt.figure(figsize=(10, 5))
    plt.plot(
        common_years, ukraine_values,
        marker="o", label="Ukraine"
    )
    plt.plot(
        common_years, country_values,
        marker="o", label=country
    )

    plt.title("GDP per capita dynamics")
    plt.xlabel("Year")
    plt.ylabel("GDP per capita (current US$)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Побудова стовпчастої діаграми
def bar_chart(data, country):
    years = sorted(data[country].keys())
    values = [data[country][year] for year in years]

    plt.figure(figsize=(10, 5))
    plt.bar(years, values)

    plt.title("GDP per capita in " + country)
    plt.xlabel("Year")
    plt.ylabel("GDP per capita (current US$)")
    plt.xticks(years, rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


# Побудова кругової діаграми
def pie_chart(data, country, year):
    if "Ukraine" not in data or country not in data:
        print("Не вдалося знайти дані для порівняння.")
        return

    if year not in data["Ukraine"] or year not in data[country]:
        print("Немає даних для обох країн за цей рік.")
        return

    if country == "Ukraine":
        print("Оберіть країну, відмінну від України.")
        return

    values = [
        data["Ukraine"][year],
        data[country][year]
    ]

    if sum(values) <= 0:
        print("Неможливо побудувати кругову діаграму.")
        return

    plt.figure(figsize=(7, 7))
    plt.pie(
        values,
        labels=["Ukraine", country],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("GDP per capita comparison (" + str(year) + ")")
    plt.tight_layout()
    plt.show()


# Основна функція програми
def main():
    print("GDP per capita - World Bank data")
    print("Період:", start_year, "-", end_year)
    print()

    # Якщо CSV-файлу немає, завантажуємо дані
    if not os.path.exists(csv_file):
        print("CSV-файл не знайдено. Завантаження даних...")
        if not download_data():
            return

    # Читаємо дані з CSV
    data = read_data()

    if data is None:
        return

    if "Ukraine" not in data:
        print("У файлі немає даних для України.")
        return

    # Введення назви країни
    country_input = input(
        "Введіть назву країни англійською (наприклад, Poland): "
    ).strip()

    # Перевірка наявності країни
    country_names = {
        name.lower(): name for name in data
    }

    country = country_names.get(country_input.lower())

    if country is None:
        print("Такої країни немає у завантажених даних.")
        print("Перевірте правильність назви.")
        return

    if country == "Ukraine":
        print("Для порівняння оберіть країну, відмінну від України.")
        return

    # Побудова першого та другого графіків
    line_chart(data, country)
    bar_chart(data, country)

    # Введення року для кругової діаграми
    try:
        year = int(input(
            f"Введіть рік для кругової діаграми "
            f"({start_year}-{end_year}): "
        ))

        if year < start_year or year > end_year:
            print("Рік виходить за межі обраного періоду.")
            return

        pie_chart(data, country, year)

    except ValueError:
        print("Помилка: потрібно ввести ціле число року.")


if __name__ == "__main__":
    main()