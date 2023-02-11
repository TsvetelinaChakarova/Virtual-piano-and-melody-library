import tkinter as tk
import registration_frame_functionalities
import login_frame_functionalities
import admin_frame_functionalities
import virtual_piano_frame_functionities
import key_buttons

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Music Library")
    app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

    login_frame = login_frame_functionalities.LoginFrame(app)
    registration_frame = registration_frame_functionalities.RegistrationFrame(app)
    virtual_piano_frame = virtual_piano_frame_functionities.VirtualPianoFrame(app)
    admin_frame = admin_frame_functionalities.AdminFrame(app)

    size_by_pixel = tk.PhotoImage(width=1, height=1)
    key_buttons.create_key_buttons(virtual_piano_frame.virtual_piano_frame, WINDOW_HEIGHT, size_by_pixel)

    login_frame.create_login_fields(login_frame, registration_frame, virtual_piano_frame, admin_frame)

    app.mainloop()