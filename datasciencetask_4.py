# -*- coding: utf-8 -*-
"""DATASCIENCETASK2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MJ-ud-gdi9BcETJFid2y2npeZM9ali-j

IMPORTING LIBRARIES
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

"""LOAD AND READ DATASET"""

df = pd.read_csv('/content/advertising.csv')
df.head()

df.info()

df.describe()

df.isna().sum()

"""EDA"""

sales_data = pd.read_csv('advertising.csv')
plt.figure(figsize=(10, 6))
sns.scatterplot(sales_data['Radio'],  marker='o', linestyle='-')
plt.title('Sales Over Time')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(sales_data['Radio'],linestyle='-')
plt.title('Sale prediction for news paper')
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.pairplot(df,hue='TV',height=2.5)
plt.show()

plt.scatter(df['TV'],df['Radio'])
plt.title("TV vs Radio")
plt.show()

sns.regplot(x='TV',y='Sales',data=df)
plt.title("TV vs Sales with Regression line")
plt.show()

plt.figure(figsize=(8,6))
df[['TV','Radio','Newspaper']].plot(kind='area')
plt.title("Sales prediction")
plt.show()

plt.figure(figsize=(8,6))
df[['TV','Radio','Newspaper']].sum().plot(kind='pie',autopct='%1.1f%%',colors=['red','green','blue'])
plt.title("Advertising distribution Pie chart Sales prediction")
plt.show()

corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True, cmap='coolwarm')
plt.title("Heatmap of Correlation matrix")
plt.show()

x=df[['TV','Radio','Newspaper']]
y=df['Sales']

"""TRAIN AND TEST"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_train_scaler=scaler.fit_transform(x_train)
x_test_scaler=scaler.fit_transform(x_test)

"""LINEAR REGRESSION"""

model=LinearRegression()
model.fit(x_train_scaler,y_train)

y_pred=model.predict(x_test_scaler)

msc=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("Mean square error:",msc)
print("R squared:",r2)

plt.scatter(y_test,y_pred)
plt.title("Actual vs Predicted sales")
plt.show()

plt.bar(y_test,y_pred,color=['blue','green'])
plt.title("Actual vs Predicted sales")
plt.show()

