import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print("Total books:", cursor.fetchone()[0])

cursor.execute("SELECT title, author, publication_year FROM books")

for book in cursor.fetchall():
    print(book)

connection.close()