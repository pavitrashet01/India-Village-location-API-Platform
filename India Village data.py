# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:49:17 2026

@author: pavitra
"""


import pandas as pd
import glob

# Read all .xls files
files = glob.glob(r"C:\Users\pavitra\Downloads\all-india-villages-master-list-excel\dataset\*.xls")

df_list = []

for file in files:
    try:
        temp_df = pd.read_excel(file, engine='xlrd')  # use temp variable
        df_list.append(temp_df)
    except Exception as e:
        print(f"Error in file {file}: {e}")

# Combine all files
df = pd.concat(df_list, ignore_index=True)

print("Files combined successfully!")

# Check data
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.columns)


# remove blank columns
df = df.drop(columns=df.filter(like='Unnamed'))


print(df.info())
print(df.isnull().sum())

# Remove null values
df = df.dropna()



# check for duplicates
df.duplicated().sum()


# Fix data types (float → int)
num_cols = df.select_dtypes(include='float').columns
df[num_cols] = df[num_cols].astype(int)

# Renaming column names
df.rename(columns={
    "MDDS STC": "state_code",
    "STATE NAME": "state",
    "MDDS DTC": "district_code",
    "DISTRICT NAME": "district",
    "MDDS Sub_DT": "sub_district_code",
    "SUB-DISTRICT NAME": "sub_district",
    "MDDS PLCN": "village_code",
    "Area Name": "village"
}, inplace=True)



# Save cleaned data (FINAL STEP)
df.to_csv(r"C:\Users\pavitra\Desktop\capstone project\cleaned_data.csv", index=False)


print("Cleaned file saved successfully ✅")







from sqlalchemy import create_engine, text
import pandas as pd

# 🔹 Step 1: Database connection details
username = "root"
password = "2298"
host = "localhost"
port = "3306"
database = "village_db"   # use your project DB name

# 🔹 Step 2: Create engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# 🔹 Step 3: Load your cleaned CSV
df = pd.read_csv(r"C:\Users\pavitra\Desktop\capstone project\cleaned_data.csv")

# 🔹 Step 4: Upload to MySQL (optimized for large data)
table_name = "villages"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",   # replace or append
    index=False,
    chunksize=10000        # IMPORTANT for large data (4 lakh rows)
)

print("Data uploaded successfully ✅")

# 🔹 Step 5: Verify data
with engine.connect() as connection:
    df_sample = pd.read_sql(text("SELECT * FROM villages LIMIT 5;"), connection)

print(df_sample)









