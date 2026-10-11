
# E-Commerce Sales & Customer Analytics

## Project Overview
This project analyzes e-commerce sales data using Python to understand revenue, profitability, product performance, regional sales, customer purchasing behavior, and business KPIs.

## Objectives
- Analyze monthly revenue trends.
- Identify top-performing products.
- Compare revenue and profit across regions.
- Identify high-value customers.
- Calculate important business KPIs.
- Present key findings through a visual dashboard.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- PyCharm
- CSV datasets

## Project Structure
```text
E-Commerce Sales & Customer Analytics/
├── README.md
└── data/
    ├── 01_Raw_Data/
    │   └── ecommerce_sales.csv.csv
    ├── 02_Cleaned_Data/
    │   ├── cleaned_ecommerce_sales.csv
    │   └── src/
    │       └── data_cleaning.py
    └── 03_EDA/
        ├── monthly_revenue.py
        ├── product_analysis.py
        ├── regional_analysis.py
        ├── customer_analysis.py
        ├── business_kpis.py
        ├── final_dashboard.py
        └── final_dashboard.png
```

## Key Results
- Total revenue: 4,234,755,650
- Total profit: 678,983,044
- Total records analyzed: 50,000
- Total units sold: 200,870
- Unique valid customer IDs: 1,192
- Average revenue per record: 84,695.11
- Profit margin: 16.03%

## Key Findings
- Laptops generated the highest revenue among standardized products.
- Pune recorded the highest revenue among named regions.
- Lucknow recorded the highest profit among named regions.
- Customer analysis identified the highest-revenue customers.
- Product names and region labels were standardized during analysis.

## Data Quality Limitations
- Monthly records are unevenly distributed, with substantially fewer records from September through December.
- Some customer IDs and region values are missing or invalid.
- Order records represent dataset rows and should not automatically be interpreted as unique orders.
- Results reflect the supplied dataset and are not independently verified real-world business figures.

## Dashboard
The generated dashboard is available at:

`data/03_EDA/final_dashboard.png`

## How to Run
1. Install Python.
2. Install the required libraries:
   `pip install pandas matplotlib`
3. Run the data-cleaning script.
4. Run the analysis scripts in the `data/03_EDA/` folder.
5. Run `final_dashboard.py` to regenerate the dashboard.

## Conclusion
This project demonstrates how Python can be used to clean data, analyze business performance, calculate KPIs, and visualize e-commerce sales insights.
