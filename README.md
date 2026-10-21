# E-Commerce Sales & Customer Analytics

## Project Overview

This project analyzes e-commerce sales data to identify best-selling products, profitable regions, customer purchasing patterns, and revenue trends. It uses Python and data analysis techniques to turn raw sales data into meaningful business insights.

## Objectives

- Analyze overall sales and profit performance.
- Identify best-selling products and product categories.
- Compare revenue and profit across regions.
- Understand customer purchasing behavior.
- Track monthly revenue trends.
- Calculate important business KPIs.

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- PyCharm
- Git and GitHub

## Dataset

The dataset contains 50,000 sales records and the following nine columns:

- Order_ID
- Order_Date
- Customer_ID
- Product
- Category
- Region
- Quantity
- Revenue
- Profit

## Data Cleaning

The dataset was processed to standardize data types, handle missing or invalid values, and remove duplicate records.

After cleaning, the dataset contained 50,000 records and nine columns, with no missing values or duplicate rows.

## Analysis Performed

### 1. Sales Analysis
Examined sales records and monthly revenue trends.

### 2. Product Analysis
Compared product sales quantities, revenue, and profitability.

### 3. Regional Analysis
Analyzed revenue and profit across different regions.

### 4. Customer Analysis
Examined customer identifiers, customer counts, and revenue contributions.

### 5. Business KPIs
Calculated overall revenue, profit, order records, units sold, customer count, average revenue per record, and profit margin.

## Key Business Findings

- **Total revenue:** ₹4,234,755,650
- **Total profit:** ₹678,983,044
- **Sales records:** 50,000
- **Units sold:** 200,870
- **Unique identified customers:** 1,192
- **Average revenue per record:** ₹84,695.11
- **Profit margin:** 16.03%
- **Highest-revenue product in the analysis:** Camera
- **Highest-profit region in the analysis:** Lucknow

These findings are based on the cleaned dataset and the project's analysis scripts.

## Project Structure

```text
E-Commerce Sales & Customer Analytics/
├── data/
│   ├── 01_Raw_Data/
│   ├── 02_Cleaned_Data/
│   │   └── src/
│   │       └── data_cleaning.py
│   ├── 03_EDA/
│   │   ├── sales_analysis.py
│   │   ├── product_analysis.py
│   │   ├── regional_analysis.py
│   │   ├── customer_analysis.py
│   │   ├── business_kpis.py
│   │   ├── final_dashboard.py
│   │   └── final_dashboard.png
│   └── .venv/
└── README.md
```

## Dashboard

The project includes a final dashboard that presents sales performance and business KPIs visually.

Dashboard image: `data/03_EDA/final_dashboard.png`

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in PyCharm.
3. Configure a Python interpreter and install the required libraries.
4. Run the data-cleaning script before running analysis scripts if you need to reproduce the workflow.
5. Run the individual analysis scripts in `data/03_EDA/`.
6. Run `final_dashboard.py` to generate the final dashboard.

Install the main libraries with:

```bash
pip install pandas matplotlib
```

## Conclusion

This project demonstrates how Python-based data analysis can help businesses understand sales performance, product profitability, regional performance, customer activity, and overall business KPIs.

## Author

Created as an E-Commerce Sales & Customer Analytics project.

