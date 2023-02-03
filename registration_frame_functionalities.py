import tkinter as tk
import database_functionalities

def register(username_input_field, password_input_field, confirm_password_input_field, 
             first_name_input_field, last_name_input_field, menu):
    username = username_input_field.get("1.0", "end-1c")
    password = password_input_field.get("1.0", "end-1c")
    confirm_password = confirm_password_input_field.get("1.0", "end-1c")
    first_name = first_name_input_field.get("1.0", "end-1c")
    last_name = last_name_input_field.get("1.0", "end-1c")
    role = menu.get()

    database_functionalities.insert_into_user_table(username, password, first_name, last_name, role)

def create_registration_fields(registration_frame):
    tk.Label(registration_frame, text="username:").pack()
    username_input_field = tk.Text(registration_frame, height=1, width=20)
    username_input_field.pack()

    tk.Label(registration_frame, text="password:").pack()
    password_input_field = tk.Text(registration_frame, height=1, width=20)
    password_input_field.pack()

    tk.Label(registration_frame, text="confirm password:").pack()
    confirm_password_input_field = tk.Text(registration_frame, height=1, width=20)
    confirm_password_input_field.pack()

    tk.Label(registration_frame, text="first name:").pack()
    first_name_input_field = tk.Text(registration_frame, height=1, width=20)
    first_name_input_field.pack()

    tk.Label(registration_frame, text="last name:").pack()
    last_name_input_field = tk.Text(registration_frame, height=1, width=20)
    last_name_input_field.pack()

    tk.Label(registration_frame, text="role:").pack()
    menu = tk.StringVar()
    menu.set("Select a role")
    role_dropdown = tk.OptionMenu(registration_frame, menu, "User with global rights", "User with local rights")
    role_dropdown.pack()

    register_button = tk.Button(registration_frame, text="Register", 
                      command=lambda:[register(username_input_field, password_input_field, confirm_password_input_field, 
                      first_name_input_field, last_name_input_field, menu)])
    register_button.pack()