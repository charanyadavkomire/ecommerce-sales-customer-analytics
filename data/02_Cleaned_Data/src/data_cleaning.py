
import pandas as pd
import os

# 1. Find the project folder
project_folder = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# 2. Load the raw CSV file
input_file = os.path.join(
    project_folder,
    "01_Raw_Data",
    "ecommerce_sales.csv.csv"
)

df = pd.read_csv(input_file)

print("Dataset loaded successfully!")
print("Original shape:", df.shape)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Clean text columns
for col in ["Customer_ID", "Product", "Category", "Region"]:
    df[col] = df[col].astype("string").str.strip()
    df[col] = df[col].replace("", pd.NA)

# 5. Clean dates
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    dayfirst=True,
    errors="coerce"
)

# 6. Convert Revenue and Profit into numbers
for col in ["Revenue", "Profit"]:
    df[col] = (
        df[col]
        .astype("string")
        .str.replace(",", "", regex=False)
        .str.replace("INR", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 7. Convert Quantity into a number
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

# 8. Handle missing values in text columns
for col in ["Customer_ID", "Product", "Category", "Region"]:
    df[col] = df[col].fillna("Unknown")

# 9. Handle missing numeric values
for col in ["Quantity", "Revenue", "Profit"]:
    median_value = df[col].median()
    if pd.notna(median_value):
        df[col] = df[col].fillna(median_value)

# 10. Remove rows with invalid IDs or dates
df = df.dropna(subset=["Order_ID", "Order_Date"])

# 11. Convert Quantity to integer
df["Quantity"] = df["Quantity"].round().astype(int)

# 12. Save the cleaned file
output_folder = os.path.join(project_folder, "02_Cleaned_Data")
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(
    output_folder, "cleaned_ecommerce_sales.csv"
)

df.to_csv(output_file, index=False)

# 13. Display results
print("\nCleaning completed successfully!")
print("Final dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSaved cleaned file to:", output_file)
print("\nFirst five cleaned rows:")
print(df.head())
