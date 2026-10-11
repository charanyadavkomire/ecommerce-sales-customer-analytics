
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "01_Raw_Data" / "ecommerce_sales.csv.csv"

df = pd.read_csv(RAW_FILE)

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

print("\nDATE DISTRIBUTION CHECK")
print("-" * 40)

print("Earliest date:", df["Order_Date"].min())
print("Latest date:", df["Order_Date"].max())

print("\nRecords per day for September:")
september = df[df["Order_Date"].dt.month == 9]
print(september["Order_Date"].dt.strftime("%Y-%m-%d").value_counts().sort_index())

print("\nRecords per day for October:")
october = df[df["Order_Date"].dt.month == 10]
print(october["Order_Date"].dt.strftime("%Y-%m-%d").value_counts().sort_index())
