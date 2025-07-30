import pandas as pd
import sqlite3

df_csv = pd.read_csv("sales_csv.csv")

df_excel = pd.read_excel("sales_excel.xlsx")

df_json = pd.read_json("sales_json.json")

conn = sqlite3.connect("sales_db.sqlite")
df_sql = pd.read_sql("select * from Sales",conn)

df_combined = pd.concat([df_csv,df_excel,df_json,df_sql],ignore_index=True)
print(df_combined)
