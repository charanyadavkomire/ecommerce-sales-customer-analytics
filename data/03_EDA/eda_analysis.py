
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the project folders
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR
    / "02_Cleaned_Data"
    / "cleaned_ecommerce_sales.csv"
)

OUTPUT_DIR = BASE_DIR / "03_EDA"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA_FILE)

print("=" * 50)
print("E-COMMERCE SALES & CUSTOMER ANALYTICS")
print("=" * 50)

print("\nDataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumerical summary:")
print(df.describe())

# Save the summary
summary_file = OUTPUT_DIR / "data_summary.txt"

with open(summary_file, "w", encoding="utf-8") as file:
    file.write("E-Commerce Dataset Summary\n\n")
    file.write(f"Dataset shape: {df.shape}\n\n")
    file.write("Columns:\n")
    file.write(str(df.columns.tolist()) + "\n\n")
    file.write("Missing values:\n")
    file.write(str(df.isnull().sum()) + "\n\n")
    file.write("Duplicate rows: ")
    file.write(str(df.duplicated().sum()) + "\n\n")
    file.write("Numerical summary:\n")
    file.write(df.describe().to_string())

print("\nEDA basic analysis completed!")
print("Summary saved to:", summary_file)
