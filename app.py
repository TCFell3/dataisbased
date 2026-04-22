import sqlite3

DATABASE = "treetable.db"


def print_all_trees():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for thetreetable in results:
        print(f"{thetreetable[1]:<10}{thetreetable[2]:<10}{thetreetable[3]:<10}{thetreetable[4]:<10}")
    db.close()


print_all_trees()
