import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.song_path = None

        self.label = tk.Label(master, text="Pemutar MP3")
        self.label.pack(pady=10)

        self.play_button = tk.Button(master, text="Play", command=self.play_audio)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_audio)
        self.stop_button.pack(pady=5)

        self.select_button = tk.Button(master, text="Pilih Lagu", command=self.select_song)
        self.select_button.pack(pady=10)
        
        pygame.mixer.init()

    def play_audio(self):
        if self.song_path:
            pygame.mixer.music.load(self.song_path)
            pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()

    def select_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if song_path:
            self.song_path = song_path

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
