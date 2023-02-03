import sqlite3

def create_connection(database_file):
    return sqlite3.connect(database_file)

def create_table(database, table):
    cursor = database.cursor()
    cursor.execute(table)

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
database.close()