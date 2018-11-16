import sqlite3

db = sqlite3.connect('users.db')
db.execute('''CREATE TABLE users 
( uid INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT, pwdhash TEXT)''')

db.commit()
db.close()
