
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

print("\nDATASET CHECK")
print("-" * 40)
print("Total rows:", len(df))
print("Columns:", df.columns.tolist())

# Convert columns to correct data types
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)
df["Revenue"] = pd.to_numeric(
    df["Revenue"], errors="coerce"
)

# Check date and revenue quality
print("\nInvalid dates:", df["Order_Date"].isna().sum())
print("Invalid revenue values:", df["Revenue"].isna().sum())

df = df.dropna(subset=["Order_Date", "Revenue"]).copy()

print("\nDate range:")
print("Start date:", df["Order_Date"].min())
print("End date:", df["Order_Date"].max())

# Group revenue by month
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMONTHLY REVENUE")
print("-" * 40)
print(monthly_sales.to_string())

# Check number of records per month
print("\nRECORDS PER MONTH")
print("-" * 40)
print(df.groupby("Month").size().to_string())

# Generate chart
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="bar")

plt.title("Monthly Revenue Analysis")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
OUTPUT_FILE = BASE_DIR / "03_EDA" / "monthly_revenue.png"
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")

print("\nChart saved to:", OUTPUT_FILE)

plt.show()