import sqlite3
import hashlib

def create_connection(database_file):
    return sqlite3.connect(database_file)

def create_table(database, table):
    cursor = database.cursor()
    cursor.execute(table)

def insert_into_user_table(username, password, first_name, last_name, role):
    insert_query = """INSERT INTO users
                          (username, password, first_name, last_name, role) 
                           VALUES 
                          (""" + "'" + username + "','" + password + "','" + first_name + "','" + last_name + "','" + role + "')"
    # print(insert_query)
    database.execute(insert_query)
    database.commit()

def check_username_and_password(inputed_username, inputed_password):
    cursor = database.cursor()
    sql_select_query = """select * from users where username = ?"""
    cursor.execute(sql_select_query, (inputed_username,))
    records = cursor.fetchall()
    if records == []:
        return False
    for row in records:
        password_for_inputed_username = (row[1])
    return hashlib.sha256(inputed_password.encode()).hexdigest() == password_for_inputed_username

database = create_connection("virtual_piano_and_melody_library.db")

user_table = """ CREATE TABLE IF NOT EXISTS users (
                                    username text PRIMARY KEY,
                                    password text NOT NULL,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    role text NOT NULL
                                ); """

melodys_table = """CREATE TABLE IF NOT EXISTS melodys (
                                name text NOT NULL,
                                path text NOT NULL,
                                creators_username text NOT NULL,
                                visibility integer NOT NULL,
                                PRIMARY KEY (name, creators_username)
                                FOREIGN KEY (creators_username) REFERENCES users (username)
                            );"""

create_table(database, user_table)
create_table(database, melodys_table)

database.commit()