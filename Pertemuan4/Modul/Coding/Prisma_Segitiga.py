import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from Fungsi import Luas_Prisma_segitiga, volume_Prisma_segitiga

def hitung_luas():
    alas = float(txt_alas.get())
    t_alas   = float(txtt_alas.get())
    t_prisma  = float(txtt_prisma.get())

    L = Luas_Prisma_segitiga (alas,t_alas,t_prisma)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas    = float(txt_alas.get())
    t_alas   = float(txtt_alas.get())
    t_prisma  = float(txtt_prisma.get())

    V = volume_Prisma_segitiga (alas,t_alas,t_prisma)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# t_alasmbahkan judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

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

# Label alas
alas = Label(frame, text="Alas:") 
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label t_alas
t_alas = Label(frame, text="Tinggi Alas:") 
t_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label t_prisma
t_prisma = Label(frame, text="Tinggi Prisma:") 
t_prisma.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox alas
txt_alas = Entry(frame)
txt_alas.grid(row=0, column=1)

# Textbox t_alas
txtt_alas = Entry(frame)
txtt_alas.grid(row=1, column=1)

# Textbox t_prisma
txtt_prisma = Entry(frame)
txtt_prisma.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()