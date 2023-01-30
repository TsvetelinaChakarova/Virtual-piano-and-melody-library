import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound

def record_melody():
    key_buttons.is_record_melody_pressed = True
    key_buttons.melody = [] 


def stop_recording_melody():
    key_buttons.is_record_melody_pressed = False
    combined_notes =  AudioSegment.empty()
    for note in key_buttons.melody:
        combined_notes += AudioSegment.from_wav('notes/' + note + '.wav')
    combined_notes.export('new_melody.wav', format="wav")
    playsound('new_melody.wav')


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

record_melody_button = tk.Button(text='Record a melody', command=record_melody)
record_melody_button.pack()

stop_record_melody_button = tk.Button(text='Stop recording a melody', command=stop_recording_melody)
stop_record_melody_button.pack()

app.mainloop()