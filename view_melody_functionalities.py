import tkinter as tk
from tkinter import ttk
import database_functionalities
import login_frame_functionalities
import pygame

WINDOW_HEIGHT = 500


class ViewMelodiesFrame:
    def __init__(self, app):
        self.view_melodies_frame = tk.Frame(app)
        self.treeview = self.display_users_melodies()

    def create_treeview(self):
        self.treeview = ttk.Treeview(self.view_melodies_frame, column=("melody_name"), show='headings')
        self.treeview["columns"] = ("melody_name")
        self.treeview.column("melody_name", anchor=tk.CENTER)
        self.treeview.heading("melody_name", text="Melody name")
        self.treeview.pack()

    def display_users_melodies(self):
        self.create_treeview()
        cursor = database_functionalities.database.cursor()
        cursor.execute(
            "SELECT name FROM melodys WHERE creators_username = '""" + login_frame_functionalities.current_user_username + "'")
        rows = cursor.fetchall()
        for row in rows:
            self.treeview.insert("", tk.END, values=row)
        return self.treeview

    def play_melody(self):
        selected_item = self.treeview.selection()
        path_to_melody = "Melodys\\" + login_frame_functionalities.current_user_username + "\\" + \
                         self.treeview.item(selected_item)['values'][0] + ".wav"
        pygame.mixer.init()
        my_sound = pygame.mixer.Sound(path_to_melody)
        my_sound.play()

    def change_to_virtual_piano_frame(self, virtual_piano_frame):
        virtual_piano_frame.virtual_piano_frame.pack(fill='both', expand=1)
        self.view_melodies_frame.pack_forget()

    def search_melody(self, search_input_field):
        self.treeview.destroy()
        self.create_treeview()
        keyword = search_input_field.get()
        cursor = database_functionalities.database.cursor()
        cursor = cursor.execute(
            "SELECT name FROM melodys WHERE creators_username = '" + login_frame_functionalities.current_user_username + "' AND (keywords LIKE '" + keyword + " %' or keywords LIKE '% " + keyword + "' or keywords LIKE '% " + keyword + " %' or keywords LIKE '" + keyword + "')")
        rows = cursor.fetchall()
        for row in rows:
            self.treeview.insert("", tk.END, values=row)
        self.view_melodies_frame.pack()

    def create_fields(self, virtual_piano_frame):
        tk.Label(self.view_melodies_frame, text="Input a keyword:").pack()
        search_input_field = tk.Entry(self.view_melodies_frame)
        search_input_field.pack()

        search_button = tk.Button(self.view_melodies_frame, text="Search",
                                  command=lambda: [self.search_melody(search_input_field)])
        search_button.pack()
        play_button = tk.Button(self.view_melodies_frame, text="Play",
                                command=lambda: [self.play_melody()])
        play_button.pack()

        go_back_button = tk.Button(self.view_melodies_frame, text="Back",
                                   command=lambda: [self.change_to_virtual_piano_frame(virtual_piano_frame)])
        go_back_button.pack()
