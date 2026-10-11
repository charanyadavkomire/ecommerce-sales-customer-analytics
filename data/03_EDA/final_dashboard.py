
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"
OUTPUT_FILE = BASE_DIR / "03_EDA" / "final_dashboard.png"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Clean data types used in the dashboard
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

for column in ["Revenue", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=["Revenue", "Profit", "Quantity"])

# Standardize product names
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
    "headphones": "Headphones",
}

df["Product"] = df["Product"].astype(str).str.strip().replace(product_mapping)
df["Region"] = df["Region"].astype(str).str.strip().str.title()

# Calculate KPIs
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_records = len(df)
total_units = df["Quantity"].sum()

customer_ids = df["Customer_ID"].fillna("").astype(str).str.strip()
valid_customer_ids = customer_ids[
    ~customer_ids.str.lower().isin(["", "unknown", "nan", "none"])
]
unique_customers = valid_customer_ids.nunique()

profit_margin = (
    total_profit / total_revenue * 100 if total_revenue else 0
)

# Prepare chart data
monthly_data = df.dropna(subset=["Order_Date"]).copy()
monthly_data["Month"] = monthly_data["Order_Date"].dt.to_period("M").astype(str)
monthly_revenue = monthly_data.groupby("Month")["Revenue"].sum()

product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

region_revenue = (
    df[df["Region"] != "Unknown"]
    .groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=True)
)

customer_data = df.copy()
customer_data["Customer_ID"] = customer_ids
customer_data = customer_data[
    ~customer_data["Customer_ID"].str.lower().isin(
        ["", "unknown", "nan", "none"]
    )
]

top_customers = (
    customer_data.groupby("Customer_ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .sort_values(ascending=True)
)

# Create dashboard layout
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(
    "E-COMMERCE SALES & CUSTOMER ANALYTICS DASHBOARD",
    fontsize=19,
    fontweight="bold",
    y=0.98,
)

# KPI cards
ax = axes[0, 0]
ax.axis("off")
kpi_text = (
    f"TOTAL REVENUE\n₹{total_revenue:,.0f}\n\n"
    f"TOTAL PROFIT\n₹{total_profit:,.0f}\n\n"
    f"PROFIT MARGIN\n{profit_margin:.2f}%"
)
ax.text(
    0.05, 0.92, kpi_text,
    transform=ax.transAxes,
    va="top",
    fontsize=15,
    fontweight="bold",
)

ax = axes[0, 1]
ax.axis("off")
ax.text(
    0.05, 0.92,
    f"ORDER RECORDS\n{total_records:,}\n\n"
    f"UNITS SOLD\n{total_units:,.0f}\n\n"
    f"UNIQUE CUSTOMERS\n{unique_customers:,}",
    transform=ax.transAxes,
    va="top",
    fontsize=15,
    fontweight="bold",
)

# Monthly revenue
ax = axes[0, 2]
monthly_revenue.plot(ax=ax, marker="o")
ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (₹)")
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.3)

# Top 5 products
ax = axes[1, 0]
product_revenue.sort_values().plot(kind="barh", ax=ax)
ax.set_title("Top 5 Products by Revenue")
ax.set_xlabel("Revenue (₹)")
ax.set_ylabel("Product")
ax.grid(axis="x", alpha=0.3)

# Revenue by region
ax = axes[1, 1]
region_revenue.plot(kind="barh", ax=ax)
ax.set_title("Revenue by Region")
ax.set_xlabel("Revenue (₹)")
ax.set_ylabel("Region")
ax.grid(axis="x", alpha=0.3)

# Top 5 customers
ax = axes[1, 2]
top_customers.plot(kind="barh", ax=ax)
ax.set_title("Top 5 Customers by Revenue")
ax.set_xlabel("Revenue (₹)")
ax.set_ylabel("Customer ID")
ax.grid(axis="x", alpha=0.3)

fig.text(
    0.5, 0.015,
    "Note: Monthly records are unevenly distributed; interpret recent-month comparisons cautiously.",
    ha="center",
    fontsize=9,
)

plt.tight_layout(rect=[0, 0.04, 1, 0.95])
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
plt.close()

print("DASHBOARD CREATED SUCCESSFULLY!")
print(f"Dashboard saved at: {OUTPUT_FILE}")
