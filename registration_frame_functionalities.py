import tkinter as tk
import database_functionalities
import re
import hashlib
import sqlite3
import popup_windows

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500


class RegistrationFrame:
    def __init__(self, app):
        self.registration_frame = tk.Frame(app)
        self.registration_fields_data = {}

    def get_input_fields_data(self, username_input_field, password_input_field, confirm_password_input_field,
                              first_name_input_field, last_name_input_field, menu):
        self.registration_fields_data['username'] = username_input_field.get()
        self.registration_fields_data['password'] = password_input_field.get()
        self.registration_fields_data['confirm_password'] = confirm_password_input_field.get()
        self.registration_fields_data['first_name'] = first_name_input_field.get()
        self.registration_fields_data['last_name'] = last_name_input_field.get()
        self.registration_fields_data['role'] = menu.get()

    def get_global_user_input_fields_data(self, motivation_input_field, email_input_field):
        self.registration_fields_data['motivation'] = motivation_input_field.get()
        self.registration_fields_data['email'] = email_input_field.get()

    def is_password_correct(self, password):
        return bool(re.match(r".*\d.*", password) and re.match(r".*[A-Z].*", password) and len(password) >= 8)
    
    def is_user_global(self, role):
        return role == "User with global rights"

    def register(self, username_input_field, password_input_field, confirm_password_input_field,
                 first_name_input_field, last_name_input_field, menu, motivation_input_field, email_input_field,
                 login_frame):
        self.get_input_fields_data(username_input_field, password_input_field, confirm_password_input_field,
                                   first_name_input_field, last_name_input_field, menu)
        self.get_global_user_input_fields_data(motivation_input_field, email_input_field)

        if self.is_user_global(self.registration_fields_data['role']):
            if self.registration_fields_data['motivation'] == '' or self.registration_fields_data['email'] == '':
                popup_windows.popup_window(self.registration_frame, "Fill in all entry fields!", "Try again!")
                return None

        if self.registration_fields_data['username'] == '' or self.registration_fields_data['password'] == '' or \
                self.registration_fields_data['confirm_password'] == '' or self.registration_fields_data[
            'first_name'] == '' or self.registration_fields_data['last_name'] == '':
            popup_windows.popup_window(self.registration_frame, "Fill in all entry fields!", "Try again!")
        elif self.registration_fields_data['role'] == 'Select a role':
            popup_windows.popup_window(self.registration_frame, "Select a role!", "Try again!")
        elif self.registration_fields_data['password'] != self.registration_fields_data['confirm_password']:
            popup_windows.popup_window(self.registration_frame, "Passwords are not matching!", "Try again!")
        elif self.is_password_correct(self.registration_fields_data['password']) == False:
            popup_windows.popup_window(self.registration_frame, "Passwords should have at least 8 symbols \n including capital letter and a number!", "Try again!" )
        else:
            try:
                if self.is_user_global(self.registration_fields_data['role']):
                    database_functionalities.insert_into_requests_for_global_user_table(
                        self.registration_fields_data['username'],
                        hashlib.sha256(self.registration_fields_data['password'].encode()).hexdigest(),
                        self.registration_fields_data['first_name'], self.registration_fields_data['last_name'],
                        self.registration_fields_data['motivation'], self.registration_fields_data['email'])
                    database_functionalities.database.commit()
                    popup_windows.popup_window(self.registration_frame, "Successfully send request!", "Continue")
                    self.change_to_login_frame(login_frame)
                else:
                    database_functionalities.insert_into_user_table(self.registration_fields_data['username'],
                                                                    hashlib.sha256(self.registration_fields_data[
                                                                                       'password'].encode()).hexdigest(),
                                                                    self.registration_fields_data['first_name'],
                                                                    self.registration_fields_data['last_name'],
                                                                    self.registration_fields_data['role'])
                    database_functionalities.database.commit()
                    popup_windows.popup_window(self.registration_frame, "Successful registration!", "Continue")
                    self.change_to_login_frame(login_frame)
            except sqlite3.IntegrityError:
                popup_windows.popup_window(self.registration_frame, "This user name is already taken!", "Try again!")

    def change_to_login_frame(self, login_frame):
        login_frame.login_frame.pack(fill='both', expand=1)
        self.registration_frame.pack_forget()

    def create_registration_fields_for_global_user(self, menu, motivation_label, motivation_input_field, email_label,
                                                   email_input_field):
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

    def create_fields(self, login_frame):
        tk.Label(self.registration_frame, text="username:").pack()
        username_input_field = tk.Entry(self.registration_frame)
        username_input_field.pack()

        tk.Label(self.registration_frame, text="password:").pack()
        password_input_field = tk.Entry(self.registration_frame, show='*')
        password_input_field.pack()

        tk.Label(self.registration_frame, text="confirm password:").pack()
        confirm_password_input_field = tk.Entry(self.registration_frame, show='*')
        confirm_password_input_field.pack()

        tk.Label(self.registration_frame, text="first name:").pack()
        first_name_input_field = tk.Entry(self.registration_frame)
        first_name_input_field.pack()

        tk.Label(self.registration_frame, text="last name:").pack()
        last_name_input_field = tk.Entry(self.registration_frame)
        last_name_input_field.pack()

        motivation_label = tk.Label(self.registration_frame, text="Why you should be a global user:")
        motivation_input_field = tk.Entry(self.registration_frame)

        email_label = tk.Label(self.registration_frame,
                               text="Please leave your email so we can contact you for more information:")
        email_input_field = tk.Entry(self.registration_frame)

        tk.Label(self.registration_frame, text="role:").pack()
        menu = tk.StringVar()
        menu.set("Select a role")
        role_dropdown = tk.OptionMenu(self.registration_frame, menu, "User with global rights",
                                      "User with local rights",
                                      command=lambda _: self.create_registration_fields_for_global_user(menu,
                                                                                                        motivation_label,
                                                                                                        motivation_input_field,
                                                                                                        email_label,
                                                                                                        email_input_field))
        role_dropdown.pack()

        register_button = tk.Button(self.registration_frame, text="Register",
                                    command=lambda: [self.register(username_input_field, password_input_field,
                                                                   confirm_password_input_field,
                                                                   first_name_input_field, last_name_input_field, menu,
                                                                   motivation_input_field, email_input_field,
                                                                   login_frame)])
        register_button.place(x=WINDOW_WIDTH / 2 - register_button.winfo_width() / 2, y=375, anchor='center')

        go_back_button = tk.Button(self.registration_frame, text="Go back",
                                   command=lambda: [self.change_to_login_frame(login_frame)])
        go_back_button.place(x=WINDOW_WIDTH / 2 - register_button.winfo_width() / 2, y=415, anchor='center')