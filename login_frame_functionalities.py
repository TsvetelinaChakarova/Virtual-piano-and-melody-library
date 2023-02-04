import tkinter as tk
import database_functionalities

login_fields_data = {}

PASSWORD_POPUP_WINDOW_WIDTH = 300
PASSWORD_POPUP_WINDOW_HEIGHT = 100

def close_window(window):
    window.destroy()

def wrong_passwords_popup(login_frame, error_message): 
    password_popup_window = tk.Toplevel(login_frame)
    password_popup_window.geometry("{}x{}".format(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT))
    password_popup_window.minsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    password_popup_window.maxsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    tk.Label(password_popup_window, text=error_message).pack()
    try_again_button = tk.Button(password_popup_window, text="Try again!", command=lambda:[close_window(password_popup_window)])
    try_again_button.pack()

def get_input_fields_data(username_input_field, password_input_field):
    login_fields_data['username'] = username_input_field.get()
    login_fields_data['password'] = password_input_field.get()

def change_to_virtual_piano_frame(login_frame, virtual_piano_frame, username_input_field, password_input_field):
    get_input_fields_data(username_input_field, password_input_field)
    if database_functionalities.check_username_and_password(login_fields_data['username'], login_fields_data['password']):
        virtual_piano_frame.pack(fill='both', expand=1)
        login_frame.pack_forget()
    else:
        wrong_passwords_popup(login_frame, "Invalid username or password!")

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