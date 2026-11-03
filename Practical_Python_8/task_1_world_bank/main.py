from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "gdp_per_capita.csv"
OUTPUT_FILE = Path(__file__).parent / "gdp_analysis_results.csv"

df = pd.read_csv(DATA_FILE)

print("=== 1. Повний DataFrame ===")
print(df.to_string())

print("\n=== 2. Перші 3 рядки DataFrame ===")
print(df.head(3))

print("\n=== 3. Типи даних у стовпцях ===")
print(df.dtypes)

print("\n=== 4. Розмір DataFrame ===")
print(f"Кількість рядків: {df.shape[0]}")
print(f"Кількість стовпців: {df.shape[1]}")
print(f"Розмір таблиці: {df.shape}")

print("\n=== 5. Описова статистика ===")
print(df.describe())

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["GDP per capita (current US$)"] = pd.to_numeric(
    df["GDP per capita (current US$)"],
    errors="coerce"
)

df = df.dropna(subset=["GDP per capita (current US$)"])

df["GDP per capita (thousand US$)"] = (
    df["GDP per capita (current US$)"] / 1000
)

print("\n=== 6. DataFrame після оброблення ===")
print(df.head(10))

df_2019 = df[df["Year"] == 2019]

print("\n=== 7. Дані за 2019 рік ===")
print(df_2019.to_string())

df_sorted = df_2019.sort_values(
    by="GDP per capita (current US$)",
    ascending=False
)

print("\n=== 8. Топ-10 записів за ВВП на душу населення ===")
print(df_sorted.head(10).to_string(index=False))

print("\n=== 9. Статистика ВВП за роками ===")
year_statistics = df.groupby("Year")[
    "GDP per capita (current US$)"
].agg(["mean", "max", "min", "count"])

print(year_statistics)

print("\n=== 10. Кількість унікальних років ===")
print(df["Year"].nunique())

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print("\n=== 11. Збереження результатів ===")
print(f"Результати збережено у файлі: {OUTPUT_FILE}")