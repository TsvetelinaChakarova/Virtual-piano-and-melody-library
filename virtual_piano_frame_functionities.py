import tkinter as tk
import record_melody_by_pressing_keys
import record_melody_by_text
import database_functionalities

WINDOW_HEIGHT = 500


class VirtualPianoFrame:
    def __init__(self, app):
        self.virtual_piano_frame = tk.Frame(app)

    def change_to_login_frame(self, login_frame):
        login_frame.login_frame.pack(fill='both', expand=1)
        self.virtual_piano_frame.pack_forget()

    def change_to_view_melodies_frame(self, view_melodies_frame):
        view_melodies_frame.view_melodies_frame.pack(fill='both', expand=1)
        view_melodies_frame.display_users_melodies(database_functionalities.database)
        self.virtual_piano_frame.pack_forget()

    def create_fields(self, login_frame, view_melodies_frame, view_global_melodies_frame):
        record_melody_by_keys_button = tk.Button(self.virtual_piano_frame, text='Record a melody by pressing piano keys', command=lambda:[record_melody_by_pressing_keys.record_melody()])
        record_melody_by_keys_button.pack()

        stop_record_melody_button = tk.Button(self.virtual_piano_frame, text='Stop recording the melody by pressing piano keys',
                                            command=lambda:[record_melody_by_pressing_keys.stop_recording_melody(self.virtual_piano_frame)])
        stop_record_melody_button.pack()
        
        record_melody_by_text_button = tk.Button(self.virtual_piano_frame, text='Record a melody by inserting notes as text', command=lambda:[record_melody_by_text.save_melody_popup_window(self.virtual_piano_frame)])
        record_melody_by_text_button.pack()

        view_melodies_button = tk.Button(self.virtual_piano_frame, text="View melodies", 
                        command=lambda:[self.change_to_view_melodies_frame(view_melodies_frame)])
        view_melodies_button.pack()

        view_global_melodies_button = tk.Button(self.virtual_piano_frame, text="View global melodies", 
                        command=lambda:[self.change_to_view_melodies_frame(view_global_melodies_frame)])
        view_global_melodies_button.pack()

        logout_button = tk.Button(self.virtual_piano_frame, text="Logout", 
                        command=lambda:[self.change_to_login_frame(login_frame)])
        logout_button.pack()
