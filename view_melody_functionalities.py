import tkinter as tk
import record_melody

WINDOW_HEIGHT = 500


class ViewMelodiesFrame:
    def __init__(self, app):
        self.view_melodies_frame = tk.Frame(app)

    def change_to_virtual_piano_frame(self, virtual_piano_frame):
        virtual_piano_frame.virtual_piano_frame.pack(fill='both', expand=1)
        self.view_melodies_frame.pack_forget()

    def create_fields(self, virtual_piano_frame):
        logout_button = tk.Button(self.view_melodies_frame, text="Back", 
                        command=lambda:[self.change_to_virtual_piano_frame(virtual_piano_frame)])
        logout_button.pack()