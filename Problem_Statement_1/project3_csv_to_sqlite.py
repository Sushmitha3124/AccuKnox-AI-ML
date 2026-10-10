
import csv
import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
""")

try:
    with open(
        "Problem_Statement_1/users.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"].strip()
            email = row["email"].strip()

            if name and email:
                cursor.execute("""
                    INSERT OR IGNORE INTO users (name, email)
                    VALUES (?, ?)
                """, (name, email))

    connection.commit()
    print("CSV data imported successfully!")

except (OSError, KeyError, sqlite3.Error) as error:
    connection.rollback()
    print("Error:", error)

finally:
    connection.close()
