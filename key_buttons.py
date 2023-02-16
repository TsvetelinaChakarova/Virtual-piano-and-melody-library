#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import ImageTk, Image
import play_sound

BLACK_PIANO_KEY_WIDTH = 30
BLACK_PIANO_KEY_HEIGHT = 140
WHITE_PIANO_KEY_WIDTH = 60
WHITE_PIANO_KEY_HEIGHT = 200

is_record_melody_pressed = False
melody = []


def which_button_is_pressed(button_press):
    if is_record_melody_pressed:
        melody.append(button_press)


def create_key_buttons(app, WINDOW_HEIGHT, size_by_pixel):
    # set white piano keys as buttons

    C3_key = tk.Button(
        app,
        text='C3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_C3(), which_button_is_pressed('C3')],
    )
    C3_key.place(x=WHITE_PIANO_KEY_WIDTH * 0, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    D3_key = tk.Button(
        app,
        text='D3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_D3(), which_button_is_pressed('D3')],
    )
    D3_key.place(x=WHITE_PIANO_KEY_WIDTH * 1, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    E3_key = tk.Button(
        app,
        text='E3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_E3(), which_button_is_pressed('E3')],
    )
    E3_key.place(x=WHITE_PIANO_KEY_WIDTH * 2, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    F3_key = tk.Button(
        app,
        text='F3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_F3(), which_button_is_pressed('F3')],
    )
    F3_key.place(x=WHITE_PIANO_KEY_WIDTH * 3, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    G3_key = tk.Button(
        app,
        text='G3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_G3(), which_button_is_pressed('G3')],
    )
    G3_key.place(x=WHITE_PIANO_KEY_WIDTH * 4, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    A3_key = tk.Button(
        app,
        text='A3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_A3(), which_button_is_pressed('A3')],
    )
    A3_key.place(x=WHITE_PIANO_KEY_WIDTH * 5, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    B3_key = tk.Button(
        app,
        text='B3',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_B3(), which_button_is_pressed('B3')],
    )
    B3_key.place(x=WHITE_PIANO_KEY_WIDTH * 6, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    C4_key = tk.Button(
        app,
        text='C4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_C4(), which_button_is_pressed('C4')],
    )
    C4_key.place(x=WHITE_PIANO_KEY_WIDTH * 7, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    D4_key = tk.Button(
        app,
        text='D4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_D4(), which_button_is_pressed('D4')],
    )
    D4_key.place(x=WHITE_PIANO_KEY_WIDTH * 8, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    E4_key = tk.Button(
        app,
        text='E4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_E4(), which_button_is_pressed('E4')],
    )
    E4_key.place(x=WHITE_PIANO_KEY_WIDTH * 9, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    F4_key = tk.Button(
        app,
        text='F4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_F4(), which_button_is_pressed('F4')],
    )
    F4_key.place(x=WHITE_PIANO_KEY_WIDTH * 10, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    G4_key = tk.Button(
        app,
        text='G4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_G4(), which_button_is_pressed('G4')],
    )
    G4_key.place(x=WHITE_PIANO_KEY_WIDTH * 11, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    A4_key = tk.Button(
        app,
        text='A4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_A4(), which_button_is_pressed('A4')],
    )
    A4_key.place(x=WHITE_PIANO_KEY_WIDTH * 12, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    B4_key = tk.Button(
        app,
        text='B4',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_B4(), which_button_is_pressed('B4')],
    )
    B4_key.place(x=WHITE_PIANO_KEY_WIDTH * 13, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    C5_key = tk.Button(
        app,
        text='C5',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_C5(), which_button_is_pressed('C5')],
    )
    C5_key.place(x=WHITE_PIANO_KEY_WIDTH * 14, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    D5_key = tk.Button(
        app,
        text='D5',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_D5(), which_button_is_pressed('D5')],
    )
    D5_key.place(x=WHITE_PIANO_KEY_WIDTH * 15, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    E5_key = tk.Button(
        app,
        text='E5',
        fg='#000',
        image=size_by_pixel,
        bg='#FFF',
        height=WHITE_PIANO_KEY_HEIGHT,
        width=WHITE_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_E5(), which_button_is_pressed('E5')],
    )
    E5_key.place(x=WHITE_PIANO_KEY_WIDTH * 16, y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)

    # set black piano keys as buttons

    Cs3_key = tk.Button(
        app,
        text='C#3',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Cs3(), which_button_is_pressed('C#3')],
    )
    Cs3_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 0 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Ds3_key = tk.Button(
        app,
        text='D#3',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Ds3(), which_button_is_pressed('D#3')],
    )
    Ds3_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 1 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Fs3_key = tk.Button(
        app,
        text='F#3',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Fs3(), which_button_is_pressed('F#3')],
    )
    Fs3_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 3 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Gs3_key = tk.Button(
        app,
        text='G#3',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Gs3(), which_button_is_pressed('G#3')],
    )
    Gs3_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 4 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    As3_key = tk.Button(
        app,
        text='A#3',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_As3(), which_button_is_pressed('A#3')],
    )
    As3_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 5 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Cs4_key = tk.Button(
        app,
        text='C#4',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Cs4(),
                         which_button_is_pressed('C#4')],
    )
    Cs4_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 7 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Ds4_key = tk.Button(
        app,
        text='D#4',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Ds4(), which_button_is_pressed('D#4')],
    )
    Ds4_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 8 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Fs4_key = tk.Button(
        app,
        text='F#4',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Fs4(), which_button_is_pressed('F#4')],
    )
    Fs4_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 10 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Gs4_key = tk.Button(
        app,
        text='G#4',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Gs4(), which_button_is_pressed('G#4')],
    )
    Gs4_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 11 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    As4_key = tk.Button(
        app,
        text='A#4',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_As4(), which_button_is_pressed('A#4')],
    )
    As4_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 12 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Cs5_key = tk.Button(
        app,
        text='C#5',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Cs5(), which_button_is_pressed('C#5')],
    )
    Cs5_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 14 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT
    )

    Ds5_key = tk.Button(
        app,
        text='D#5',
        fg='#FFF',
        image=size_by_pixel,
        bg='#000',
        height=BLACK_PIANO_KEY_HEIGHT,
        width=BLACK_PIANO_KEY_WIDTH,
        compound='bottom',
        anchor='s',
        command=lambda: [play_sound.play_Ds5(), which_button_is_pressed('D#5')],
    )
    Ds5_key.place(
        x=WHITE_PIANO_KEY_WIDTH * 15 + WHITE_PIANO_KEY_WIDTH - BLACK_PIANO_KEY_WIDTH / 2,
        y=WINDOW_HEIGHT - WHITE_PIANO_KEY_HEIGHT)
