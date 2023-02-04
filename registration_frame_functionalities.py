import tkinter as tk
import database_functionalities
import re
import hashlib
import sqlite3
import popup_windows

registration_fields_data = {}


def get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu):
    registration_fields_data['username'] = username_input_field.get()
    registration_fields_data['password'] = password_input_field.get()
    registration_fields_data['confirm_password'] = confirm_password_input_field.get()
    registration_fields_data['first_name'] = first_name_input_field.get()
    registration_fields_data['last_name'] = last_name_input_field.get()
    registration_fields_data['role'] = menu.get()


def register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
             first_name_input_field, last_name_input_field, menu):
    get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu)
    
    if registration_fields_data['password'] != registration_fields_data['confirm_password']:
        popup_windows.passwords_error_popup(registration_frame, "Passwords are not matching!")
    elif bool(re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", registration_fields_data['password'])) == False:
        popup_windows.passwords_error_popup(registration_frame, "Passwords should have at least 6 symbols \n including capital letter and a number!" )
    else:
        try:
            database_functionalities.insert_into_user_table(registration_fields_data['username'], hashlib.sha256(registration_fields_data['password'].encode()).hexdigest(), 
                                                        registration_fields_data['first_name'], registration_fields_data['last_name'],
                                                        registration_fields_data['role'])
        except sqlite3.IntegrityError:
            popup_windows.passwords_error_popup(registration_frame, "This iser name is already taken!")

def create_registration_fields(registration_frame):
    tk.Label(registration_frame, text="username:").pack()
    username_input_field = tk.Entry(registration_frame)
    username_input_field.pack()

    tk.Label(registration_frame, text="password:").pack()
    password_input_field = tk.Entry(registration_frame, show='*')
    password_input_field.pack()

    tk.Label(registration_frame, text="confirm password:").pack()
    confirm_password_input_field = tk.Entry(registration_frame, show='*')
    confirm_password_input_field.pack()

    tk.Label(registration_frame, text="first name:").pack()
    first_name_input_field = tk.Entry(registration_frame)
    first_name_input_field.pack()

    tk.Label(registration_frame, text="last name:").pack()
    last_name_input_field = tk.Entry(registration_frame)
    last_name_input_field.pack()

    tk.Label(registration_frame, text="role:").pack()
    menu = tk.StringVar()
    menu.set("Select a role")
    role_dropdown = tk.OptionMenu(registration_frame, menu, "User with global rights", "User with local rights")
    role_dropdown.pack()

    register_button = tk.Button(registration_frame, text="Register", 
                      command=lambda:[register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
                      first_name_input_field, last_name_input_field, menu)])
    register_button.pack()