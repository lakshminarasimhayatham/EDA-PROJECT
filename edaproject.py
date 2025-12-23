print("Hello This is Narasimha")
import pandas as pd
import numpy as np
df = pd.read_csv('data.csv', encoding = 'ISO-8859-1')
df.shape
df.head(2)
df.tail(2)
df.columns
for column in df.columns:
    print(column)
d = {
        'InvoiceNo': 'invoice_num',
        'StockCode' : 'stock_code',
        'Description' : 'description',
        'Quantity' : 'quantity',
        'InvoiceDate' : 'invoice_date',
        'UnitPrice' : 'unit_price',
        'CustomerID' : 'cust_id',
        'Country' : 'country'
}
d
df.rename(columns = d, inplace = True)
df.columns
for i in df.columns:
    print(i)
df.dtypes
df.info()
df.isnull()
len(df.columns)
df.shape
df.isnull().sum()
df.isnull().sum().sort_values()
df.isnull().sum().sort_values(ascending = False)
df.dtypes
df.head(2)
df['invoice_date'] = pd.to_datetime(df.invoice_date, format='%m/%d/%Y %H:%M')
df.dtypes
df.head(2)
df.description
df.description.str.lower()
df.head(2)
df['description'] = df.description.str.lower()
df.head(3)
df.isnull().sum().sort_values(ascending = False)
df_new = df.dropna()
df_new.isnull().sum()
df_new.isnull().sum()
df_new.head()

df_new.dtypes
df_new['cust_id']
import warnings
warnings.filterwarnings('ignore')
df_new['cust_id'] = df_new['cust_id'].astype('int64')

df_new.head(2)
df_new.info()

df_new.describe()
df_new.describe().round(2)

df_new.quantity > 0
con = df_new.quantity > 0
df_new = df_new[con]
df_new.describe().round(2)
df_new.head()
df_new.shape
df_new['amount_spent'] = df_new['quantity'] * df_new['unit_price']
df_new.head()
df_new['amount_spent'] = df_new['quantity'] * df_new['unit_price']
df_new.head()
col_order = ['invoice_num','invoice_date','stock_code','description','quantity','unit_price','amount_spent','cust_id','country']
df_new = df_new[col_order]
df_new.head()

df_new.shape
len(df_new.columns)
df_new['invoice_date']

df_new.invoice_date
df_new['invoice_date'].dt.year
df_new['invoice_date'].dt.month
df_new.head(2)

y = 2010
m = 12
y_m = 100*2010 + 12
y_m
201012
c1 = 'year_month'
v1 = df_new['invoice_date'].map(lambda col: 100*(col.year) + col.month)
df_new.insert(loc = 2, column = c1, value = v1)
df_new
df_new.head()
c2 = 'month'
v2 = df_new.invoice_date.dt.month
df_new.insert(loc = 3, column = c2, value = v2)
df_new.head()
df_new.invoice_date
df_new.invoice_date.dt.dayofweek
c3 = 'day'
v3 = (df_new.invoice_date.dt.dayofweek)+1
df_new.insert(loc = 4, column = c3, value = v3)
df_new.head()

df_new.invoice_date
c4 = "hour"
v4 = df_new.invoice_date.dt.hour
df_new.insert(loc = 5, column = c4, value = v4)
df_new.head()

df_new.columns
for col in df_new.columns:
    print(col)

df_new.groupby(by = ['cust_id','country'])['invoice_num'].count()
df_new.groupby(by = ['cust_id','country'], as_index = False)['invoice_num'].count()

import matplotlib.pyplot as plt
import seaborn as sns 
orders = df_new.groupby(by=['cust_id','country'], as_index=False)['invoice_num'].count()
orders
orders.sort_values(by = 'invoice_num', ascending = False).head()
orders = df_new.groupby(by=['cust_id','country'], as_index=False)['invoice_num'].count()

plt.subplots(figsize=(15,6))

plt.plot(orders.cust_id, orders.invoice_num)

plt.xlabel('Customers ID')
plt.ylabel('Number of Orders')
plt.title('Number of Orders for different Customers')
df_new.groupby(by = ['cust_id', 'country'])['amount_spent'].sum()
df_new.groupby(by = ['cust_id', 'country'], as_index = False)['amount_spent'].sum()
money_spent = df_new.groupby(by = ['cust_id', 'country'], as_index = False)['amount_spent'].sum()
money_spent
money_spent.sort_values(by='amount_spent', ascending = False).head()
money_spent.sort_values(by='amount_spent', ascending = False).head(10)
money_spent = df_new.groupby(by=['cust_id','country'], as_index=False)['amount_spent'].sum()

plt.subplots(figsize=(15,6))

plt.plot(money_spent.cust_id, money_spent.amount_spent)

plt.xlabel('Customers ID')
plt.ylabel('Money spent (Dollar)')
plt.title('Money Spent for different Customers')
df_new.head()
color = sns.color_palette()
df_new.head()
df_new.groupby('invoice_num')['year_month'].unique()

df_new.groupby('invoice_num')['year_month'].unique().value_counts()
ax = df_new.groupby('invoice_num')['year_month'].unique().value_counts().sort_index().plot(kind = 'bar',color = color[0],figsize = (15,6))

ax.set_xlabel('Month and Year',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders for different Months (1st Dec 2010 - 9th Dec 2011)', fontsize = 15)

t = ('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','Jun_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11','Dec_11')

ax.set_xticklabels(t, rotation='horizontal', fontsize=13)

df_new.groupby('invoice_num')['day'].unique()

df_new.groupby('invoice_num')['day'].unique().value_counts()

df_new.groupby('invoice_num')['day'].unique().value_counts().sort_index()

df_new.head()
df_new.groupby('invoice_num')['day'].unique()
df_new.groupby('invoice_num')['day'].unique().value_counts()
df_new.groupby('invoice_num')['day'].unique().value_counts().sort_index()

ax = df_new.groupby('invoice_num')['day'].unique().value_counts().sort_index().plot(kind = 'bar',color=color[0],figsize=(15,6))

ax.set_xlabel('Day',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders for different Days',fontsize=15)
d = ('Mon','Tue','Wed','Thur','Fri','Sun')
ax.set_xticklabels(d, rotation='horizontal', fontsize=15)

df_new.unit_price.describe()
plt.subplots(figsize = (12,6))

sns.boxplot(df_new.unit_price)
df_free = df_new[df_new.unit_price == 0]
len(df_free)
40
df_free.year_month
df_free.year_month.value_counts()
ax = df_free.year_month.value_counts().sort_index().plot(kind = 'bar',figsize=(12,6), color=color[0])
ax.set_xlabel('Month',fontsize=15)
ax.set_ylabel('Frequency',fontsize=15)
ax.set_title('Frequency for different Months (Dec 2010 - Dec 2011)',fontsize=15)

m = ('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11')

ax.set_xticklabels(m, rotation='horizontal', fontsize=13)
df_new
df_new.groupby('country')['invoice_num'].count()
df_new.groupby('country')['invoice_num'].count().sort_values()
group_country_orders = df_new.groupby('country')['invoice_num'].count().sort_values()
# del group_country_orders['United Kingdom']

# plot number of unique customers in each country (with UK)
plt.subplots(figsize=(15,8))
group_country_orders.plot(kind = 'barh', fontsize=12, color=color[0])
plt.xlabel('Number of Orders', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Number of Orders for different Countries', fontsize=12)
group_country_orders = df_new.groupby('country')['invoice_num'].count().sort_values()
del group_country_orders['United Kingdom']

# plot number of unique customers in each country (with UK)
plt.subplots(figsize=(15,8))
group_country_orders.plot(kind = 'barh', fontsize=12, color=color[0])
plt.xlabel('Number of Orders', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Number of Orders for different Countries', fontsize=12)
df_new
df_new.groupby('country')['amount_spent'].sum()
df_new.groupby('country')['amount_spent'].sum().sort_values()
group_country_amount_spent = df_new.groupby('country')['amount_spent'].sum().sort_values()
# del group_country_orders['United Kingdom']

# plot total money spent by each country (with UK)
plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind = 'barh', fontsize=12, color=color[0])
plt.xlabel('Money Spent (Dollar)', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Money Spent by different Countries', fontsize=12)
group_country_amount_spent = df_new.groupby('country')['amount_spent'].sum().sort_values()
del group_country_amount_spent['United Kingdom']

# plot total money spent by each country (without UK)
plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind = 'barh', fontsize=12, color=color[0])
plt.xlabel('Money Spent (Dollar)', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Money Spent by different Countries', fontsize=12)
plt.show()