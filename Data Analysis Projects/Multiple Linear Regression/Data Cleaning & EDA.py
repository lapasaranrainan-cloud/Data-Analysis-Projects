import pandas as pd
from dateutil import parser

df = pd.read_csv(r"D:\Data Analysis Projects\Multiple Linear Regression\kc_house_data (Cleaned Data).csv")

print(df.info())
print(df.head())
print(df.describe(include="all").T)
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

df.drop(columns=['date'], inplace=True)

#Remove Duplicates
before = len(df)

df.drop_duplicates(inplace=True)

after = len(df)

print(f"Removed {before-after} duplicate rows")

#Check Missing Values
missing = df.isnull().sum()

print(missing)

print(df)

print(df.info())

print(df.describe())

print(df.head())

print(df.shape)

print(df.columns)

df.to_csv(r"D:\Data Analysis Projects\Multiple Linear Regression\kc_house_data (Final Data).csv", index=False)


