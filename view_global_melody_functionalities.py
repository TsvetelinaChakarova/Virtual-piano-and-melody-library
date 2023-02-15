import tkinter as tk
from tkinter import ttk
import database_functionalities
import login_frame_functionalities
from playsound import playsound
from os import chdir
import record_melody_by_pressing_keys
import pygame

WINDOW_HEIGHT = 500


class ViewGlobalMelodiesFrame:
    def __init__(self, app):
        self.view_melodies_frame = tk.Frame(app)
        self.treeview = ttk.Treeview(self.view_melodies_frame, column=("melody_name"), show='headings')

    def display_users_melodies(self, database): 
        self.treeview["columns"] = ("melody_name", "creators_name")
        self.treeview.column("melody_name", anchor=tk.CENTER)
        self.treeview.heading("melody_name", text="Melody name")
        self.treeview.column("creators_name", anchor=tk.CENTER)
        self.treeview.heading("creators_name", text="Creators name")
        self.treeview.pack()
        
        cursor = database.cursor()
        cursor.execute("""SELECT name, creators_username FROM melodys WHERE visibility = 'User with global rights'""")
        rows = cursor.fetchall()    
        for row in rows:
            self.treeview.insert("", tk.END, values=row)  
        return self.treeview

    def play_melody(self):
        selected_item = self.treeview.selection()
        cursor = database_functionalities.database.cursor()
        cursor.execute("""SELECT path FROM melodys WHERE creators_username = '""" + self.treeview.item(selected_item)['values'][1] + """' AND name = '""" + self.treeview.item(selected_item)['values'][0] + """'""")
        for row in cursor:
            for record in row:
                path_to_melody = record

        pygame.mixer.init()
        my_sound = pygame.mixer.Sound(path_to_melody)
        my_sound.play()

    def change_to_virtual_piano_frame(self, virtual_piano_frame):
        virtual_piano_frame.virtual_piano_frame.pack(fill='both', expand=1)
        self.view_melodies_frame.pack_forget()

    def create_fields(self, virtual_piano_frame):
        play_button = tk.Button(self.view_melodies_frame, text="Play", 
                        command=lambda:[self.play_melody()])
        play_button.pack()

        go_back_button = tk.Button(self.view_melodies_frame, text="Back", 
                        command=lambda:[self.change_to_virtual_piano_frame(virtual_piano_frame)])
        go_back_button.pack()