
import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("SELECT id, name, email FROM users")

for user in cursor.fetchall():
    print(user)

connection.close()
