import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound
import record_melody

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

size_by_pixel = tk.PhotoImage(width=1, height=1)
key_buttons.create_key_buttons(app, WINDOW_HEIGHT, size_by_pixel)

record_melody_button = tk.Button(text='Record a melody', command=record_melody.record_melody)
record_melody_button.pack()

stop_record_melody_button = tk.Button(text='Stop recording a melody', command=lambda:[record_melody.stop_recording_melody(), record_melody.open_save_melody_popup_window(app)])
stop_record_melody_button.pack()

app.mainloop()