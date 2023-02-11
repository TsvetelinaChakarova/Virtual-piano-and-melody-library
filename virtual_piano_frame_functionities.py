import tkinter as tk
import record_melody

WINDOW_HEIGHT = 500


class VirtualPianoFrame:
    def __init__(self, app):
        self.virtual_piano_frame = tk.Frame(app)

    def change_to_login_frame(self, login_frame):
        login_frame.login_frame.pack(fill='both', expand=1)
        self.virtual_piano_frame.pack_forget()

    def create_fields(self, login_frame):
        record_melody_button = tk.Button(self.virtual_piano_frame, text='Record a melody', command=lambda:[record_melody.record_melody()])
        record_melody_button.pack()

        stop_record_melody_button = tk.Button(self.virtual_piano_frame, text='Stop recording a melody',
                                            command=lambda:[record_melody.stop_recording_melody(self.virtual_piano_frame)])
        stop_record_melody_button.pack()

        logout_button = tk.Button(self.virtual_piano_frame, text="Logout", 
                        command=lambda:[self.change_to_login_frame(login_frame)])
        logout_button.pack()
