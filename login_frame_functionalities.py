import tkinter as tk
import database_functionalities
import popup_windows

login_fields_data = {}

def close_window(window):
    window.destroy()

def get_input_fields_data(username_input_field, password_input_field):
    login_fields_data['username'] = username_input_field.get()
    login_fields_data['password'] = password_input_field.get()

def change_to_virtual_piano_frame(login_frame, virtual_piano_frame, username_input_field, password_input_field):
    get_input_fields_data(username_input_field, password_input_field)
    if database_functionalities.check_username_and_password(login_fields_data['username'], login_fields_data['password']):
        virtual_piano_frame.pack(fill='both', expand=1)
        login_frame.pack_forget()
    else:
        popup_windows.passwords_error_popup(login_frame, "Invalid username or password!")

def change_to_registration_frame(login_frame, registration_frame):
    registration_frame.pack(fill='both', expand=1)
    login_frame.pack_forget()

def create_login_fields(login_frame, registration_frame, virtual_piano_frame):
    tk.Label(login_frame, text="username:").pack()
    username_input_field = tk.Entry(login_frame)
    username_input_field.pack()

    tk.Label(login_frame, text="password:").pack()
    password_input_field = tk.Entry(login_frame, show='*')
    password_input_field.pack()

    create_account_button = tk.Button(login_frame, text='Create account', command=lambda:[change_to_registration_frame(login_frame, registration_frame)])
    create_account_button.pack()

    login_button = tk.Button(login_frame, text='Login', command=lambda:[change_to_virtual_piano_frame(login_frame, virtual_piano_frame, username_input_field, password_input_field)])
    login_button.pack()