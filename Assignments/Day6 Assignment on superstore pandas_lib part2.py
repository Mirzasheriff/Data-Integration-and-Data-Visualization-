import pandas as pd

# Task 1: Extract and Preview the Data
#     Q1. The Superstore sales team has shared a new CSV file. Load the dataset and give a preview of the top 5 records to validate its structure.
#     Load Superstore.csv into a DataFrame.
#     Check number of rows and columns.
#     Display column names and their data types.

df = pd.read_csv('Superstore.csv')
no_of_rows = len(df['Row ID'])
col_names = df.columns.to_list()
col_len = len(col_names)
datatypes_of = df.dtypes
# print(df.head())
# print(f"the number of rows are {no_of_rows} and the no of columns are {col_len}")
# print(datatypes_of)


# Task 2: Clean Column Names and Normalize Dates
#     Q2. Some columns have inconsistent names with spaces and slashes. Also, the dates are strings. Clean the column names and convert Order Date and Ship Date to datetime format so that you can later group data by month.
#     Clean column headers using .str.replace().
#     Convert Order_Date and Ship_Date to datetime64.

df.rename( columns= {
  'Row ID':'Row_id', 
  'Order ID':'Order_id', 
  'Order Date':'Order_date', 
  'Ship Date':'Ship_date', 
  'Ship Mode':'Ship_mode', 
  'Customer ID':'Customer_id', 
  'Customer Name': 'Customer_name', 
  'Postal Code':'Postal_code', 
  'Product ID':'Product_id', 
  'Product Name':'Product_name', 
},inplace=True)

df['Order_date'] = df['Order_date'].astype('datetime64[ns]')
df['Ship_date'] = df['Ship_date'].astype('datetime64[ns]')
# print(df.head()[['Row_id','Order_date','Ship_date']])
# print(df.dtypes)


# Task 3: Profitability by Region and Category
# Q3. The regional manager wants to know which region and category combinations are most profitable. Summarize total Sales, Profit, and average Discount grouped by Region and Category.
#     Use groupby() + agg() to generate the report.
#     Identify which Region+Category had highest profit.

grouped = df.groupby(['Region','Category']).agg({
  'Sales':'sum',
  'Profit':'sum',
  'Discount':'mean'
}).reset_index()

highest_profit = grouped.sort_values(by='Profit',ascending=False).head(1)
# print(grouped)
# print(highest_profit)


# Task 4: Top 5 Most Profitable Products
# Q4. The product team is planning to promote high-profit items. Identify the top 5 products that contributed the most to overall profit.
#     Group by Product_Name, sum the profit, sort descending, and take top 5.

high_products = df.groupby('Product_name')['Profit'].sum().sort_values(ascending=False).head(5)
# print(high_products)


# Task 5: Monthly Sales Trend
# Q5. The leadership team wants to review monthly sales performance to understand seasonality. Prepare a month-wise sales trend report.
#     Extract month from Order_Date
#     Group by month and sum Sales

df['Month']=df['Order_date'].dt.to_period('M')
monthly_report = df.groupby('Month')['Sales'].sum().reset_index().head(20)
#print(monthly_report)



# Task 6: Cities with Highest Average Order Value
# Q6. The business is interested in targeting high-value cities for marketing. Calculate the average order value (Sales ÷ Quantity) for each city and list the top 10.
#     Create a new column Order_Value
#     Group by City and calculate average order value
#     Sort and get top 10

df['Order_value'] = df['Sales']/df['Quantity']
order_val = df.groupby('City')['Order_value'].mean().sort_values(ascending=False).head(10)
#print(order_val)



# Task 7: Identify and Save Orders with Loss
# Q7. Finance wants to analyze all loss-making orders. Filter all records where Profit < 0 and save it to a new file called loss_orders.csv.
#     Use boolean filtering
#     Export the filtered DataFrame to a CSV file without index

loss_products = df[df['Profit']<0]
loss_products.to_csv('loss_making_sales.csv',index=False)



# Task 8: Detect Null Values and Impute
# Q8. Are there any missing values in the dataset? If yes, identify columns with nulls and fill missing Price values with 1.
#     Use isnull().sum()
#     Apply fillna() only on Price column

df['Null_data'] = df['Sales']/df['Quantity']
counting = df['Null_data'].isnull().sum()
#print(counting)
df['Null_data']=df['Null_data'].fillna(1)
counting1 = df['Null_data'].isnull().sum()
#print(counting1)
