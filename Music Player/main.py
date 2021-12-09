import os
from tkinter import *
from typing import List
from tkinter import filedialog
from pygame import init, mixer

cwd = os.getcwd()
cw = cwd.replace("\\","/")
cw = cw + "/"
mixer.init()

def Play_this():
    this = songs.curselection()
    this = this[0]
    song_is = songs.get(this)
    mixer.music.load(song_is)
    mixer.music.play()
    return
def Play():
    this = songs.curselection()
    this = this[0]
    song_is = songs.get(ACTIVE)
    songs.select_set(this)
    mixer.music.load(song_is)
    mixer.music.play()
    pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    
    
def Resume():
    mixer.music.unpause()
    pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    return
def Next():
    n = len(songs_)
    this = songs.curselection()
    
    this = this[0]
    if this != n-1:
        to_play = songs.get(this+1)
        songs.selection_clear(0,END)
        songs.select_set(this+1)
        mixer.music.load(to_play)
        mixer.music.play()
        pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    else:
        to_play = songs.get(0)
        songs.selection_clear(0,END)
        songs.select_set(0)
        mixer.music.load(to_play)
        mixer.music.play()
        pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    
    return
def Previous():
    n = len(songs_)
    this = songs.curselection()
    this = this[0]
    if this == 0:
        to_play = songs.get(0)
        songs.selection_clear(0,END)
        songs.select_set(0)
        mixer.music.load(to_play)
        mixer.music.play()
        pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    if this !=0:
        to_play = songs.get(this-1)
        songs.selection_clear(0,END)
        songs.select_set(this-1)
        mixer.music.load(to_play)
        mixer.music.play()
        pause = Button(window, text = "Pause", width = 7, command = Pause).grid(row = 1, column = 0)
    return


def Pause():
    mixer.music.pause()
    resume = Button(window, text = "resume", width = 7, command = Resume).grid(row = 1, column = 0)
    return
def addsongs():
    global songs_
    songs_ = filedialog.askopenfilenames(title = "Choose Songs", initialdir= cw, filetypes = (("music files","*.ogg"),))
    
    i = 0
    for s in songs_:
        i+=1
        s = s.replace(cw,"")
        songs.insert(i,s)
    return
def deletesong():
    list_to_delete = songs.curselection()
    mixer.music.stop()
    songs.delete(list_to_delete[0])
    play = Button(window, text = "Play", width = 7, command = Play).grid(row = 1, column =0)
    return




window = Tk()
icon = PhotoImage(file = r'images\draft.png') #images need to be convertd as photoimage before using

window.iconphoto(True, icon)
window.title("Start Music")
window.geometry("400x350")
songs = Listbox(window, selectmode= SINGLE, height = 12, width= 47)
songs.grid(row = 0, column = 0, columnspan=9)

songs_ = []
play = Button(window, text = "Play", width = 7, command = Play).grid(row = 1, column =0)
next = Button(window, text = "Next", width = 7, command = Next).grid(row = 1, column = 1)
previous = Button(window, text = "Previous", width = 7, command = Previous).grid(row = 1, column = 2)
play_this = Button(window, text = "Play this", width = 7, command = Play_this).grid(row = 1, column = 3)

menubar = Menu(window)
window.config(menu = menubar)
fileMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Add songs", command = addsongs)
fileMenu.add_command(label = "Delete song", command = deletesong)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = quit)
editMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editMenu)

window.mainloop()