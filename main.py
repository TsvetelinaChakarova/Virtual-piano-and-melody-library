import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound
import record_melody

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

def change_to_virtual_piano_page():
    virtual_piano_page.pack(fill='both', expand=1)
    login_frame.pack_forget()

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

login_frame = tk.Frame(app)
login_frame.pack()
virtual_piano_page = tk.Frame(app)

login_button = tk.Button(login_frame, text='Login', command=lambda:[change_to_virtual_piano_page()])
login_button.pack()

size_by_pixel = tk.PhotoImage(width=1, height=1)
key_buttons.create_key_buttons(virtual_piano_page, WINDOW_HEIGHT, size_by_pixel)

record_melody_button = tk.Button(virtual_piano_page, text='Record a melody', command=lambda:[record_melody.record_melody()])
record_melody_button.pack()

stop_record_melody_button = tk.Button(virtual_piano_page, text='Stop recording a melody',
                                      command=lambda:[record_melody.stop_recording_melody(virtual_piano_page)])
stop_record_melody_button.pack()

app.mainloop()