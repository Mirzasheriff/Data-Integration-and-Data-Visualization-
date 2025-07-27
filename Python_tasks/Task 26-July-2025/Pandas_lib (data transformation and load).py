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


#================================================================================================================================================================

import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")

#print(df[df['country'].isin(['Span','India','Turkey'])]) #country match

#print(df[df['country'].str.contains("la",case=False,na=False)]['country']) #newzealand,poland,iceland,greenland...

#isnull
#print(df[df['price'].isnull()][['country','title']])
#notnull
#print(df[df['price'].notnull()][['title','country']])


#filter duplicated
#print(df[df.duplicated('title',keep=False)])

#unique without deleting anything

#title_counts = df['title'].value_counts()
#print(title_counts[title_counts>1])

# #Filter Duplicates
# duplcate_df=df[df.duplicated('title',keep=False)]
# print(duplcate_df[['title','points','price']])


# # Keep Only First Occurance and drop the rest
# df_no_duplicates=df.drop_duplicates(subset='title',keep='first')
# print(df_no_duplicates[['title','points','price']].head(20))

# # Display unique Row of Title column
# unique_titles=df[df.duplicated('title',keep=False)]['title'].unique()
# print(unique_titles)

# # howmany time each title occurs
# title_counts=df['title'].value_counts();
# print(title_counts[title_counts>1])


# find the Duplicates in Multiple column
multi_column_duplicates=df[df.duplicated(subset=['title','points'],keep=False)]
print(multi_column_duplicates[['title','points','country']])


#=============================================================================================================================================================================


#group by sorting
import pandas as pd

df=pd.read_csv("winemag-data-130k-v2.csv")

# # Groupby
# print(df.groupby('country')['points'].mean())

# #Group By Multiple Colummns
# print(df.groupby(['country','variety'])['points'].mean())

# # Groupig with multiple Aggreagetion
# print(df.groupby('country')['points'].agg(['mean','min','max','count']))


# # naming Aggregated columns
# print(
#     df.groupby('country').agg(
#         avg_points=('points','mean'),
#         total_reviews=('points','count')
#        ))

# # Filter with Group by
# print(df.groupby('country').filter(lambda x :len(x)>1000))


# # Apply the Logic 
# print(df.groupby('country').apply(lambda x:x[x['points']>95])[['country','points']])

# # Sort by column
# print(df.sort_values(by='points',ascending=False)['points'])

# # Sorting Multiple Columns
# print(df.sort_values(by=["country","points"],ascending=[True,False])[['country','points']])

# # Sorting After Grouping
# grouped=df.groupby('country')['points'].mean()
# grouped_sorted=grouped.sort_index(ascending=True)
# print(grouped_sorted)

# #Sorting Aggregated Results
# print(df.groupby('country')['points'].mean().sort_values(ascending=False))

#Flatterned the grouped result back
# print(df.groupby('country')['points'].mean().reset_index()) #converting series into dataframe using reset_index
