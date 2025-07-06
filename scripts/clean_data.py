# scripts/clean_data.py

import pandas as pd
import os

# ✅ Load raw data
df = pd.read_csv('./data/raw_data.csv')

print("🔹 Original shape:", df.shape)

# ✅ Step 1: Check for duplicates
duplicates = df.duplicated().sum()
print("🔍 Duplicates found:", duplicates)

df = df.drop_duplicates()
print("✅ Removed duplicates. New shape:", df.shape)

# ✅ Step 2: Handle missing values
missing = df.isnull().sum()
print("🔍 Missing values:\n", missing)

# For this dataset, we expect no missing. If found, drop or fill them:
df = df.dropna()

# ✅ Step 3: Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')
print("✅ Converted 'date' to datetime.")

# ✅ Drop rows where date conversion failed
df = df.dropna(subset=['date'])

# ✅ Step 4: Sort by date
df = df.sort_values(by='date')

# ✅ Step 5: Save to new CSV
df.to_csv('./data/clean_data.csv', index=False)
print(f"🎉 Saved cleaned data with {len(df)} rows to data/clean_data.csv")
