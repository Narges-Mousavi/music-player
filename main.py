import tkinter as tk
from moviepy.editor import *
import moviepy.video.fx.all as vfx
from pygame import mixer
from tkinter import filedialog
import pygame as pg


mp = tk.Tk()
mp.title('Music_player')
img = tk.PhotoImage(file='icon2.png')
mp.iconphoto(False, img)


def menu():
    mixer.init()
    music = filedialog.askopenfilenames(initialdir='audio/', title='choose the music')
    for i in music:
        play_list_box.insert('end', i)
        mixer.music.load(i)
    play3 = play_list_box


global play
play = False


def play_pause(play2): 
    try:
        global play
        play = play2
        mixer.init()
        if mixer.music.get_pos() == -1:
            music = play_list_box.get('active')
            mixer.music.load(music)
            mixer.music.play()
        else:
            if play == True:
                mixer.music.pause()
                play = False

            else:
                mixer.music.unpause()
                play = True
    except pg.error:
        Lp = tk.Label(mp, text='No music has been\n uploaded yet', font=('Times New Roman', 12, 'bold'), bd=2)
        Lp.place(x=290, y=218, height=75)


def next_song():
    try:
        next_music = play_list_box.curselection()
        next_music = next_music[0] + 1
        music = play_list_box.get(next_music)
        # music = play_list_box.get('active')
        mixer.music.load(music)
        mixer.music.play()
        play_list_box.selection_clear(0, 'end')
        play_list_box.selection_set(next_music)
    except pg.error:
        play_list_box.selection_clear(0, 'end')
        play_list_box.selection_set(0, 0)
        music = play_list_box.get('active')
        mixer.music.load(music)
        mixer.music.play()
    except IndexError:
        Ln = tk.Label(mp, text='No music has been\n uploaded yet', font=('Times New Roman', 12, 'bold'))
        Ln.place(x=290, y=218, height=75)


def repeat_song():
    try:
        play_list_box.selection_get()
        mixer.music.play()
    except:
        Lr = tk.Label(mp, text='No music has been\n uploaded yet', font=('Times New Roman', 12, 'bold'), bd=2)
        Lr.place(x=290, y=218, height=75)


def vol_up():
    mixer.music.set_volume(mixer.music.get_volume() + 0.1)


def vol_down():
    mixer.music.set_volume(mixer.music.get_volume() - 0.1)


lst = []


def forward():
    try:
        second = skip_entry.get()
        if second:
            lst.append(mixer.music.get_pos() / 1000 + float(second))
            mixer.music.play(loops=0, start=(sum(lst)))
            if float(second) < 0:
                lst.append(mixer.music.get_pos() / 1000 - (float(second)))
                mixer.music.play(loops=0, start=(sum(lst)))
        else:
            lst.append(mixer.music.get_pos() / 1000 + 15.0)
            mixer.music.play(loops=0, start=(sum(lst)))
    except pg.error:
        Lf = tk.Label(mp, text='No music has been\n uploaded yet', font=('Times New Roman', 12, 'bold'), bd=2)
        Lf.place(x=290, y=218, height=75)
    except ValueError:
        Le = tk.Label(mp, text='                                 \n                              \n', font=('Times New Roman', 12, 'bold'), bd=2)
        Le.place(x=290, y=218, height=75)
        Lv = tk.Label(mp, text='Please enter a \n correct number', font=('Times New Roman', 12, 'bold'), bd=2)
        Lv.place(x=290, y=218, height=75)


def backward():
    try:
        second = skip_entry.get()
        if second:
            lst.append(mixer.music.get_pos() / 1000 - float(second))
            mixer.music.play(loops=0, start=(sum(lst)))
            if float(second) < 0:
                lst.append(mixer.music.get_pos() / 1000 + float(second))
                mixer.music.play(loops=0, start=(sum(lst)))
        else:
            lst.append(mixer.music.get_pos() / 1000 - 15.0)
            mixer.music.play(loops=0, start=(sum(lst)))
    except pg.error:
        Lb = tk.Label(mp, text='No music has been\n uploaded yet', font=('Times New Roman', 12, 'bold'), bd=2)
        Lb.place(x=290, y=218, height=75)
    except ValueError:
        Le = tk.Label(mp, text='                                 \n                              \n', font=('Times New Roman', 12, 'bold'), bd=2)
        Le.place(x=290, y=218, height=75)
        Lv = tk.Label(mp, text='Please enter a \n correct number', font=('Times New Roman', 12, 'bold'), bd=2)
        Lv.place(x=290, y=218, height=75)


def speed():
    try:
        play_speed = (speed_entry.get())
        pg.display.set_caption('play')
        music_path = play_list_box.get('active')
        sound = AudioFileClip(r'{}'.format(music_path))
        sound = vfx.speedx(sound, factor=float(play_speed))
        sound.preview()
        pg.quit()
    except:
        Le = tk.Label(mp, text='                                 \n                              \n', font=('Times New Roman', 12, 'bold'), bd=2)
        Le.place(x=290, y=218, height=75)
        Lv = tk.Label(mp, text='Please enter a \n correct number', font=('Times New Roman', 12, 'bold'), bd=2)
        Lv.place(x=290, y=218, height=75)


songlabelframe= tk.LabelFrame(mp, padx=16, pady=16, bd=8, text='Play list', width=370, font=('Times New Roman', 11, 'bold'), height=138).place(x=90, y=0)
play_list_box = tk.Listbox(songlabelframe, bg='white', fg='#CC0066', selectbackground='#990099')
play_list_box.place(x=100, y=20, width=345, height=105)
btn_menu = tk.Button(mp, padx=16, pady=16, bd=8, text='Menu', width=3, font=('Times New Roman', 11, 'bold'), bg='#ff9933', fg='black', command=lambda: menu()).grid(row=1, column=4)
btn_play_pause = tk.Button(mp, padx=16, pady=16, bd=8, text='Play/Pause', width=4, font=('Times New Roman', 10, 'bold'), bg='#FFFF66', fg='black', command=lambda: play_pause(play)).grid(row=2, column=4)
btn_next = tk.Button(mp, padx=16, pady=16, bd=8, text='Next', width=3, font=('Times New Roman', 12, 'bold'), bg='#FF99CC', fg='black', command=next_song).grid(row=3, column=4)
btn_repeat = tk.Button(mp, padx=16, pady=16, bd=8, text='Repeat', width=3, font=('Times New Roman', 12, 'bold'), bg='#e5ccff', fg='black', command=lambda: repeat_song()).grid(row=4, column=4)
skip_entry = tk.Entry(mp, width=3, bg='#E5CCFF', font=('Times New Roman', 39), bd=3)
skip_entry.grid(row=3, column=30, sticky='w', columnspan=9, padx=5, pady=5)
btn_skip_forward = tk.Button(mp, padx=16, pady=16, bd=8, text='▶▶', width=3, font=('Times New Roman', 11, 'bold'), bg='#CCFFCC', fg='black', command=lambda: forward()).grid(row=3, column=41)
btn_skip_back = tk.Button(mp, padx=16, pady=16, bd=8, text='◀◀', width=3, font=('Times New Roman', 11, 'bold'), bg='#CCFFCC', fg='black', command=lambda: backward()).grid(row=3, column=26)
volume_up = tk.Button(mp, padx=16, pady=16, bd=8, text='🔊', width=1, font=('Times New Roman', 13), bg='#ff9999', fg='black', command=lambda: vol_up()).grid(row=3, column=50)
volume_down = tk.Button(mp, padx=16, pady=16, bd=8, text='🔉', width=1, font=('Times New Roman', 13), bg='#CCE5FF', fg='black', command=lambda: vol_down()).grid(row=3, column=5)
speed_entry = tk.Entry(mp, width=3, bg='#E5CCFF', font=('Times New Roman', 39), bd=3)
speed_entry.place(x=165, y=218, height=72)
speed_btn = tk.Button(mp, padx=16, pady=16, bd=8, text='speed\ncontrol', width=3, font=('Times New Roman', 12, 'bold'), bg='#FFCCFF', fg='black', command=lambda: speed()).place(x=81, y=218, height=75)

# Speed entry = 2 --> music plays with 2x speed

mp.mainloop()
# Tkinter - pygame - music player
