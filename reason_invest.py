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

# checking risky investment
plt.figure(figsize=(18, 6))

plt.subplot(1, 2, 1)
sns.countplot(hue=df['gender'], x=df['Duration'], palette='viridis', linewidth=2, edgecolor='black')
plt.title("Duration")

plt.subplot(1, 2, 2)
sns.countplot(hue=df['gender'], x=df['Invest_Monitor'], palette='seismic', linewidth=2, edgecolor='black')
plt.title("Investment Monitoring")

plt.show()

