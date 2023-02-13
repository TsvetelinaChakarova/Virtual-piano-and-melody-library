import tkinter as tk
import key_buttons
from pydub import AudioSegment
from playsound import playsound
import database_functionalities
import login_frame_functionalities
import os

SAVE_MELODY_POPUP_WINDOW_WIDTH = 600
SAVE_MELODY_POPUP_WINDOW_HEIGHT = 300
MELODY_NAME_INPUT_FIELD_WIDTH = 30
MELODY_NAME_INPUT_FIELD_HEIGHT = 1

#save melody under a name inputed by the user
def save_melody(melody_name_input_field, melody_keywords_input_field):
    melody_name = melody_name_input_field.get("1.0", "end-1c")
    melody_keywords = melody_keywords_input_field.get("1.0", "end-1c")
    combined_notes =  AudioSegment.empty()
    for note in key_buttons.melody:
        combined_notes += AudioSegment.from_wav('notes/' + note + '.wav')
    path = "Melodys/" + login_frame_functionalities.current_user_username
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    combined_notes.export(path + '/' + melody_name + '.wav', format="wav")
    database_functionalities.insert_into_melodys_table(melody_name, path + '/' + melody_name + '.wav', melody_keywords, login_frame_functionalities.current_user_username, login_frame_functionalities.current_user_role)

# create and open a popup window with input field for melody's name
def save_melody_popup_window(app):
    save_melody_popup_window = tk.Toplevel(app)
    save_melody_popup_window.geometry("{}x{}".format(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT))
    save_melody_popup_window.minsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.maxsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.title("Save melody")
    
    melody_name_input_field = tk.Text(save_melody_popup_window, height=MELODY_NAME_INPUT_FIELD_HEIGHT, width=MELODY_NAME_INPUT_FIELD_WIDTH)
    melody_name_input_field.pack()   

    melody_keywords_input_field = tk.Text(save_melody_popup_window, height=MELODY_NAME_INPUT_FIELD_HEIGHT, width=MELODY_NAME_INPUT_FIELD_WIDTH)
    melody_keywords_input_field.pack() 
    
    save_melody_button = tk.Button(save_melody_popup_window, text="Save melody", command=lambda:[save_melody(melody_name_input_field, melody_keywords_input_field)])
    save_melody_button.pack()

def record_melody():
    key_buttons.is_record_melody_pressed = True
    key_buttons.melody = [] 

def stop_recording_melody(app):
    key_buttons.is_record_melody_pressed = False
    save_melody_popup_window(app)
