import psycopg2;

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres1",
    port=5300
)

cur = con.cursor()

cur.execute("select id,name from employee")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} and name {r[1]}")

cur.close()

con.close()

