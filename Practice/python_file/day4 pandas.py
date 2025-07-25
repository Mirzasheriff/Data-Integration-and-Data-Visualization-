import pandas as pd


##.dataframe
df1 = pd.DataFrame({
  'Team 1': [10,20,30],
  'Team 2': [20,30,20]
})

print(df1)
print()
print()

df2 = pd.DataFrame({
  'Team 1': [10,20,30],
  'Team 2': [20,30,20]},index = ['cmt1','cmt2','cmt3'])

print(df2)

##.Series
oddseries = pd.Series([100,200,300])
print(oddseries)

odded_series = pd.Series([100,200,300],index = ['row1','row2','row3'],name = 'datas')
print(odded_series)


##.connecting csv file
wine_review = pd.read_csv('winemag-data-130k-v2.csv')

#operations with csv file
print(wine_review.head()) ## top 5 row
print(wine_review.country) ##all countries dot notation
print(wine_review['country']) ##all countries box notation
print(wine_review['country'].iloc[3]) ## 3rd country
print(wine_review.iloc[:,0]) ##all rows of 0th column
print(wine_review.iloc[:3,1]) ##3 rows one col
print(wine_review.iloc[:1,3]) ## one col, 3 rows
print(wine_review.iloc[[1,3,5,7,8],1]) ##1st col of row 1,3,5,7,8
print(wine_review.iloc[[1,3,5,7,8],[1,2]]) ##1st and 2nd col of orw 1,3,5,7,8
print(wine_review.iloc[-5]) ##last 5th row
print(wine_review.iloc[5]) ##5th row


#selecting based on label
print(wine_review.loc[10,'country'])  ##US
print(wine_review.iloc[10,'country']) ##error
print(wine_review) ##native accessor -- i.e access all 


#select specific columns
new_rev = wine_review.loc[:,['country','points','price']]
print(new_rev)   ##displays only thse 3 col all rows

# set index
print(wine_review.set_index('winery')) ##winery col comes first

#conditional selections
print(wine_review.country=='France') ##compares and returns false or true for each row
print(wine_review.loc[wine_review.country== 'France']) ##matched data
print(wine_review.loc[(wine_review.country=='France')&(wine_review.price>60)]) ##returns based on both conditions
print(wine_review.loc[(wine_review.country=='France')&(wine_review.price>60),['country','price']]) ##same as above but only 2 specific col
print(wine_review.loc[wine_review.country.isin(['France','Italy']),['country','price']]) ##2 countries only 2 col
print(wine_review.loc[wine_review.price.notnull()]) ##returns record tahats price are notnull
wine_review['test_column']= 'test1'  ##adds new column
print(wine_review)

#summary function
print(wine_review.describe()) ##shows count,mean,min,max...
print(wine_review.country.describe())
print(wine_review.price.mean())
print(wine_review.title.mean())
print(wine_review.title.unique())
print(wine_review.country.value_counts()) ##each country count

print(wine_review.country.value_counts().get("Argentina")) ##specific country count
##or
print((wine_review.country=='Argentina').sum())  ##specific country count
##or
print(wine_review.loc[wine_review.country=='Argentina'].shape[0])  ##specific country count











