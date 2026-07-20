from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM artists")

for row in cursor.fetchall():
    print(dict(row))

conn.close()
