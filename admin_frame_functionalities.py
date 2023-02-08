import tkinter as tk
from tkinter import ttk
import database_functionalities

def add_global_user(treeview):
    treeview.bind("<<TreeviewSelect>>", get_selected_items_from_treeview(treeview))

def get_selected_items_from_treeview(treeview):
    selected_item = treeview.selection()[0]
    print(treeview.item(selected_item)['values'][0])
    print(treeview.item(selected_item)['values'][1])
    print(treeview.item(selected_item)['values'][2])
    print(treeview.item(selected_item)['values'][3])
    print(treeview.item(selected_item)['values'][4])


def display_requests_for_global_user_table(frame, database): 
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

def create_admin_fields(admin_frame):
    treeview = display_requests_for_global_user_table(admin_frame, database_functionalities.database)
    button1 = tk.Button(admin_frame, text='Add user', command=lambda:[add_global_user(treeview)])
    button1.pack()