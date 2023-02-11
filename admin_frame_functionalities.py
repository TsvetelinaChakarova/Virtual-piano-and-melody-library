import tkinter as tk
from tkinter import ttk
import database_functionalities

class AdminFrame:
    def __init__(self, app):
        self.admin_frame = tk.Frame(app)
        self.create_admin_fields(self.admin_frame)

    def add_global_user(self, treeview):
        treeview.bind("<<TreeviewSelect>>", self.get_selected_items_from_treeview(treeview))

    def get_selected_items_from_treeview(self, treeview):
        selected_item = treeview.selection()[0]
        cursor = database_functionalities.database.cursor()
        sql_select_query = """SELECT * FROM requests_for_global_user_table WHERE username = ?"""
        cursor.execute(sql_select_query, (treeview.item(selected_item)['values'][0],))
        records = cursor.fetchall()
        if records == []:
            return False
        for row in records:
            password_for_inputed_username = (row[1])

        database_functionalities.insert_into_user_table(treeview.item(selected_item)['values'][0], password_for_inputed_username, 
                                                            treeview.item(selected_item)['values'][1], treeview.item(selected_item)['values'][2],
                                                            "User with global rights")
        database_functionalities.insert_into_global_user_additional_info_table(treeview.item(selected_item)['values'][0], treeview.item(selected_item)['values'][4], treeview.item(selected_item)['values'][3])
        sql_delete_query = """DELETE from requests_for_global_user_table where username = ?"""
        cursor.execute(sql_delete_query, (treeview.item(selected_item)['values'][0],))
        database_functionalities.database.commit()

    def display_requests_for_global_user_table(self, frame, database): 
        treeview = ttk.Treeview(frame, column=("username", "first_name", "last_name", "email", "motivation"), show='headings')
        treeview["columns"] = ("username", "first_name", "last_name", "email", "motivation")
        treeview.column("username", anchor=tk.CENTER)
        treeview.heading("username", text="Username")
        treeview.column("first_name", anchor=tk.CENTER)
        treeview.heading("first_name", text="First name")
        treeview.column("last_name", anchor=tk.CENTER)
        treeview.heading("last_name", text="Last name")
        treeview.column("email", anchor=tk.CENTER)
        treeview.heading("email", text="Email")
        treeview.column("motivation", anchor=tk.CENTER)
        treeview.heading("motivation", text="Motivation")
        treeview.pack()

        cursor = database.cursor()
        cursor.execute("""SELECT username, first_name, last_name, email, motivation FROM requests_for_global_user_table""")
        rows = cursor.fetchall()    
        for row in rows:
            treeview.insert("", tk.END, values=row)  
        return treeview

    def create_admin_fields(self, admin_frame):
        treeview = self.display_requests_for_global_user_table(admin_frame, database_functionalities.database)
        add_global_user_button = tk.Button(admin_frame, text='Add user', command=lambda:[self.add_global_user(treeview)])
        add_global_user_button.pack()

        reject_global_user_button = tk.Button(admin_frame, text='Reject user', command=lambda:[self.add_global_user(treeview)])
        reject_global_user_button.pack()
