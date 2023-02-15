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
    database.execute(insert_query)
    database.commit()

def insert_into_global_user_additional_info_table(username, motivation, email):
    insert_query = """INSERT INTO global_user_additional_info_table
                          (username, motivation, email) 
                           VALUES 
                          (""" + "'" + username + "','" + motivation + "','" + email + "')"
    database.execute(insert_query)
    database.commit()

def insert_into_requests_for_global_user_table(username, password, first_name, last_name, motivation, email):
    insert_query = """INSERT INTO requests_for_global_user_table
                          (username, password, first_name, last_name, motivation, email) 
                           VALUES 
                          (""" + "'" + username + "','" + password + "','" + first_name + "','" + last_name + "','" + motivation + "','" + email + "')"
    database.execute(insert_query)
    database.commit()

def insert_into_melodys_table(name, path, keywords, creators_username, visibility):
    insert_query = """INSERT INTO melodys
                          (name, path, keywords, creators_username, visibility) 
                           VALUES 
                          (""" + "'" + name + "','" + path + "','" + keywords + "','" + creators_username + "','" + visibility + "')"
    database.execute(insert_query)
    database.commit()

def check_username_and_password(inputed_username, inputed_password):
    cursor = database.cursor()
    sql_select_query = """SELECT * FROM users WHERE username = ?"""
    cursor.execute(sql_select_query, (inputed_username,))
    records = cursor.fetchall()
    if records == []:
        return False
    for row in records:
        password_for_inputed_username = (row[1])
    return hashlib.sha256(inputed_password.encode()).hexdigest() == password_for_inputed_username

def get_role_from_username(username):
    cursor = database.cursor()
    sql_select_query = """SELECT * FROM users WHERE username = ?"""
    cursor.execute(sql_select_query, (username,))
    records = cursor.fetchall()
    if records == []:
        return False
    for row in records:
        role_for_user = (row[4])
    return role_for_user

def get_users_melodies(creators_username):
    cursor = database.cursor()
    sql_select_query = """SELECT name FROM melodys WHERE creators_username = ?"""
    cursor.execute(sql_select_query, (creators_username,))
    records = cursor.fetchall()
    if records == []:
        return False
    melodies_names = []
    for row in records:
        melodies_names.append(row[0])
    return melodies_names

def get_global_melodies():
    cursor = database.cursor()
    sql_select_query = """SELECT name, creators_username FROM melodys WHERE visibility = ?"""
    cursor.execute(sql_select_query, ("User with global rights",))
    records = cursor.fetchall()
    if records == []:
        return False
    melodies_names = []
    for row in records:
        melodies_names.append(row[0])
    return melodies_names

database = create_connection("virtual_piano_and_melody_library.db")

user_table = """ CREATE TABLE IF NOT EXISTS users (
                                    username text PRIMARY KEY,
                                    password text NOT NULL,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    role text NOT NULL
                                ); """

global_user_additional_info_table = """CREATE TABLE IF NOT EXISTS global_user_additional_info_table (
                                username text PRIMARY KEY,
                                motivation text NOT NULL, 
                                email text NOT NULL,
                                FOREIGN KEY (username) REFERENCES users (username)
                            );"""

requests_for_global_user_table = """CREATE TABLE IF NOT EXISTS requests_for_global_user_table (
                                username text PRIMARY KEY,
                                password text NOT NULL,
                                first_name text NOT NULL,
                                last_name text NOT NULL,
                                motivation text NOT NULL, 
                                email text NOT NULL
                            ); """

melodys_table = """CREATE TABLE IF NOT EXISTS melodys (
                                name text NOT NULL,
                                path text NOT NULL,
                                keywords text NOT NULL,
                                creators_username text NOT NULL,
                                visibility integer NOT NULL,
                                PRIMARY KEY (name, creators_username),
                                FOREIGN KEY (creators_username) REFERENCES users (username)
                            );"""

create_table(database, user_table)
create_table(database, global_user_additional_info_table)
create_table(database, requests_for_global_user_table)
create_table(database, melodys_table)

database.commit()