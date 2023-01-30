import tkinter as tk
from PIL import ImageTk, Image
import play_sound 

WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 500
BLACK_PIANO_KEY_WIDTH = 30
BLACK_PIANO_KEY_HEIGHT = 140
WHITE_PIANO_KEY_WIDTH = 60
WHITE_PIANO_KEY_HEIGHT = 200

app = tk.Tk()
app.title("Music Library")

#set current, min and max window size
app.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
app.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

size_by_pixel = tk.PhotoImage(width=1, height=1)

#set white piano keys as buttons
white_key_1 = tk.Button(app, text="C3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_C3)  
white_key_1.place(x=WHITE_PIANO_KEY_WIDTH*0, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)

white_key_2 = tk.Button(app, text="D3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_D3)  
white_key_2.place(x=WHITE_PIANO_KEY_WIDTH*1, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)   

white_key_3 = tk.Button(app, text="E3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_E3)  
white_key_3.place(x=WHITE_PIANO_KEY_WIDTH*2, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_4 = tk.Button(app, text="F3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_F3)  
white_key_4.place(x=WHITE_PIANO_KEY_WIDTH*3, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_5 = tk.Button(app, text="G3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_G3)  
white_key_5.place(x=WHITE_PIANO_KEY_WIDTH*4, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_6 = tk.Button(app, text="A3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_A3)  
white_key_6.place(x=WHITE_PIANO_KEY_WIDTH*5, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_7 = tk.Button(app, text="B3", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_B3)  
white_key_7.place(x=WHITE_PIANO_KEY_WIDTH*6, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_8 = tk.Button(app, text="C4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_C4)  
white_key_8.place(x=WHITE_PIANO_KEY_WIDTH*7, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_9 = tk.Button(app, text="D4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_D4)  
white_key_9.place(x=WHITE_PIANO_KEY_WIDTH*8, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_10 = tk.Button(app, text="E4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_E4)  
white_key_10.place(x=WHITE_PIANO_KEY_WIDTH*9, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_11 = tk.Button(app, text="F4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_F4)  
white_key_11.place(x=WHITE_PIANO_KEY_WIDTH*10, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_12 = tk.Button(app, text="G4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_G4)  
white_key_12.place(x=WHITE_PIANO_KEY_WIDTH*11, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_13 = tk.Button(app, text="A4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_A4)  
white_key_13.place(x=WHITE_PIANO_KEY_WIDTH*12, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_14 = tk.Button(app, text="B4", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_B4)  
white_key_14.place(x=WHITE_PIANO_KEY_WIDTH*13, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_15 = tk.Button(app, text="C5", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_C5)  
white_key_15.place(x=WHITE_PIANO_KEY_WIDTH*14, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_16 = tk.Button(app, text="D5", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_D5)  
white_key_16.place(x=WHITE_PIANO_KEY_WIDTH*15, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

white_key_17 = tk.Button(app, text="E5", fg="#000", image=size_by_pixel, bg='#FFF', height=WHITE_PIANO_KEY_HEIGHT, width=WHITE_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_E5)  
white_key_17.place(x=WHITE_PIANO_KEY_WIDTH*16, y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT) 

#set black piano keys as buttons
black_key_1 = tk.Button(app, text="C#3", fg="#FFF",image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Cs3)  
black_key_1.place(x=(WHITE_PIANO_KEY_WIDTH*0)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)

black_key_2 = tk.Button(app, text="D#3", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Ds3)  
black_key_2.place(x=(WHITE_PIANO_KEY_WIDTH*1)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_3 = tk.Button(app, text="F#3", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Fs3)  
black_key_3.place(x=(WHITE_PIANO_KEY_WIDTH*3)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_4 = tk.Button(app, text="G#3", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Gs3)  
black_key_4.place(x=(WHITE_PIANO_KEY_WIDTH*4)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_5 = tk.Button(app, text="A#3", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_As3)  
black_key_5.place(x=(WHITE_PIANO_KEY_WIDTH*5)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)

black_key_6 = tk.Button(app, text="C#4", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Cs4)  
black_key_6.place(x=(WHITE_PIANO_KEY_WIDTH*7)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_7 = tk.Button(app, text="D#4", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Ds4)  
black_key_7.place(x=(WHITE_PIANO_KEY_WIDTH*8)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_8 = tk.Button(app, text="F#4", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Fs4)  
black_key_8.place(x=(WHITE_PIANO_KEY_WIDTH*10)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_9 = tk.Button(app, text="G#4", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Gs4)  
black_key_9.place(x=(WHITE_PIANO_KEY_WIDTH*11)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_10 = tk.Button(app, text="A#4", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_As4)  
black_key_10.place(x=(WHITE_PIANO_KEY_WIDTH*12)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)

black_key_11 = tk.Button(app, text="C#5", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Cs5)  
black_key_11.place(x=(WHITE_PIANO_KEY_WIDTH*14)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)
   
black_key_12 = tk.Button(app, text="D#5", fg="#FFF", image=size_by_pixel, bg='#000', height=BLACK_PIANO_KEY_HEIGHT, width=BLACK_PIANO_KEY_WIDTH, compound='bottom', anchor="s", command=play_sound.play_Ds5)  
black_key_12.place(x=(WHITE_PIANO_KEY_WIDTH*15)+(WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH/2), y=WINDOW_HEIGHT-WHITE_PIANO_KEY_HEIGHT)

app.mainloop()