import tkinter as tk
from tkinter import messagebox

def save_data():
    data = entry_data.get()
    if not data:
        messagebox.showwarning("Input Error", "Tolong Masukan Data.")
        return

    with open("Jadwal_kuliah.txt", "a") as file:
        file.write(data + "\n")
    
    entry_data.delete(0, tk.END)
    messagebox.showinfo("Success", "Data Telah berhasil disimpan.")

def read_data():
    try:
        with open("Jadwal_kuliah.txt", "r") as file:
            data_text.config(state=tk.NORMAL)
            data_text.delete(1.0, tk.END)
            data_text.insert(tk.END, file.read())
            data_text.config(state=tk.DISABLED)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Belum ada data yang di masukan.")

# Gui tampilan 
app = tk.Tk()
app.title("GUI Jadwal Kuliah by.Roy ZIkin")

label_data = tk.Label(app, text="Masukan Jadwal Kuliah :")
label_data.pack()

entry_data = tk.Entry(app, width=40)
entry_data.pack()

save_button = tk.Button(app, text="Simpan Data", command=save_data)
save_button.pack(pady=10)

read_button = tk.Button(app, text="Muat Data", command=read_data)
read_button.pack(pady=10)

data_text = tk.Text(app, height=10, width=40, state=tk.DISABLED)
data_text.pack()

app.mainloop()
