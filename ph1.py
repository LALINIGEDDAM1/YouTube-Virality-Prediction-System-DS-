import pandas as pd

print("="*60)
print("PHASE 1 : DATASET LOADING & VERIFICATION")
print("="*60)

# Absolute path of dataset
file_path = r"C:\Projects\Youtube_trending(Datascience)\youtube.csv"

# Load dataset
df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully!")

# Shape
print("\nShape (Rows, Columns):", df.shape)

# Column Names
print("\nColumns:")
for col in df.columns:
    print(col)

# Preview
print("\nFirst 5 Rows:")
print(df.head())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nPHASE 1 COMPLETED")
