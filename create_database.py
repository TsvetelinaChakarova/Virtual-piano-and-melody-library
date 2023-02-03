import sqlite3

#creating a database 
database = sqlite3.connect("virtual_piano_and_melody_library.db")
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user(username, password, first_name, last_name, role)")
cursor.execute("CREATE TABLE IF NOT EXISTS melody(name, path, creators_username, visibility)")

database.commit()

database.close() 