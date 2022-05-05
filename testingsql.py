import sqlite3
import os

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+'testing2.db')
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS addresses")
cur.execute("DROP TABLE IF EXISTS phones")

cur.execute("CREATE TABLE 'addresses' ('Name' TEXT, 'Address' TEXT)")
cur.execute("CREATE TABLE 'phones' ('Name' TEXT, 'Number' TEXT)")

cur.execute("INSERT INTO addresses (Name, Address) VALUES ('John', '123 Somewhere St')")
cur.execute("INSERT INTO addresses (Name, Address) VALUES ('Mary', '234 Easy St')")
cur.execute("INSERT INTO addresses (Name, Address) VALUES ('Alice', '345 Main')")

cur.execute("INSERT INTO phones (Name, Number) VALUES ('John', 'xxx')")
cur.execute("INSERT INTO phones (Name, Number) VALUES ('James', 'yyy')")
cur.execute("INSERT INTO phones (Name, Number) VALUES ('Alice', 'zzz')")

cur.execute("SELECT addresses.Name, Address, phones.Number FROM addresses LEFT JOIN phones ON addresses.Name = phones.Name")

for row in cur.fetchall():
    print(row)

conn.commit()
cur.close()
# cur.execute('CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE)')

# cur.execute('INSERT INTO Users (id, name, email) VALUES (?, ?, ?)', (2, 'Erica', 'ewpoon@umch.edu'))

# cur.execute('INSERT INTO Users (id, name, email) VALUES (?, ?, ?)', (1, 'Matthew', 'mkpoon@umich.edu'))

# conn.commit()

# print("Names: ")


# cur.execute("SELECT * FROM Users")
# print(cur.fetchone())

# for row in cur.fetchall():
#     print(row)
#     print("id: " + str(row[0]))
#     print("Name: " + row[1])
#     print("email: " + row[2])

# # for row in cur.execute('SELECT * FROM Users'):
# #     print("It'll print this: ")
# #     print(cur.fetchone())
# #     # print(row)


# # cur.close()
# cur.close()

