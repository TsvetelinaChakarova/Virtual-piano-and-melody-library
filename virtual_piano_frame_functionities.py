import tkinter as tk
import record_melody

WINDOW_HEIGHT = 500

def create_virtual_piano_fields(virtual_piano_frame):
    record_melody_button = tk.Button(virtual_piano_frame, text='Record a melody', command=lambda:[record_melody.record_melody()])
    record_melody_button.pack()

    stop_record_melody_button = tk.Button(virtual_piano_frame, text='Stop recording a melody',
                                        command=lambda:[record_melody.stop_recording_melody(virtual_piano_frame)])
    stop_record_melody_button.pack()
