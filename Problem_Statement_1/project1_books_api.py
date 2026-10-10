import requests
import sqlite3

# Step 1: Fetch book data from the API
url = "https://openlibrary.org/search.json?q=python&limit=5"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    # Step 2: Create a local SQLite database
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)

    # Step 3: Store the books in the database
    for book in data["docs"]:
        title = book.get("title", "Unknown title")
        authors = book.get("author_name", ["Unknown author"])
        author = ", ".join(authors)
        year = book.get("first_publish_year")

        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, year))

    connection.commit()

    # Step 4: Display the saved books
    cursor.execute("""
        SELECT title, author, publication_year FROM books
    """)

    print("\nBooks saved in the database:\n")

    for row in cursor.fetchall():
        print("Title:", row[0])
        print("Author:", row[1])
        print("Year:", row[2])
        print("-" * 30)

    connection.close()

except requests.RequestException as error:
    print("API request failed:", error)