import tkinter as tk
import registration_frame_functionalities
import login_frame_functionalities
import virtual_piano_frame_functionities
import key_buttons

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

# create frames 
login_frame = tk.Frame(app)
registration_frame = tk.Frame(app)
virtual_piano_frame = tk.Frame(app)

# for login_frame
login_frame.pack()
login_frame_functionalities.create_login_fields(login_frame, registration_frame, virtual_piano_frame)

# for registration frame
registration_frame_functionalities.create_registration_fields(registration_frame)

# for virtual_piano_frame
size_by_pixel = tk.PhotoImage(width=1, height=1)
key_buttons.create_key_buttons(virtual_piano_frame, WINDOW_HEIGHT, size_by_pixel)

virtual_piano_frame_functionities.create_virtual_piano_fields(virtual_piano_frame)

app.mainloop()