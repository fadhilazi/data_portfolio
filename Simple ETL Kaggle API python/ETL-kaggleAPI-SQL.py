#Importing kaggle API to vscode
import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('atharvasoundankar/chocolate-sales', path='.', unzip=True)


#replacing columns name into lower case and underscore
import pandas as pd
df = pd.read_csv('orders.csv')
print(df)
print(df.head(5))
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
print(df.columns)


#convert Amount column to Indonesian Rupiah
df['amount_clean'] = df['amount'].replace('[\$,]', '',regex = True). astype(float)
exchange_rate = 16000
df['amount_IR'] = df['amount_clean'] * exchange_rate
df['amount_IR'] = df['amount_IR']. astype(int)

df['amount_USD'] = df['amount'].replace(r'[\$,]', '',regex = True). astype(float)

df.drop(columns=['amount_clean'], inplace=True)

#change column date data-type into Date
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')
df.dtypes



#making an ID for each sales_person for Primary Key
print(df['sales_person'].unique())

df['sales_id'] = pd.factorize(df['sales_person'])[0] + 1

#moving sales_id column to the front row
cols = df.columns.tolist()
cols.remove('sales_id')
new_order = ['sales_id'] + cols
df = df[new_order]


#load the data into SQL Server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-SQALVDR\SQLEXPRESS/test?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn = engine.connect()
df.to_sql('chocolate_sales', engine, if_exists='replace', index=False)
print(f"Successfully imported {len(df)} rows into {'chocolate_sales'}.")

