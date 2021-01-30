import sqlite3
import pandas as pd
conn = sqlite3.connect("db/mydatabase.db")
cursor = conn.cursor()
cursor.execute("""Select 'source', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
 'rooms_number', 'equipped_kitchen_has', 'garden', 'garden_area', 'terrace',
 'terrace_area', 'furnished', 'swimming_pool_has', 'land_surface', 'basement',
 'building_state_agg', 'open_fire', 'longitude', 'latitude' from cleaned""")
df = pd.DataFrame(cursor.fetchall())
print(df)
# del df[20]
# df = df.drop(20, 1)
# print(df)
# # df.to_sql(name='cleaned', con=conn, if_exists='replace')
# # print(df)
# # df.drop(columns=['19', '20'])
# cursor.execute('drop table cleaned;')
# conn.commit()
# conn.close()
# conn = sqlite3.connect("db/mydatabase.db")
# cursor = conn.cursor()
# # cursor.execute("""Select * from cleaned""")
# # df = pd.DataFrame(cursor.fetchall())
# df.to_sql(name='cleaned', con=conn)
# conn.commit()
# # print(df)
conn.close()
