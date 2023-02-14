import tkinter as tk
import record_melody
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
        record_melody_button = tk.Button(self.virtual_piano_frame, text='Record a melody', command=lambda:[record_melody.record_melody()])
        record_melody_button.pack()

        stop_record_melody_button = tk.Button(self.virtual_piano_frame, text='Stop recording a melody',
                                            command=lambda:[record_melody.stop_recording_melody(self.virtual_piano_frame)])
        stop_record_melody_button.pack()

        view_melodies_button = tk.Button(self.virtual_piano_frame, text="View melodies", 
                        command=lambda:[self.change_to_view_melodies_frame(view_melodies_frame)])
        view_melodies_button.pack()

        view_global_melodies_button = tk.Button(self.virtual_piano_frame, text="View global melodies", 
                        command=lambda:[self.change_to_view_melodies_frame(view_global_melodies_frame)])
        view_global_melodies_button.pack()

        logout_button = tk.Button(self.virtual_piano_frame, text="Logout", 
                        command=lambda:[self.change_to_login_frame(login_frame)])
        logout_button.pack()
