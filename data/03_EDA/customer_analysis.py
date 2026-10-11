
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate cleaned dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Convert numeric columns
for column in ["Revenue", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Exclude missing customer IDs for customer-level analysis
df = df.dropna(subset=["Customer_ID", "Revenue", "Profit"]).copy()


# Standardize customer IDs and exclude missing placeholders
df["Customer_ID"] = (
    df["Customer_ID"]
    .fillna("")
    .astype(str)
    .str.strip()
)

missing_ids = df["Customer_ID"].str.lower().isin(
    ["", "unknown", "nan", "none"]
)

print("Records without valid customer IDs:", missing_ids.sum())

df = df[~missing_ids].copy()


# Summarize customer activity
customer_summary = df.groupby("Customer_ID").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

# Top 10 customers by revenue
top_customers = customer_summary.sort_values(
    "Total_Revenue", ascending=False
).head(10)

print("\nCUSTOMER ANALYSIS")
print("-" * 60)
print("Unique customers:", df["Customer_ID"].nunique())

print("\nTOP 10 CUSTOMERS BY REVENUE")
print("-" * 60)
print(top_customers.to_string())

# Create chart
plt.figure(figsize=(11, 6))
top_customers["Total_Revenue"].sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Customer ID")
plt.tight_layout()

# Save chart
OUTPUT_FILE = BASE_DIR / "03_EDA" / "top_customers_revenue.png"
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")

print("\nChart saved to:", OUTPUT_FILE)

plt.show()
