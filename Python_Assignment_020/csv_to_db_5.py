# 5. Read books.csv and insert its data into the book table.

import csv
import sqlite3

# Open the CSV file and read the data
with open('books.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    rows = []
    for row in csvreader:
        if row:
            if len(row) == 3:
                rows.append((row[0], row[1], int(row[2])))
            else:
                print(f"Skipping row: {row}")

# Connect to the SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create a new table to store the data
cursor.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER)')

# Insert the data into the table
cursor.executemany('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', rows)

# Commit the changes and close the connection
conn.commit()
conn.close()
