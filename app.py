import sqlite3

DATABASE = "treetable.db"


def print_all_trees():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name          Fruit     Flower   Max Height")
    for thetreetable in results:
        print(f"{thetreetable[1].title():<14}{thetreetable[2].title():10}{thetreetable[3].title():9}{thetreetable[4]}")
    db.close()


def print_all_trees_by_height():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable ORDER BY maxheight ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name          Fruit     Flower   Max Height")
    for thetreetable in results:
        print(f"{thetreetable[1].title():<14}{thetreetable[2].title():10}{thetreetable[3].title():9}{thetreetable[4]}")
    db.close()


def print_all_trees_by_fruit():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable ORDER BY fruit DESC ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name          Fruit     Flower   Max Height")
    for thetreetable in results:
        print(f"{thetreetable[1].title():<14}{thetreetable[2].title():10}{thetreetable[3].title():9}{thetreetable[4]}")
    db.close()


def print_all_trees_by_flower():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable ORDER BY flower DESC ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name          Fruit     Flower   Max Height")
    for thetreetable in results:
        print(f"{thetreetable[1].title():<14}{thetreetable[2].title():10}{thetreetable[3].title():9}{thetreetable[4]}")
    db.close()


def print_all_trees_by_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM thetreetable ORDER BY name ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name          Fruit     Flower   Max Height")
    for thetreetable in results:
        print(f"{thetreetable[1].title():<14}{thetreetable[2].title():10}{thetreetable[3].title():9}{thetreetable[4]}")
    db.close()


while True:
    user_input = input(
"""
What would you like to do?
\n1. Print all trees
\n2. Print all trees by height
\n3. Print all trees by whether they fruit
\n4. Print all trees by whether they flower
\n5. Print all trees by alphabetical order
\n6. Stop\n
""")
    if user_input == "1":
        print_all_trees()
    elif user_input == "2":
        print_all_trees_by_height()
    elif user_input == "3":
        print_all_trees_by_fruit()
    elif user_input == "4":
        print_all_trees_by_flower()
    elif user_input == "5":
        print_all_trees_by_name()
    elif user_input == "6":
        break
    else:
        print("That was not an option\n")

