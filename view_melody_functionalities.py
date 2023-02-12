import tkinter as tk
from tkinter import ttk
import database_functionalities
import login_frame_functionalities

import record_melody

WINDOW_HEIGHT = 500


class ViewMelodiesFrame:
    def __init__(self, app):
        self.view_melodies_frame = tk.Frame(app)

    def display_users_melodies(self, database): 
        treeview = ttk.Treeview(self.view_melodies_frame, column=("melody_name"), show='headings')
        treeview["columns"] = ("melody_name")
        treeview.column("melody_name", anchor=tk.CENTER)
        treeview.heading("melody_name", text="Melody name")
        treeview.pack()
        
        print(login_frame_functionalities.current_user_role)
        melodies = database_functionalities.get_users_melodies(login_frame_functionalities.current_user_username)
        for melody in melodies:
            treeview.insert("", tk.END, melody, text=melody, values=(melody,))
        return treeview

    def change_to_virtual_piano_frame(self, virtual_piano_frame):
        virtual_piano_frame.virtual_piano_frame.pack(fill='both', expand=1)
        self.view_melodies_frame.pack_forget()

    def create_fields(self, virtual_piano_frame):
        go_back_button = tk.Button(self.view_melodies_frame, text="Back", 
                        command=lambda:[self.change_to_virtual_piano_frame(virtual_piano_frame)])
        go_back_button.pack()