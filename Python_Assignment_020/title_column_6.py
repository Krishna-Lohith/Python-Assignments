# 6. Select and print the title column from the book table in alphabetical order.

# This file can't be open in our local systems.
import sqlite3

# Connecting
my_conn = sqlite3.connect('books.db') 

# creating a cursor
my_cur = my_conn.cursor()

my_cur.execute('PRAGMA table_info(books)')
x = my_cur.fetchall()
header = [i[1] for i in x]
header_sorted = sorted(header)

for j in header_sorted:
    print(j)

my_conn.commit()
my_conn.close()