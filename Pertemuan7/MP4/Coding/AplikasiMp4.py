import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.video_path = None

        self.label = tk.Label(master, text="Pemutar Video MP4")
        self.label.pack(pady=10)

        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_video)
        self.stop_button.pack(pady=5)

        self.select_button = tk.Button(master, text="Pilih Video", command=self.select_video)
        self.select_button.pack(pady=10)

        self.video_label = tk.Label(master)
        self.video_label.pack()

        self.video_cap = None

    def play_video(self):
        if self.video_path:
            self.video_cap = cv2.VideoCapture(self.video_path)
            self.show_frame()

    def stop_video(self):
        if self.video_cap:
            self.video_cap.release()
            self.video_cap = None
            self.video_label.configure(image=None)

    def show_frame(self):
        _, frame = self.video_cap.read()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image)

            self.video_label.configure(image=photo)
            self.video_label.image = photo

            self.video_label.after(10, self.show_frame)
        else:
            self.stop_video()

    def select_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if video_path:
            self.video_path = video_path
            self.stop_video()
            self.video_label.configure(image=None)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
