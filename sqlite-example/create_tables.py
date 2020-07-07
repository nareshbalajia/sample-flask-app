import sqlite3

# create and connect to a local sqlite db
connection = sqlite3.connect("sample.db")

# create a cursor obj to interact with db
cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
