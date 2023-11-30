import tkinter as tk
from tkinter import Menu

from Balok import *
from Bola import *
from Kubus import *
from Kerucut import *
from Limas_Segiempat import *
from Limas_Segitiga import *
from Prisma_Segitiga import *
from Selinder import *


# window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")

# membuat menubar
menubar = Menu(root)
root.config(menu=menubar)

# membuat menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
#data_menu = Menu(menubar)

# untuk menambahkan menu item pada menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label=' Balok', command= lambda: new_window("Luas Balok", Balok)
)
app_menu.add_command(
    label=' Bola', command= lambda: new_window(" Luas Bola", Bola)
)
app_menu.add_command(
    label=' Kerucut', command= lambda: new_window(" Kerucut", Kerucut)
)
app_menu.add_command(
    label='Limas Segiempat', command= lambda: new_window(" Limas Segiempat", Limas_Segiempat)
)
app_menu.add_command(
    label='Limas Segitiga', command= lambda: new_window(" Limas Segitiga", Limas_Segitiga)
)
app_menu.add_command(
    label=' Prisma Segitiga ', command= lambda: new_window(" Prisma Segitiga", Prisma_Segitiga)
)
app_menu.add_command(
    label='Selinder', command= lambda: new_window(" Selinder", Selinder)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()