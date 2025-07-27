import pandas as pd

df = pd.read_csv('winemag-data-130k-v2.csv')

#df_types

print(df.dtypes)
print()
df['country']=df['country'].astype('string')
df['points']=df['points'].astype("Int32")
print()
print(df.dtypes)

#to numeric
df['price']=pd.to_numeric(df['price'],errors='ignore')
print(df['price'])

# # autmatic Type conversion
df=df.convert_dtypes()

print(df.isnull().head()[['country','price','points']])
print(df.notnull().head()[['country','price','points']])
print(df.isna().head()[['country','price','points']])

mask = df.isnull().any(axis=1)
print(df[mask].head()[['country','price','points']])  # masking printing data which return s true for isnull ..ie null row alone
print(df.isnull().any(axis=1).head())


print("before:")
print(df['price'].isnull().head(35))
print(df['price'].isnull().sum())
df['price']= df['price'].fillna(0)
print()
print("after: ")
print(df['price'].isnull().head(35))
print(df['price'].isnull().sum())


#forward fill
print(df[['country','price']].head(20))
df_ffill = df[['country','price']].copy()
df_ffill.ffill(inplace=True)  # null value takes above value
print(df_ffill.head(20))

# backward fill
print(df[['country','price']].head(20))
df_bfill = df[['country','price']].copy()  #null value takes below value
df_bfill.bfill(inplace= True)
print(df_bfill.head(20))

print(len(df))
print(df.isnull().any(axis=1).sum())
print()
df=df.dropna()   #removes all row with null value
print()
print(len(df))
print(df.isnull().any(axis=1).sum())

df.to_csv('removed_null_from_winemag.csv')
