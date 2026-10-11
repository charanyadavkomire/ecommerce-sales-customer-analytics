
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the cleaned dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Convert numeric columns
for column in ["Revenue", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=["Region", "Revenue", "Profit", "Quantity"]).copy()

# Standardize region names
df["Region"] = df["Region"].str.strip().str.title()

# Calculate regional performance
regional_summary = df.groupby("Region").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

# Sort by revenue
regional_summary = regional_summary.sort_values(
    "Total_Revenue", ascending=False
)

print("\nREGIONAL PERFORMANCE ANALYSIS")
print("-" * 60)
print(regional_summary.to_string())

# Create regional revenue chart
plt.figure(figsize=(11, 6))
regional_summary["Total_Revenue"].sort_values().plot(kind="barh")

plt.title("Revenue by Region")
plt.xlabel("Total Revenue")
plt.ylabel("Region")
plt.tight_layout()

# Save chart
OUTPUT_FILE = BASE_DIR / "03_EDA" / "regional_revenue.png"
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")

print("\nChart saved to:", OUTPUT_FILE)

plt.show()
