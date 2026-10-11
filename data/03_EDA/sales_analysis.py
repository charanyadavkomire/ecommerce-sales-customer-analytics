
import pandas as pd
from pathlib import Path

# Find the cleaned dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "02_Cleaned_Data" / "cleaned_ecommerce_sales.csv"

# Load the data
df = pd.read_csv(DATA_FILE)

print("SALES ANALYSIS")
print("-" * 40)

# Display available columns
print("\nColumns in dataset:")
print(df.columns.tolist())

# Display first five records
print("\nFirst five records:")
print(df.head().to_string(index=False))

# Display numerical columns
print("\nNumerical column summary:")
print(df.describe().to_string())

print("\nSales analysis completed!")
