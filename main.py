import tkinter as tk
import registration_frame_functionalities
import login_frame_functionalities
import admin_frame_functionalities
import virtual_piano_frame_functionities
import key_buttons

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

class LoginFrame:
    def __init__(self, app):
        self.app = app
        self.login_frame = tk.Frame(self.app)
        self.login_frame.pack()

class RegistrationFrame:
    def __init__(self, app):
        self.registration_frame = tk.Frame(app)
        registration_frame_functionalities.create_registration_fields(self.registration_frame)

class VirtualPianoFrame:
    def __init__(self, app):
        self.virtual_piano_frame = tk.Frame(app)
        virtual_piano_frame_functionities.create_virtual_piano_fields(self.virtual_piano_frame)

class AdminFrame:
    def __init__(self, app):
        self.admin_frame = tk.Frame(app)
        admin_frame_functionalities.create_admin_fields(self.admin_frame)

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Music Library")
    app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

    login_frame = LoginFrame(app)
    registration_frame = RegistrationFrame(app)
    virtual_piano_frame = VirtualPianoFrame(app)
    admin_frame = AdminFrame(app)
    
    size_by_pixel = tk.PhotoImage(width=1, height=1)
    key_buttons.create_key_buttons(virtual_piano_frame.virtual_piano_frame, WINDOW_HEIGHT, size_by_pixel)

    login_frame_functionalities.create_login_fields(login_frame, registration_frame, virtual_piano_frame, admin_frame)

    app.mainloop()