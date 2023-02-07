import tkinter as tk
import database_functionalities
import re
import hashlib
import sqlite3
import popup_windows

registration_fields_data = {}

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

def get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu):
    registration_fields_data['username'] = username_input_field.get()
    registration_fields_data['password'] = password_input_field.get()
    registration_fields_data['confirm_password'] = confirm_password_input_field.get()
    registration_fields_data['first_name'] = first_name_input_field.get()
    registration_fields_data['last_name'] = last_name_input_field.get()
    registration_fields_data['role'] = menu.get()

def get_global_user_input_fields_data(motivation_input_field, email_input_field):
    registration_fields_data['motivation'] = motivation_input_field.get()
    registration_fields_data['email'] = email_input_field.get()

def register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
             first_name_input_field, last_name_input_field, menu, motivation_input_field, email_input_field):
    get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu)
    get_global_user_input_fields_data(motivation_input_field, email_input_field)
    
    if registration_fields_data['role'] == "User with global rights":
        if registration_fields_data['motivation'] == '' or  registration_fields_data['email'] == '':
            popup_windows.passwords_error_popup(registration_frame, "Fill in all entry fields!")

    if registration_fields_data['username'] == '' or  registration_fields_data['password'] == '' or registration_fields_data['confirm_password'] == '' or registration_fields_data['first_name'] == '' or registration_fields_data['last_name'] == '':
        popup_windows.passwords_error_popup(registration_frame, "Fill in all entry fields!")
    elif registration_fields_data['role'] == 'Select a role':
         popup_windows.passwords_error_popup(registration_frame, "Select a role!")
    elif registration_fields_data['password'] != registration_fields_data['confirm_password']:
        popup_windows.passwords_error_popup(registration_frame, "Passwords are not matching!")
    # elif bool(re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", registration_fields_data['password'])) == False:
    #     popup_windows.passwords_error_popup(registration_frame, "Passwords should have at least 6 symbols \n including capital letter and a number!" )
    else:
        try:
            database_functionalities.insert_into_user_table(registration_fields_data['username'], hashlib.sha256(registration_fields_data['password'].encode()).hexdigest(), 
                                                        registration_fields_data['first_name'], registration_fields_data['last_name'],
                                                        registration_fields_data['role'])
            if registration_fields_data['role'] == "User with global rights":
                database_functionalities.insert_into_global_user_additional_info_table(registration_fields_data['username'], registration_fields_data['motivation'], registration_fields_data['email'])
        except sqlite3.IntegrityError:
            popup_windows.passwords_error_popup(registration_frame, "This iser name is already taken!")
    


def create_registration_fields_for_global_user(menu, motivation_label, motivation_input_field, email_label, email_input_field):
    if menu.get() == "User with global rights":
        motivation_label.pack()
        motivation_input_field.pack()
        email_label.pack()
        email_input_field.pack()
    else:
        motivation_label.forget()
        motivation_input_field.pack_forget()
        email_input_field.pack_forget()
        email_label.pack_forget()


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

    motivation_label = tk.Label(registration_frame, text="Why you should be a global user:")
    motivation_input_field = tk.Entry(registration_frame)
    
    email_label = tk.Label(registration_frame, text="Please leave your email so we can contact you for more information:")
    email_input_field = tk.Entry(registration_frame)

    tk.Label(registration_frame, text="role:").pack()
    menu = tk.StringVar()
    menu.set("Select a role")
    role_dropdown = tk.OptionMenu(registration_frame, menu, "User with global rights", "User with local rights", command=lambda _ : create_registration_fields_for_global_user(menu, motivation_label, motivation_input_field, email_label, email_input_field))
    role_dropdown.pack()

    register_button = tk.Button(registration_frame, text="Register", 
                      command=lambda:[register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
                      first_name_input_field, last_name_input_field, menu, motivation_input_field, email_input_field)])
    register_button.place(x = WINDOW_WIDTH/2 - register_button.winfo_width()/2, y=375, anchor='center')
