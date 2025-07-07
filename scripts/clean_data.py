
import pandas as pd
import os

df = pd.read_csv('./data/raw_data.csv')

print("🔹 Original shape:", df.shape)

duplicates = df.duplicated().sum()
print("🔍 Duplicates found:", duplicates)

df = df.drop_duplicates()
print(" Removed duplicates. New shape:", df.shape)

missing = df.isnull().sum()
print("🔍 Missing values:\n", missing)

df = df.dropna()

df['date'] = pd.to_datetime(df['date'], errors='coerce')
print(" Converted 'date' to datetime.")

df = df.dropna(subset=['date'])

df = df.sort_values(by='date')

df.to_csv('./data/clean_data.csv', index=False)
print(f"🎉 Saved cleaned data with {len(df)} rows to data/clean_data.csv")
