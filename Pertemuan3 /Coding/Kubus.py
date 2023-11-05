import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    ss = float(txtsisi.get())

    L = round (6 * ss **2)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L) 

def hitung_volume():
    ss = float(txtsisi.get())

    K = round (ss **3)

    txtvolume.delete(0,END)
    txtvolume.insert(END,K)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

#Nametag
nametag = tk.Frame(frame, bg="Green", height=50)
nametag.grid(row=6, column=1, columnspan=1, sticky='ew', pady=10)

nama = Label(nametag, text="Roy Zikin", bg='Green')
nama.grid(row=6, column=1, sticky='nsew' , padx=5, pady=5)

nametag.grid_rowconfigure(6, weight=1)
nametag.grid_columnconfigure(1, weight=1)

# Label sisi
sisi = Label(frame, text="Sisi:") 
sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox sisi
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()