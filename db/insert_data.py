import os
import psycopg2
conn = psycopg2.connect(
    host='185.4.180.217',
    database='kaznudb',
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])
# Open a cursor to perform database operations
cur = conn.cursor()
with open('data.sql', 'r') as f:
    sql = f.read()
cur.execute(sql)
conn.commit()
cur.close()
conn.close()