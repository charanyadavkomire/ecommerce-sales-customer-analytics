
import pandas as pd
from pathlib import Path

# Locate cleaned dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Convert numeric columns
for column in ["Revenue", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows with invalid KPI values
df = df.dropna(subset=["Revenue", "Profit", "Quantity"])

# Calculate business KPIs
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_order_records = len(df)
total_units_sold = df["Quantity"].sum()

valid_customers = (
    df["Customer_ID"]
    .fillna("")
    .astype(str)
    .str.strip()
)

valid_customers = valid_customers[
    ~valid_customers.str.lower().isin(["", "unknown", "nan", "none"])
]

unique_customers = valid_customers.nunique()

average_revenue_per_record = (
    total_revenue / total_order_records
    if total_order_records else 0
)

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue else 0
)

# Display results
print("\nBUSINESS KPI ANALYSIS")
print("=" * 45)

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Order Records: {total_order_records:,}")
print(f"Total Units Sold: {total_units_sold:,}")
print(f"Unique Customers: {unique_customers:,}")
print(f"Average Revenue per Record: {average_revenue_per_record:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
