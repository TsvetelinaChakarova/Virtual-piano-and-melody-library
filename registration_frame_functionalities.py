import tkinter as tk
import database_functionalities

PASSWORD_POPUP_WINDOW_WIDTH = 300
PASSWORD_POPUP_WINDOW_HEIGHT = 100

registration_fields_data = {}

def close_window(window):
    window.destroy()


def get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu):
    registration_fields_data['username'] = username_input_field.get("1.0", "end-1c")
    registration_fields_data['password'] = password_input_field.get("1.0", "end-1c")
    registration_fields_data['confirm_password'] = confirm_password_input_field.get("1.0", "end-1c")
    registration_fields_data['first_name'] = first_name_input_field.get("1.0", "end-1c")
    registration_fields_data['last_name'] = last_name_input_field.get("1.0", "end-1c")
    registration_fields_data['role'] = menu.get()


def passwords_not_matching_popup(registration_frame): 
    password_popup_window = tk.Toplevel(registration_frame)
    password_popup_window.geometry("{}x{}".format(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT))
    password_popup_window.minsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    password_popup_window.maxsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    tk.Label(password_popup_window, text="Passwords are not mastching!").pack()
    try_again_button = tk.Button(password_popup_window, text="Try again!", command=lambda:[close_window(password_popup_window)])
    try_again_button.pack()


def register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
             first_name_input_field, last_name_input_field, menu):
    get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field, 
                          first_name_input_field, last_name_input_field, menu)
    
    if registration_fields_data['password'] != registration_fields_data['confirm_password']:
        passwords_not_matching_popup(registration_frame)
    else:
        database_functionalities.insert_into_user_table(registration_fields_data['username'], registration_fields_data['password'], 
                                                        registration_fields_data['first_name'], registration_fields_data['last_name'],
                                                        registration_fields_data['role'])


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
                      command=lambda:[register(registration_frame, username_input_field, password_input_field, confirm_password_input_field, 
                      first_name_input_field, last_name_input_field, menu)])
    register_button.pack()