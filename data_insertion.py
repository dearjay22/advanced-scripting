import pymysql
import random

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Secret123',
    database='prog8850'
)

cursor = conn.cursor()

for i in range(1, 501):
    name = f'Name_{i}'
    age = random.randint(18, 80)
    email = f'email_{i}@example.com'

    cursor.execute(
        "INSERT INTO large_table (name, age, email) VALUES (%s, %s, %s)",
        (name, age, email)
    )

conn.commit()
cursor.close()
conn.close()

print("500 rows inserted.")
