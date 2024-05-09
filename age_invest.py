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
# sns.countplot(x='age', data=df, linewidth=3, palette='Set2', edgecolor="black")
sns.countplot(x='age', data=df, linewidth=3, hue='age', palette='Set2', edgecolor="black", legend=False)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Investing')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('age_invest.png')
# plt.savefig('age_invest.pdf')
# plt.savefig('age_invest.svg')
# plt.savefig('age_invest.eps')
# plt.savefig('age_invest.jpg')
# plt.savefig('age_invest.jpeg')
# plt.savefig('age_invest.tif')
# plt.savefig('age_invest.tiff')
# plt.savefig('age_invest.bmp')
# plt.savefig('age_invest.png')
# plt.savefig('age_invest.ppm')
# plt.savefig('age_invest.pgm')
# plt.savefig('age_invest.pbm')
# plt.savefig('age_invest.pnm')


plt.show()

