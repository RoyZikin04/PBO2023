from tkinter import Frame, Label, Entry, Button, Tk, W, BOTH, END

class Reamur:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=True) 
        Label(mainFrame, text='Reamur:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=0, column=1, padx=5, pady=5)  
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5) 
        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5) 
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def get_Celcius(self, suhu):
        val = float(suhu) * 5/4
        return val
    
    def get_fahrenheit(self, suhu):
        val = (float(suhu) * 9/4) + 32 
        return val
    
    def get_kelvin(self, suhu):
        val = (float(suhu) * 5/4) + 273
        return val

    def onHitung(self):
        # Suhu dalam Reamur
        suhu = self.txtReamur.get()
        C = self.get_Celcius(float(suhu))
        self.txtCelcius.delete(0, END)
        self.txtCelcius.insert(END, str(C))

        # Suhu dalam Fahrenheit
        F = self.get_fahrenheit(float(suhu))
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        # Suhu dalam Kelvin
        K = self.get_kelvin(float(suhu))
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()            

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Reamur(root, "Program Konversi Suhu Reamur")
    root.mainloop()