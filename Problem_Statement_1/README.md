# AccuKnox AI/ML Trainee Assignment

## Problem Statement 1

### Project 1: Fetch Books from an API and Store in SQLite
- Used Python Requests to fetch book data from the Open Library REST API.
- Stored book titles, authors, and publication years in SQLite.
- Retrieved saved records to verify the database.

**File:** `project1_books_api.py`

### Project 2: Fetch Student Scores and Calculate Average
- Created a REST API using Flask to return student test scores.
- Used Python Requests to fetch student data from the API.
- Calculated the average score using Python statistics.
- Created a bar chart using Matplotlib.

**Files:** `student_api.py`, `project2_student_scores.py`

### Project 3: Import CSV Data into SQLite
- Read user names and email addresses from a CSV file.
- Created a SQLite users table.
- Inserted user records and checked the saved data.

**Files:** `users.csv`, `project3_csv_to_sqlite.py`, `check_users.py`

## Technologies Used
- Python
- REST APIs
- Flask
- SQLite
- CSV
- Requests
- Matplotlib

## How to Run
Run commands from the main assignment folder. Start the Flask API in one terminal before running Project 2 in another terminal.

```bash
python Problem_Statement_1/project1_books_api.py
python Problem_Statement_1/student_api.py
python Problem_Statement_1/project2_student_scores.py
python Problem_Statement_1/project3_csv_to_sqlite.py
python Problem_Statement_1/check_users.py
```

Note: The student API server must remain running while Project 2 is exe