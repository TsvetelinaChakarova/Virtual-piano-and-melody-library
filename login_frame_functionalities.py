import tkinter as tk
import database_functionalities
import popup_windows

current_user_username = ""
current_user_role = ""


class LoginFrame:
    def __init__(self, app):
        self.app = app
        self.login_frame = tk.Frame(self.app)
        self.login_frame.pack()
        self.login_fields_data = {}

    def get_input_fields_data(self, username_input_field, password_input_field):
        self.login_fields_data['username'] = username_input_field.get()
        self.login_fields_data['password'] = password_input_field.get()
        self.login_fields_data['password'] = password_input_field.get()

    def update_current_user(self):
        global current_user_username, current_user_role
        current_user_username = self.login_fields_data['username']
        current_user_role = database_functionalities.get_role_from_username(self.login_fields_data['username'])

    def change_frame_after_login(self, virtual_piano_frame, admin_frame, username_input_field, password_input_field):
        self.get_input_fields_data(username_input_field, password_input_field)
        if self.login_fields_data['username'] == '' or self.login_fields_data['password'] == '':
            popup_windows.popup_window(self.login_frame, "Fill in all entry fields!", "Try again!")
        elif self.login_fields_data['username'] == 'Admin' and database_functionalities.check_username_and_password(
                self.login_fields_data['username'], self.login_fields_data['password']):
            admin_frame.treeview.destroy()
            admin_frame.treeview = admin_frame.display_requests_for_global_user_table()
            admin_frame.admin_frame.pack(fill='both', expand=1)
            self.login_frame.pack_forget()
            username_input_field.delete(0, "end")
            password_input_field.delete(0, "end")
        elif database_functionalities.check_username_and_password(self.login_fields_data['username'],
                                                                  self.login_fields_data['password']):
            virtual_piano_frame.virtual_piano_frame.pack(fill='both', expand=1)
            self.login_frame.pack_forget()
            username_input_field.delete(0, "end")
            password_input_field.delete(0, "end")
        else:
            popup_windows.popup_window(self.login_frame, "Invalid username or password!", "Try again!")

    def change_to_registration_frame(self, registration_frame, username_input_field, password_input_field):
        registration_frame.registration_frame.pack(fill='both', expand=1)
        self.login_frame.pack_forget()
        username_input_field.delete(0, "end")
        password_input_field.delete(0, "end")

    def create_fields(self, registration_frame, virtual_piano_frame, admin_frame):
        tk.Label(self.login_frame, text="username:").pack()
        username_input_field = tk.Entry(self.login_frame)
        username_input_field.pack()

        tk.Label(self.login_frame, text="password:").pack()
        password_input_field = tk.Entry(self.login_frame, show='*')
        password_input_field.pack()

        login_button = tk.Button(self.login_frame, text='Login', command=lambda: [
            self.change_frame_after_login(virtual_piano_frame, admin_frame, username_input_field, password_input_field),
            self.update_current_user()])
        login_button.pack()

        create_account_button = tk.Button(self.login_frame, text='Create account',
                                          command=lambda: [self.change_to_registration_frame(registration_frame, username_input_field, password_input_field)])
        create_account_button.pack()
