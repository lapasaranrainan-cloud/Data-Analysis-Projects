import pandas as pd
from dateutil import parser

df = pd.read_csv(r"D:\Data Analysis\Data Analysis Projects\Superstore Sales\Raw Data.csv")

print(df.info())
print(df.head())
print(df.describe().T)
print(df.columns)

#Standardize column names
df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
)

#Trim
text_columns = df.select_dtypes(include="object").columns
for col in text_columns:
    df[col] = df[col].str.strip()

#Change Date Format
date_columns = [c for c in df.columns if "Date" in c]

for col in date_columns:
    df[col] = pd.to_datetime(
        df[col],
        format="mixed",
    )

#Remove Duplicates
before = len(df)

df.drop_duplicates(inplace=True)

after = len(df)

print(f"Removed {before-after} duplicate rows")

#Check Missing Values
missing = df.isnull().sum()

print(missing)

#Add columns
df["Shipping_Days"] = (df["Ship_Date"] - df["Order_Date"]).dt.days
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month_name()
df["Quarter"] = df["Order_Date"].dt.quarter

print(df.info())

print(df.describe())

print(df.head())

print(df.shape)

df.to_csv("D:\Data Analysis\Data Analysis Projects\Superstore Sales\Cleaned Data.csv", index=False)

