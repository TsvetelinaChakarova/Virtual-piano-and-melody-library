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

#set piano as button
piano_image = Image.open("piano.jpg")
piano_image = piano_image.resize((500, 300))
piano_tk_image = ImageTk.PhotoImage(piano_image)
piano_button = tk.Button(app)
piano_button.pack()
piano_button.config(image = piano_tk_image)

app.mainloop()