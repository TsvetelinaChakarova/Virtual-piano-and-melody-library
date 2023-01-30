import tkinter as tk
import key_buttons

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

size_by_pixel = tk.PhotoImage(width=1, height=1)
key_buttons.create_key_buttons(app, WINDOW_HEIGHT, size_by_pixel)

app.mainloop()