import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")

print(df[df['country'].isin(['Span','India','Turkey'])]) #country match

print(df[df['country'].str.contains("la",case=False,na=False)]['country']) #newzealand,poland,iceland,greenland...

#isnull
print(df[df['price'].isnull()][['country','title']])
#notnull
print(df[df['price'].notnull()][['title','country']])


#filter duplicated
print(df[df.duplicated('title',keep=False)])

#unique without deleting anything

title_counts = df['title'].value_counts()
print(title_counts[title_counts>1])

#Filter Duplicates
duplcate_df=df[df.duplicated('title',keep=False)]
print(duplcate_df[['title','points','price']])


# Keep Only First Occurance and drop the rest
df_no_duplicates=df.drop_duplicates(subset='title',keep='first')
print(df_no_duplicates[['title','points','price']].head(20))

# Display unique Row of Title column
unique_titles=df[df.duplicated('title',keep=False)]['title'].unique()
print(unique_titles)

# howmany time each title occurs
title_counts=df['title'].value_counts();
print(title_counts[title_counts>1])


# find the Duplicates in Multiple column
multi_column_duplicates=df[df.duplicated(subset=['title','points'],keep=False)]
print(multi_column_duplicates[['title','points','country']])
