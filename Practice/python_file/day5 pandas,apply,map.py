import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")


country_map = {"US":"USA",
               "England":"UK",
               "South Africa":"Africa"
               }

df['new_country_category']=df['country'].map(country_map).fillna(df['country'])
print(df[['country','new_country_category']])

#print(len(df.columns))

def price_category(price):
  if pd.isna(price):
    return "Unknown"
  elif price<20:
    return "Budget"
  elif price<50:
    return "Standard"
  elif price<100:
    return "Premium"
  else:
    return "Luxury"
  
df['price_category'] = df['price'].apply(price_category) #also works with apply instaed of map and vice-versa

df['points_grade']= df['points'].map(lambda x: 'High' if x>90 else 'low')



df['quality_label'] = df['points'].apply(lambda x: 'excellent' if x>95 else
                                       'very good' if x>90 else
                                       'good' if x>85 else
                                       'average')

print(df[['country','new_country_category','price_category','points_grade','quality_label']])


df.to_csv("transformed_data.csv",index=False)

