import tkinter as tk
from pydub import AudioSegment
import database_functionalities
import login_frame_functionalities
import os
import popup_windows

SAVE_MELODY_POPUP_WINDOW_WIDTH = 600
SAVE_MELODY_POPUP_WINDOW_HEIGHT = 300
MELODY_NAME_INPUT_FIELD_WIDTH = 30
MELODY_NAME_INPUT_FIELD_HEIGHT = 1

#save melody under a name inputed by the user
def save_melody(save_melody_popup_window, melody_input_field, melody_name_input_field, melody_keywords_input_field, menu):
    try: 
        melody = melody_input_field.get("1.0", "end-1c")
        melody_name = melody_name_input_field.get("1.0", "end-1c")
        melody_keywords = melody_keywords_input_field.get("1.0", "end-1c")
        
        if melody_name == "" or melody_keywords == "": 
            popup_windows.popup_window(save_melody_popup_window, "Fill in all entry fields!", "Try again!")
            return None
        
        if menu.get() == "Select":
            popup_windows.popup_window(save_melody_popup_window, "Select a role!", "Try again!")
            return None

        combined_notes =  AudioSegment.empty()
        for note in melody.split(" "):
            combined_notes += AudioSegment.from_wav('notes/' + note + '.wav')
        path = "Melodys/" + login_frame_functionalities.current_user_username
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        combined_notes.export(path + '/' + melody_name + '.wav', format="wav")
        if login_frame_functionalities.current_user_role == "User with global rights" and menu.get() == "Save as local melody":
            database_functionalities.insert_into_melodys_table(melody_name, path + '/' + melody_name + '.wav', melody_keywords, login_frame_functionalities.current_user_username, "User with local rights")
        else:
            database_functionalities.insert_into_melodys_table(melody_name, path + '/' + melody_name + '.wav', melody_keywords, login_frame_functionalities.current_user_username, login_frame_functionalities.current_user_role)
        database_functionalities.database.commit()
        save_melody_popup_window.destroy()
    except FileNotFoundError:
        popup_windows.popup_window(save_melody_popup_window, "The inputed notes are not correct!", "Try again!")

# create and open a popup window with input field for melody's name
def save_melody_popup_window(app):
    save_melody_popup_window = tk.Toplevel(app)
    save_melody_popup_window.geometry("{}x{}".format(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT))
    save_melody_popup_window.minsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.maxsize(SAVE_MELODY_POPUP_WINDOW_WIDTH, SAVE_MELODY_POPUP_WINDOW_HEIGHT)
    save_melody_popup_window.title("Save melody")
    
    rules = """Please follow the listed rules:
    1. Input notes in the ABC notation. Only A, B, C, D, E, F, G are permitted.
    2. Next input 'sharp' as '#'. Sharp is not required.  
    4. Next input a number for the octave.
    5. Separate notes with one space
    6. Input notes only shown at the piano: from C3 to E5.
    Example: F#4 E3 A#4"""
    rules_button = tk.Button(save_melody_popup_window, text='Rules', command=lambda:[popup_windows.popup_window(save_melody_popup_window, rules, "Continue")])
    rules_button.pack()
    
    melody_label = tk.Label(save_melody_popup_window, text="Melody:")
    melody_label.pack()

    melody_input_field = tk.Text(save_melody_popup_window, height=MELODY_NAME_INPUT_FIELD_HEIGHT, width=MELODY_NAME_INPUT_FIELD_WIDTH)
    melody_input_field.pack()   
    
    melody_name_label = tk.Label(save_melody_popup_window, text="Melody name:")
    melody_name_label.pack()

    melody_name_input_field = tk.Text(save_melody_popup_window, height=MELODY_NAME_INPUT_FIELD_HEIGHT, width=MELODY_NAME_INPUT_FIELD_WIDTH)
    melody_name_input_field.pack()   
    
    melody_keywords_label = tk.Label(save_melody_popup_window, text="Melody keywords:")
    melody_keywords_label.pack()

    melody_keywords_input_field = tk.Text(save_melody_popup_window, height=MELODY_NAME_INPUT_FIELD_HEIGHT, width=MELODY_NAME_INPUT_FIELD_WIDTH)
    melody_keywords_input_field.pack() 
    
    tk.Label(save_melody_popup_window, text="Save melody as:").pack()
    menu = tk.StringVar()
    menu.set("Select")
    if login_frame_functionalities.current_user_role == "User with global rights":
        save_as_dropdown = tk.OptionMenu(save_melody_popup_window, menu, "Save as global melody", "Save as local melody")
    else:
        save_as_dropdown = tk.OptionMenu(save_melody_popup_window, menu, "Save as local melody")
    save_as_dropdown.pack()
    
    save_melody_button = tk.Button(save_melody_popup_window, text="Save melody", command=lambda:[save_melody(save_melody_popup_window, melody_input_field, melody_name_input_field, melody_keywords_input_field, menu)])
    save_melody_button.pack()