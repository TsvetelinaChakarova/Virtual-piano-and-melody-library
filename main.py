import tkinter as tk
from PIL import ImageTk, Image

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 400

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

app.mainloop()