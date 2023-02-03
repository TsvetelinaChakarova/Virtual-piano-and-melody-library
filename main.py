import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound
import record_melody    
import registration_frame_functionalities

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

def change_to_virtual_piano_frame():
    virtual_piano_frame.pack(fill='both', expand=1)
    login_frame.pack_forget()

def change_to_registration_frame():
    registration_frame.pack(fill='both', expand=1)
    login_frame.pack_forget()

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
create_account_button = tk.Button(login_frame, text='Create account', command=lambda:[change_to_registration_frame()])
create_account_button.pack()

login_button = tk.Button(login_frame, text='Login', command=lambda:[change_to_virtual_piano_frame()])
login_button.pack()

# for registration frame
registration_frame_functionalities.create_registration_fields(registration_frame)

# for virtual_piano_frame
size_by_pixel = tk.PhotoImage(width=1, height=1)
key_buttons.create_key_buttons(virtual_piano_frame, WINDOW_HEIGHT, size_by_pixel)

# record melody 
record_melody_button = tk.Button(virtual_piano_frame, text='Record a melody', command=lambda:[record_melody.record_melody()])
record_melody_button.pack()

stop_record_melody_button = tk.Button(virtual_piano_frame, text='Stop recording a melody',
                                      command=lambda:[record_melody.stop_recording_melody(virtual_piano_frame)])
stop_record_melody_button.pack()

app.mainloop()