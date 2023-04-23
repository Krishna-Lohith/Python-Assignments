# 4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields:
# title (text), author (text), and year (integer).

import sqlite3

# Connecting
my_conn = sqlite3.connect('books.db') 

# creating a cursor
my_cur = my_conn.cursor()

my_cur.execute('''CREATE TABLE books (title text, author text, year integer)''')

my_cur.execute('Insert into table books values( )')

my_conn.commit()
my_conn.close()