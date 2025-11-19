import pymysql
import cProfile
import pstats

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Secret123",
    database="prog8850"
)
cursor = conn.cursor()

def fetch_large_data():
    print("Running Optimize query...")
    cursor.execute("""
                SELECT *
                FROM large_table
                WHERE id >= FLOOR(RAND() * (SELECT MAX(id) FROM large_table))
                LIMIT 100
                """)
    results = cursor.fetchall()
    print("Done.")
    return results

cProfile.run('fetch_large_data()', 'profile_output')

p = pstats.Stats('profile_output')
p.sort_stats('cumulative')
p.print_stats(10)

cursor.close()
conn.close()
print("Connection closed.")
