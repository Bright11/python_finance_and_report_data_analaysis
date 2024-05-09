# numpy
# pip install pandas
# pip install seaborn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')

# reading csv files
df=pd.read_csv('Finance_data.csv')
df.head()
print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())
# print(df.corr())

df.drop(['Mutual_Funds','Equity_Market','Government_Bonds','PPF','Fixed_Deposits','Gold'], axis=1, inplace=True)
# replacing an empty colunms
# df.fillna(0, inplace=True)
df.replace(r'^\s*$', np.nan, regex=True)

# checking how many male and fimale are investing
sns.countplot(x='gender', data=df, linewidth=3, hue='gender', palette='Set2', edgecolor="black")
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Investing')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('gender_invest.png')

plt.show()

