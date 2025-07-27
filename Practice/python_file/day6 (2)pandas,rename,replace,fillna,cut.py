import pandas as pd

df = pd.read_csv('winemag-data-130k-v2.csv')

print(df.columns.tolist())

df.rename(columns={
  'country':'Country', 
  'description':'Description', 
  'designation':'Designation', 
  'points': 'Points', 
  'price': 'Price', 
  'province': 'Province', 
  'region_1':'Region', 
  'region_2': 'Subregion', 
  'taster_name': 'Reviewer', 
  'taster_twitter_handle': 'Twitter', 
  'title': 'Title', 
  'variety': 'Variety', 
  'winery':'Winery'
},inplace=True)

print(df.columns.tolist())

df['Wine_overview'] =df['Title']+ "|" +df['Country']+ "|" +df['Province']

print(df['Wine_overview'].head())

print(df.columns.tolist())


df['Country']= df['Country'].replace(
  {
    "US":"United States of America",
    "England":"United Kingdom"
  }
)

print(df[['Country']].head(35))

high_rated_wine = df[df['Points']>90]
print(high_rated_wine[['Country','Price','Points']].tail())

print(f"\nBefore fillna null rows count {high_rated_wine.isnull().sum()}")
high_rated_wine['Price'].fillna(1,inplace=True)
print(f"\n After fillna null rows count {high_rated_wine.isnull().sum()}")

df['Price'].fillna(1,inplace=True)
df['PriceCategory']=pd.cut(df['Price'],bins=[0,20,50,100,500,1000],
                           labels=['Budget','Standard','Good','Premium','Luxury'])

print(df[['Country','Price','PriceCategory']])
