import sqlite3

db = sqlite3.connect('users.db')

cursor = db.cursor()

# Execute the DROP Table SQL statement

dropTableStatement = "DROP TABLE IF EXISTS scores"
cursor.executescript(dropTableStatement)

dropTableStatement = "DROP TABLE IF EXISTS users"
cursor.executescript(dropTableStatement)

db.execute('''CREATE TABLE users ( 
    uid INTEGER PRIMARY KEY, 
    firstname TEXT, 
    lastname TEXT, 
    email TEXT, 
    pwdhash TEXT)''')

db.execute('''CREATE TABLE scores ( 
    sid INTEGER PRIMARY KEY,
    uid INTEGER,
    score INTEGER,
    FOREIGN KEY(uid) REFERENCES users(uid))''')

db.commit()
db.close()
