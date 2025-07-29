import matplotlib.pyplot as plt

x = [1,2,4,6,8]
y = [10,34,21,78,9]

plt.plot(x,y)
plt.title("Demo")
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.show()

#===================================data visualiation ==============================================

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('winemag-data-130k-v2.csv',index_col=0)
country_count = df['country'].value_counts().head(20)
plt.figure(figsize=(10,5))
country_count.plot(kind='bar',color='teal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
