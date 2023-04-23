"""
3. Create a CSV file called books.csv by using these lines:  
title,author,year  
The Weirdstone of Brisingamen,Alan Garner,1960  
Perdido Street Station,China Miéville,2000  
Thud!,Terry Pratchett,2005  
The Spellman Files,Lisa Lutz,2007   
Small Gods,Terry Pratchett,1992  
"""


import csv

data = data = [
    ['title', 'author', 'year'],['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],['Perdido Street Station', 'China Miéville', '2000'],['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992']
]

#Writing data.
with open('books.csv','w') as filecsv:
    writer = csv.writer(filecsv)
    writer.writerows(data)

# Reading data
with open('books.csv','r') as filecsv:
    reader = csv.reader(filecsv)
    for i in reader:
        if i:
            print(i)