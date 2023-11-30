from tkinter import *
from gtts import gTTS
from playsound import playsound

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech")

        self.text_to_speech = StringVar()

        self.label = Label(master, text="Masukkan Teks:")
        self.label.pack(pady=10)

        self.text_entry = Entry(master, textvariable=self.text_to_speech, width=40)
        self.text_entry.pack(pady=10)

        self.play_button = Button(master, text="Putar", command=self.play_audio)
        self.play_button.pack(pady=10)

    def play_audio(self):
        text = self.text_to_speech.get()
        if text:
            tts = gTTS(text=text, lang='id')  # Ganti 'id' dengan kode bahasa yang diinginkan
            tts.save("output.mp3")
            playsound("output.mp3")

if __name__ == "__main__":
    root = Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
