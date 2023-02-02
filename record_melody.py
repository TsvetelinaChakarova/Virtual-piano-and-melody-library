import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound

SAVE_MELODY_POPUP_WINDOW_WIDTH = 600
SAVE_MELODY_POPUP_WINDOW_HEIGHT = 300

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


def open_save_melody_popup_window(app):
    save_melody_popup_window = tk.Toplevel(app)
    save_melody_popup_window.geometry("{}x{}".format(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT))
    save_melody_popup_window.minsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.maxsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.title("Save melody")