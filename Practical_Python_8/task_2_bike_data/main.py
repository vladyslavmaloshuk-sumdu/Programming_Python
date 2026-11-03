
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "data" / "comptage_velo_2018.csv"
OUTPUT_FILE = Path(__file__).parent / "bike_analysis_results.csv"
GRAPH_FILE = Path(__file__).parent / "berri1_monthly.png"

df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

print("=== 1. Перші 5 рядків DataFrame ===")
print(df.head())

print("\n=== 2. Інформація про DataFrame ===")
df.info()

print("\n=== 3. Описова статистика ===")
print(df.describe())

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

df = df.dropna(subset=["Date"]).copy()

df = df[df["Date"].dt.year == 2018].copy()

bike_columns = [col for col in df.columns if col not in ["Date", "Month"]]

for col in bike_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df[bike_columns] = df[bike_columns].fillna(0).round(0).astype(int)

print("\n=== 4. Типи даних після оброблення ===")
print(df.dtypes)

total_cyclists = int(df[bike_columns].sum().sum())

print("\n=== 5. Загальна кількість велосипедистів за 2018 рік ===")
print(f"Загальна кількість: {total_cyclists:,}".replace(",", " "))

df["Month"] = df["Date"].dt.month

selected_paths = ["Berri1", "Boyer", "Maisonneuve_2"]

selected_paths = [
    path for path in selected_paths if path in df.columns
]

if not selected_paths:
    raise ValueError(
        "Не знайдено вибраних доріжок. "
        "Перевір назви стовпців у CSV-файлі."
    )

monthly_totals = df.groupby("Month")[selected_paths].sum()

print("\n=== 6. Найпопулярніший місяць для трьох доріжок ===")

for path in selected_paths:
    best_month = int(monthly_totals[path].idxmax())
    best_count = int(monthly_totals[path].max())

    print(
        f"{path}: місяць {best_month}, "
        f"кількість велосипедистів: "
        f"{best_count:,}".replace(",", " ")
    )

path_to_analyze = "Berri1"

if path_to_analyze in df.columns:
    monthly_analysis = df.groupby("Month")[path_to_analyze].agg(
        ["sum", "mean", "max", "min", "count"]
    )

    for col in ["sum", "max", "min", "count"]:
        monthly_analysis[col] = monthly_analysis[col].astype(int)

    print(f"\n=== 7. Аналіз доріжки {path_to_analyze} за місяцями ===")
    print(monthly_analysis)

    monthly_analysis["sum"].plot(
        kind="line",
        marker="o",
        figsize=(10, 5)
    )

    plt.title(
        f"Кількість велосипедистів на доріжці "
        f"{path_to_analyze} за місяцями у 2018 році"
    )
    plt.xlabel("Місяць")
    plt.ylabel("Кількість велосипедистів")
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(GRAPH_FILE, dpi=150)
    print(f"\nГрафік збережено у файлі: {GRAPH_FILE}")

    plt.show()
else:
    print(f"\nДоріжку {path_to_analyze} не знайдено, графік не побудовано.")

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"\nРезультати збережено у файлі: {OUTPUT_FILE}")
print("\nАналіз завершено!")