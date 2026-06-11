import pandas as pd
from logger_config import logger

logger.info("Transformation started")



# Load the data
df = pd.read_csv('ecommerce_dataset_updated.csv')

print("=" * 50)
print("TRANSFORM PHASE")
print("=" * 50)

# 1. Check for missing values
print("\n1. MISSING VALUES:")

print(df.isnull().sum())

# 2. Check data types
print("\n2. DATA TYPES:")
print(df.dtypes)

# 3. Check for duplicates
print("\n3. DUPLICATES:")
print(f"Duplicate rows: {df.duplicated().sum()}")

try:
	df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
	df['Discount (%)'] = pd.to_numeric(df['Discount (%)'], errors='coerce')
	df['Price (Rs.)'] = pd.to_numeric(df['Price (Rs.)'], errors='coerce')
	df['Final_Price(Rs.)'] = pd.to_numeric(df['Final_Price(Rs.)'], errors='coerce')

# 5. Create calculated column (Discount Amount)
	df['Discount_Amount'] = df['Price (Rs.)'] - df['Final_Price(Rs.)']

# 6. Fill missing values
	df['Discount (%)'] = df['Discount (%)'].fillna(0)
	df['Payment_Method'] = df['Payment_Method'].fillna('Unknown')

except Exception as e:
	logger.error("TRANSFORMATION FAILED")


print("\n4. AFTER CLEANING:")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"\nNew column added: 'Discount_Amount'")

# 7. Save cleaned data
df.to_csv('cleaned_ecommerce_data.csv', index=False)
print("\n5. SAVED: cleaned_ecommerce_data.csv")

print("\n" + "=" * 50)
print("TRANSFORM COMPLETE")
print("=" * 50)


