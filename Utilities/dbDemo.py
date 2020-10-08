import mysql.connector

#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='ritesh12')
from Utilities.Configuration import *

conn = getSQLConnection()

print(conn.is_connected())

cursor = conn.cursor()

cursor.execute('select * from CustomerInfo;')

# row = cursor.fetchone()

# print(row)

# print(row[2])

rows = cursor.fetchall()

print(rows)

sum = 0

for row in rows:

    print(row[2])

    sum = sum + row[2]

print('Total sum is', sum)

query = "update customerinfo set Location = %s where CourseName = %s"

data = ("Africa", "selenium")

cursor.execute(query, data)

conn.commit()

print(rows)

conn.close()
