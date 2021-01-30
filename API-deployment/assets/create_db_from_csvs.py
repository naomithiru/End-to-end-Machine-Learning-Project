import sqlite3
import pandas as pd
conn = sqlite3.connect("db/mydatabase.db")  # or use :memory: to put it in RAM
cursor = conn.cursor()
df = pd.read_csv('assets/def_dataset.csv')
print(df.columns.values)
df.to_sql(name='scrapped', con=conn, if_exists='replace')
df.to_sql(name='cleaned', con=conn, if_exists='replace')
conn.commit()
conn.close()
