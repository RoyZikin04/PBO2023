from tkinter import Frame, Label, Entry, Button, Tk, W, BOTH, END

class Fahrenheit:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=True) 
        Label(mainFrame, text='Fahrenheit:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        
        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=0, column=1, padx=5, pady=5)  
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5) 
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5) 
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def get_Celcius(self, suhu):
        val =(32 - float(suhu)) * 5/9
        return val
    
    def get_reamur(self, suhu):
        val = (32 - float(suhu)) * 4/9
        return val
    
    def get_kelvin(self, suhu):
        val = (32 - float(suhu)) * 5/9 + 273
        return val

    def onHitung(self):
        # Suhu dalam Fahrenheit
        suhu = self.txtFahrenheit.get()
        C = self.get_Celcius(float(suhu))
        self.txtCelcius.delete(0, END)
        self.txtCelcius.insert(END, str(C))

        # Suhu dalam Reamur
        R = self.get_reamur(float(suhu))
        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))

        # Suhu dalam Kelvin
        K = self.get_kelvin(float(suhu))
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()            

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Fahrenheit(root, "Program Konversi Suhu Fahrenheit")
    root.mainloop()