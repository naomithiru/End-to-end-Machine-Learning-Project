import sqlite3
import pandas as pd
conn = sqlite3.connect("db/mydatabase.db")  # or use :memory: to put it in RAM
cursor = conn.cursor()
cursor.execute('drop table cleaned;')
conn.commit()
conn.close()
