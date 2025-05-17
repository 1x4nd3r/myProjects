from tkinter import *
import pygame
import os
import random

class MusicPlayer:
    def __init__(self, root):
        fontFamily = "Consolas"
        fontColor = "silver"
        bgColor = "navyblue"
        accentColor = "grey"

        self.root = root
        self.root.title("Music Player >w<")
        self.root.geometry("600x400")
        self.root.config(bg=bgColor)

        pygame.init()
        pygame.mixer.init()
        self.is_playing = False
        self.current_index = 0
        self.shuffle_mode = False
        self.hasStarted = False

        self.track = StringVar()
        self.status = StringVar()

        os.chdir("C:/Users/Alex/Music")
        self.songtracks = [track for track in os.listdir() if track.endswith('.mp3')]

        self.playlistbox = Listbox(self.root, selectmode=SINGLE, bg=accentColor, fg=fontColor, font=(fontFamily, 12))
        self.playlistbox.place(x=20, y=20, width=560, height=300)

        for track in self.songtracks:
            self.playlistbox.insert(END, track)

        self.playlistbox.bind("<Double-Button-1>", self.play_selected_song)

        buttonframe = LabelFrame(self.root, text="", font=(fontFamily, 15, "bold"), bg=bgColor, fg=fontColor)
        buttonframe.place(x=0, y=340, width=600, height=60)

        self.prevbtn = Button(buttonframe, text="START", command=self.previous_song, width=10, font=("Consolas", 16, "bold"), fg="silver", bg="grey")
        self.prevbtn.grid(row=0, column=0, padx=10, pady=5)

        play_pause_btn = Button(buttonframe, text="PLAY/PAUSE", command=self.toggle_play_pause, width=10, font=(fontFamily, 16, "bold"), fg=fontColor, bg=accentColor)
        play_pause_btn.grid(row=0, column=1, padx=10, pady=5)

        nextbtn = Button(buttonframe, text="NEXT", command=self.next_song, width=10, font=(fontFamily, 16, "bold"), fg=fontColor, bg=accentColor)
        nextbtn.grid(row=0, column=2, padx=10, pady=5)

        shufflebtn = Button(buttonframe, text="SHUFFLE", command=self.toggle_shuffle, width=10, font=(fontFamily, 16, "bold"), fg=fontColor, bg=accentColor)
        shufflebtn.grid(row=0, column=3, padx=10, pady=5)

    def playsong(self):
        if self.songtracks:
            selected_song = self.songtracks[self.current_index]
            self.track.set(selected_song)
            self.status.set("-Playing")
            pygame.mixer.music.load(os.path.join("C:/Users/Alex/Music", selected_song))
            pygame.mixer.music.play()
            self.is_playing = True

    def toggle_play_pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.status.set("-Paused")
        else:
            pygame.mixer.music.unpause()
            self.status.set("-Playing")
        self.is_playing = not self.is_playing

    def shuffle_song(self):
        if self.songtracks:
            self.current_index = random.randint(0, len(self.songtracks) - 1)
            self.playsong()

    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode

    def next_song(self):
        if self.songtracks:
            if self.shuffle_mode:
                self.shuffle_song()
            else:
                self.current_index = (self.current_index + 1) % len(self.songtracks)
                self.playsong()

    def previous_song(self):
        if self.songtracks:
            if not self.hasStarted:
                self.hasStarted = True
                self.prevbtn.config(text="PREV")

            self.current_index = (self.current_index - 1) % len(self.songtracks)
            self.playsong()

    def play_selected_song(self, event):
        selected_index = self.playlistbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            self.playsong()

root = Tk()
app = MusicPlayer(root)
root.mainloop()
