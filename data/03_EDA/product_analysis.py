
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the cleaned dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Ensure numeric columns are valid
for column in ["Quantity", "Revenue", "Profit"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=["Product", "Quantity", "Revenue", "Profit"])

# Standardize inconsistent product names
product_mapping = {
    "Smart Watch": "Smartwatch",
    "smart watch": "Smartwatch",
    "makeup kit": "Makeup Kit",
    "MAKEUP KIT": "Makeup Kit",
    "Make Up Kit": "Makeup Kit",
    "Vacum Cleaner": "Vacuum Cleaner",
    "Vacuum cleaner": "Vacuum Cleaner",
    "vacuum cleaner": "Vacuum Cleaner",
    "HEADPHONES": "Headphones",
    "Head Phones": "Headphones",
    "headphones": "Headphones"
}

df["Product"] = df["Product"].replace(product_mapping)

# Group performance by product
product_summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

# Best-selling products
print("\nBEST-SELLING PRODUCTS BY QUANTITY")
print("-" * 50)
print(product_summary.sort_values(
    "Total_Quantity", ascending=False
).to_string())

# Top 10 products by revenue
top_revenue = product_summary.sort_values(
    "Total_Revenue", ascending=False
).head(10)

print("\nTOP 10 PRODUCTS BY REVENUE")
print("-" * 50)
print(top_revenue.to_string())

# Create revenue chart
plt.figure(figsize=(12, 6))
top_revenue["Total_Revenue"].sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.tight_layout()

# Save chart
OUTPUT_FILE = BASE_DIR / "03_EDA" / "top_products_revenue.png"
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")

print("\nChart saved to:", OUTPUT_FILE)

plt.show()
