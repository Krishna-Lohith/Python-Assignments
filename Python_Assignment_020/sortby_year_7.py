# 7. From the book table, select and print all columns in the order of publication.

import sqlite3

# Connecting
my_conn = sqlite3.connect('books.db') 

# creating a cursor
my_cur = my_conn.cursor()

my_cur.execute('select * from books order by year')
x = my_cur.fetchall()
for i in x:
    print(i)

my_conn.commit()
my_conn.close()