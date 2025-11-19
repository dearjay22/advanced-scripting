import pymysql
import threading
import pandas as pd

def execute_query_to_csv(query, output_filename):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Secret123",
        database="prog8850"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=["id", "name", "age", "email"])
    df.to_csv(output_filename, index=False)
    print(f"Saved {len(df)} rows to {output_filename}")
    cursor.close()
    conn.close()

jobs = [
    ("SELECT * FROM large_table WHERE age < 30", "results_age_below_30.csv"),
    ("SELECT * FROM large_table WHERE age >= 30 AND age < 60", "results_age_30_60.csv"),
    ("SELECT * FROM large_table WHERE age >= 60", "results_age_60_plus.csv")
]

threads = []
for query, filename in jobs:
    t = threading.Thread(target=execute_query_to_csv, args=(query, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All CSV exports completed.")
