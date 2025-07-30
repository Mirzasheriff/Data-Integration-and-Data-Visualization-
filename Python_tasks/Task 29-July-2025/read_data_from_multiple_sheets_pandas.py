import pandas as pd

file_path = "CustomerSales_2025.xlsx"

sheet_names = pd.ExcelFile(file_path).sheet_names

print(sheet_names)  #['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

df_jan = pd.read_excel(file_path,sheet_name=sheet_names[0])
print(df_jan)
print()
df_feb = pd.read_excel(file_path,sheet_name=sheet_names[1])
print("feb data :")
print(df_feb)

df_combined = pd.concat([pd.read_excel(file_path,sheet_name=sheet)for sheet in sheet_names])

print(df_combined)

df_combined.reset_index(drop=True,inplace=True)

print(df_combined)

df_combined.to_csv("CustomerSales2025Combines.csv")
