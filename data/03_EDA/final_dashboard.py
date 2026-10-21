
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

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR
    / "02_Cleaned_Data"
    / "cleaned_ecommerce_sales.csv"
)

OUTPUT_FILE = BASE_DIR / "03_EDA" / "final_dashboard.png"

# --------------------------------------------------
# 2. LOAD AND PREPARE DATA
# --------------------------------------------------
df = pd.read_csv(DATA_FILE)

# Parse dates using day-first interpretation
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    dayfirst=True
)

for column in ["Revenue", "Profit", "Quantity"]:
    df[column] = pd.to_numeric(
        df[column].astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )

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

df["Product"] = (
    df["Product"].astype(str).str.strip().replace(product_mapping)
)

df["Region"] = df["Region"].astype(str).str.strip().str.title()

# --------------------------------------------------
# 3. CALCULATE BUSINESS KPIs
# --------------------------------------------------
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
    total_profit / total_revenue * 100
    if total_revenue != 0 else 0
)

# --------------------------------------------------
# 4. PREPARE CHART DATA
# --------------------------------------------------

# Monthly revenue
monthly_data = df.dropna(subset=["Order_Date"]).copy()

monthly_data["Month"] = (
    monthly_data["Order_Date"].dt.to_period("M")
)

monthly_revenue = (
    monthly_data.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

# Top 5 products
product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .nlargest(5)
    .sort_values()
)

# Revenue by region
region_revenue = (
    df[df["Region"].str.lower() != "unknown"]
    .groupby("Region")["Revenue"]
    .sum()
    .sort_values()
)

# Top 5 valid customers
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
    .nlargest(5)
    .sort_values()
)

# --------------------------------------------------
# 5. CHART FORMATTING
# --------------------------------------------------

def crore_formatter(value, position):
    return f"₹{value / 10_000_000:.1f} Cr"


def style_axis(ax, title, xlabel):
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.grid(axis="x", alpha=0.25)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=9)


# --------------------------------------------------
# 6. CREATE PROFESSIONAL DASHBOARD
# --------------------------------------------------

fig = plt.figure(figsize=(20, 13), facecolor="#F4F6F9")

fig.suptitle(
    "E-COMMERCE SALES & CUSTOMER ANALYTICS",
    fontsize=23,
    fontweight="bold",
    y=0.975,
    color="#183153"
)

fig.text(
    0.5, 0.945,
    "Sales Performance | Product Insights | Regional Analysis | Customers",
    ha="center",
    fontsize=11,
    color="#555555"
)

gs = fig.add_gridspec(
    3, 3,
    left=0.06,
    right=0.97,
    top=0.89,
    bottom=0.09,
    height_ratios=[0.85, 1.35, 1.35],
    hspace=0.48,
    wspace=0.35
)

# --------------------------------------------------
# 7. KPI CARDS
# --------------------------------------------------

kpis = [
    ("TOTAL REVENUE", f"₹{total_revenue:,.0f}"),
    ("TOTAL PROFIT", f"₹{total_profit:,.0f}"),
    ("PROFIT MARGIN", f"{profit_margin:.2f}%"),
    ("ORDER RECORDS", f"{total_records:,}"),
    ("UNITS SOLD", f"{total_units:,.0f}"),
    ("UNIQUE CUSTOMERS", f"{unique_customers:,}")
]

for i, (label, value) in enumerate(kpis):
    row = i // 3
    col = i % 3

    ax = fig.add_subplot(gs[row, col])
    ax.set_facecolor("white")
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_color("#DCE3EA")
        spine.set_linewidth(1.2)

    ax.text(
        0.5, 0.68, label,
        transform=ax.transAxes,
        ha="center",
        fontsize=11,
        fontweight="bold",
        color="#526579"
    )

    ax.text(
        0.5, 0.32, value,
        transform=ax.transAxes,
        ha="center",
        fontsize=17 if i < 2 else 19,
        fontweight="bold",
        color="#183153"
    )

# --------------------------------------------------
# 8. MONTHLY REVENUE CHART
# --------------------------------------------------

ax1 = fig.add_subplot(gs[1, :])

if not monthly_revenue.empty:
    month_labels = monthly_revenue.index.astype(str)

    ax1.plot(
        month_labels,
        monthly_revenue.values,
        marker="o",
        linewidth=2.5,
        markersize=6
    )

    ax1.yaxis.set_major_formatter(
        mticker.FuncFormatter(crore_formatter)
    )

    ax1.tick_params(axis="x", rotation=35)

    style_axis(
        ax1,
        "Monthly Revenue Trend",
        "Month"
    )

    ax1.set_ylabel("Revenue (₹ Crore)", fontsize=10)

    ax1.grid(axis="y", alpha=0.25)

# --------------------------------------------------
# 9. TOP PRODUCTS BY REVENUE
# --------------------------------------------------

ax2 = fig.add_subplot(gs[2, 0])

product_revenue.plot(
    kind="barh",
    ax=ax2,
    color="#3984C6",
    edgecolor="white"
)

ax2.xaxis.set_major_formatter(
    mticker.FuncFormatter(crore_formatter)
)

style_axis(
    ax2,
    "Top 5 Products by Revenue",
    "Revenue (₹ Crore)"
)

ax2.set_ylabel("")

# --------------------------------------------------
# 10. REVENUE BY REGION
# --------------------------------------------------

ax3 = fig.add_subplot(gs[2, 1])

region_revenue.plot(
    kind="barh",
    ax=ax3,
    color="#36A18B",
    edgecolor="white"
)

ax3.xaxis.set_major_formatter(
    mticker.FuncFormatter(crore_formatter)
)

style_axis(
    ax3,
    "Revenue by Region",
    "Revenue (₹ Crore)"
)

ax3.set_ylabel("")

# --------------------------------------------------
# 11. TOP CUSTOMERS BY REVENUE
# --------------------------------------------------

ax4 = fig.add_subplot(gs[2, 2])

top_customers.plot(
    kind="barh",
    ax=ax4,
    color="#E6A04B",
    edgecolor="white"
)

ax4.xaxis.set_major_formatter(
    mticker.FuncFormatter(crore_formatter)
)

style_axis(
    ax4,
    "Top 5 Customers by Revenue",
    "Revenue (₹ Crore)"
)

ax4.set_ylabel("Customer ID")

# --------------------------------------------------
# 12. FOOTNOTE AND SAVE
# --------------------------------------------------

fig.text(
    0.5, 0.035,
    "Note: Monthly record counts are uneven. Recent-month comparisons "
    "should be interpreted cautiously.",
    ha="center",
    fontsize=9,
    color="#555555"
)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(
    OUTPUT_FILE,
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.close(fig)

print("DASHBOARD CREATED SUCCESSFULLY!")
print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Profit: ₹{total_profit:,.0f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Unique Customers: {unique_customers:,}")
print(f"Dashboard saved at: {OUTPUT_FILE}")

