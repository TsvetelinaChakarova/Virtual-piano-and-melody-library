import tkinter as tk

PASSWORD_POPUP_WINDOW_WIDTH = 300
PASSWORD_POPUP_WINDOW_HEIGHT = 100

def close_window(window):
    window.destroy()

def popup_window(registration_frame, error_message, button_text): 
    password_popup_window = tk.Toplevel(registration_frame)
    password_popup_window.geometry("{}x{}".format(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT))
    password_popup_window.minsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    password_popup_window.maxsize(PASSWORD_POPUP_WINDOW_WIDTH, PASSWORD_POPUP_WINDOW_HEIGHT)
    tk.Label(password_popup_window, text=error_message).pack()
    try_again_button = tk.Button(password_popup_window, text=button_text, command=lambda:[close_window(password_popup_window)])
    try_again_button.pack()