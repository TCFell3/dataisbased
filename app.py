import sqlite3

db = sqlite3.connect("treetable.db")
cursor = db.cursor()
sql = "SELECT * FROM thetreetable;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
