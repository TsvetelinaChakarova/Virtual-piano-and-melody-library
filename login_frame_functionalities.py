import tkinter as tk

def change_to_virtual_piano_frame(login_frame, virtual_piano_frame):
    virtual_piano_frame.pack(fill='both', expand=1)
    login_frame.pack_forget()

def change_to_registration_frame(login_frame, registration_frame):
    registration_frame.pack(fill='both', expand=1)
    login_frame.pack_forget()

def create_login_fields(login_frame, registration_frame, virtual_piano_frame):
    create_account_button = tk.Button(login_frame, text='Create account', command=lambda:[change_to_registration_frame(login_frame, registration_frame)])
    create_account_button.pack()

    login_button = tk.Button(login_frame, text='Login', command=lambda:[change_to_virtual_piano_frame(login_frame, virtual_piano_frame)])
    login_button.pack()