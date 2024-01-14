import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def get_Celcius():
    suhu = txtsuhu.get()
    C = float(suhu) - 273
    txtCelcius.delete(0,END)
    txtCelcius.insert(END,C)

def get_Fahrenheit():
    suhu = txtsuhu.get()
    F = 9/5 * (float(suhu) - 273) + 32
    txtFahrenheit.delete(0,END)
    txtFahrenheit.insert(END,F)

def get_Reamur():
    suhu = txtsuhu.get()
    R = 4/5 * (float(suhu) - 273)
    txtReamur.delete(0,END)
    txtReamur.insert(END,R)

def hitung():
    get_Celcius()
    get_Fahrenheit()
    get_Reamur()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Suhu Kelvin")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label 
suhu= Label(frame, text="Kelvin:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox 
txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

C= Label(frame, text="Celcius:")
C.grid(row=3, column=0, sticky=W, padx=5, pady=5)

F= Label(frame, text="Fahrenheit:")
F.grid(row=4, column=0, sticky=W, padx=5, pady=5)

R= Label(frame, text="Reamur:")
R.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox 
txtCelcius = Entry(frame)
txtCelcius.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtReamur = Entry(frame)
txtReamur.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()