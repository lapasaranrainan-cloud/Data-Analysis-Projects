import pandas as pd
from sqlalchemy import create_engine

# Read cleaned data
df = pd.read_csv(
    r"D:\Data Analysis\Data Analysis Projects\Superstore Sales\Cleaned Data.csv"
)

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:*******@localhost:3306/superstore"
)

# Upload data
df.to_sql(
    "sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Upload successful")

