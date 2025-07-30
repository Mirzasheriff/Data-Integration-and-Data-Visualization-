import pandas as pd
import pyodbc

conn = pyodbc.connect(
  'DRIVER={ODBC DRIVER 17 for SQL Server};'
  'SERVER=MIRZA-SHERIFF;'
  'DATABASE=sql_py_read;'
  'Trusted_Connection=yes;'
  'TrustedServerCertificate=true'
)

query = "select * from CustomerOrders"
df = pd.read_sql(query,conn)

#general basic data cleaning
df['CustomerName'] = df['CustomerName'].str.strip().str.title()

mask = df['Email'].fillna('').str.contains(r'[A-Z]')
upper_case_emails = df[mask]

#print(upper_case_emails.head(10))

df['Email'] = df['Email'].str.lower()
df['Quantity'].fillna(1,inplace=True)
df['PricePerUnit'].fillna(df['PricePerUnit'].mean(),inplace=True)
df['OrderDate'].fillna(method='ffill',inplace=True)


df_cleaned = df.drop_duplicates()
duplicates = df_cleaned.duplicated(keep=False)
#print(duplicates)

df_cleaned['Total Price'] = df_cleaned['Quantity']*df_cleaned['PricePerUnit']

print(df_cleaned.head())

