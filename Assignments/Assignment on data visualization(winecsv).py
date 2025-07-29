import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('winemag-data-130k-v2.csv',index_col=0)

grouped = df.groupby('country')['points'].mean()
#print(grouped.head(10))
sorted_grouped = grouped.sort_values(ascending=False).head(10)
#print(sorted_grouped)


plt.figure(figsize=(10,5))
sorted_grouped.plot(kind='bar',color='teal')
plt.title('top 10 wine producing country with high average ratings')
plt.xlabel("Country")
plt.ylabel("average ratings")
plt.xticks(rotation=45)           
plt.tight_layout()
plt.show()



plt.figure(figsize=(10,5))
sorted_grouped.plot(kind='bar',color='orchid')
plt.title('Top 10 Countries by Average Wine Rating')
plt.xlabel("Country")
plt.ylabel("average price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

