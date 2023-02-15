import tkinter as tk
from tkinter import ttk
import database_functionalities


class AdminFrame:

    def __init__(self, app):
        self.admin_frame = tk.Frame(app)

    def add_global_user(self, treeview):
        treeview.bind('<<TreeviewSelect>>', self.add_global_user_help_function(treeview))

    def add_global_user_help_function(self, treeview):
        selected_item = treeview.selection()[0]
        cursor = database_functionalities.database.cursor()
        sql_select_query = "SELECT * FROM requests_for_global_user_table WHERE username = ?"
        cursor.execute(sql_select_query, (treeview.item(selected_item)['values'][0], ))
        records = cursor.fetchall()
        if records == []:
            return False
        for row in records:
            password_for_inputed_username = row[1]

        database_functionalities.insert_into_user_table(treeview.item(selected_item)['values'][0], 
                password_for_inputed_username,
                treeview.item(selected_item)['values'][1],
                treeview.item(selected_item)['values'][2],
                'User with global rights')
        database_functionalities.insert_into_global_user_additional_info_table(treeview.item(selected_item)['values'][0],
                treeview.item(selected_item)['values'][4],
                treeview.item(selected_item)['values'][3])
        sql_delete_query = "DELETE from requests_for_global_user_table where username = ?"
        cursor.execute(sql_delete_query, (treeview.item(selected_item)['values'][0], ))
        database_functionalities.database.commit()

    def reject_global_user(self, treeview):
        treeview.bind('<<TreeviewSelect>>', self.reject_global_user_help_function(treeview))

    def reject_global_user_help_function(self, treeview):
        selected_item = treeview.selection()[0]
        cursor = database_functionalities.database.cursor()
        sql_select_query = "SELECT * FROM requests_for_global_user_table WHERE username = ?"
        cursor.execute(sql_select_query,
                       (treeview.item(selected_item)['values'][0], ))

        sql_delete_query = "DELETE from requests_for_global_user_table where username = ?"
        cursor.execute(sql_delete_query,
                       (treeview.item(selected_item)['values'][0], ))
        database_functionalities.database.commit()

    def display_requests_for_global_user_table(self, database):
        treeview = ttk.Treeview(self.admin_frame, column=('username',
                                'first_name', 'last_name', 'email',
                                'motivation'), show='headings')
        treeview['columns'] = ('username', 'first_name', 'last_name',
                               'email', 'motivation')
        treeview.column('username', anchor=tk.CENTER)
        treeview.heading('username', text='Username')
        treeview.column('first_name', anchor=tk.CENTER)
        treeview.heading('first_name', text='First name')
        treeview.column('last_name', anchor=tk.CENTER)
        treeview.heading('last_name', text='Last name')
        treeview.column('email', anchor=tk.CENTER)
        treeview.heading('email', text='Email')
        treeview.column('motivation', anchor=tk.CENTER)
        treeview.heading('motivation', text='Motivation')
        treeview.pack()

        cursor = database.cursor()
        cursor.execute("SELECT username, first_name, last_name, email, motivation FROM requests_for_global_user_table")
        rows = cursor.fetchall()
        for row in rows:
            treeview.insert('', tk.END, values=row)
        return treeview

    def refresh_admin_frame(self, treeview, database):
        treeview.pack_forget()
        self.display_requests_for_global_user_table(database)

    def change_to_login_frame(self, login_frame):
        login_frame.login_frame.pack(fill='both', expand=1)
        self.admin_frame.pack_forget()

    def create_fields(self, login_frame):
        add_global_user_button = tk.Button(self.admin_frame, text='Add user', command=lambda : \
                [self.add_global_user(treeview),
                self.refresh_admin_frame(treeview,
                database_functionalities.database)])
        add_global_user_button.pack()

        reject_global_user_button = tk.Button(self.admin_frame, text='Reject user', command=lambda : \
                [self.reject_global_user(treeview),
                self.refresh_admin_frame(treeview,
                database_functionalities.database)])
        reject_global_user_button.pack()

        logout_button = tk.Button(self.admin_frame, text='Logout', command=lambda : \
                                  [self.change_to_login_frame(login_frame)])
        logout_button.pack()

        treeview = self.display_requests_for_global_user_table(database_functionalities.database)