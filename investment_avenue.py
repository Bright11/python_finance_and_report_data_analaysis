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
plt.figure(figsize=(18,6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['gender'], linewidth=3, palette='summer', edgecolor="white", hue=df['Investment_Avenues'])
plt.xlabel('Investment Avenues')
plt.ylabel('Count')
plt.title('Investment Avenues')
plt.tight_layout()

plt.subplot(1, 2, 2)
sns.countplot(x=df['gender'], linewidth=3, hue=df['Stock_Marktet'], palette='hot', edgecolor="white")
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender vs Stock Market')
plt.tight_layout()
plt.savefig('Investment_Avenue.png')
plt.show()


plt.show()

