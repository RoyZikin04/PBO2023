from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class Selinder :
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        #nametag
        nametag = Frame (mainFrame, bg="Green", height=50)
        nametag.grid(row=6, column=1, columnspan=1, sticky='ew', pady=10)

        nama = Label(nametag, text="Roy Zikin", bg='Green')
        nama.grid(row=6, column=1, sticky='nsew' , padx=5, pady=5)

        nametag.grid_rowconfigure(6, weight=1)
        nametag.grid_columnconfigure(1, weight=1)

        # pasang Label
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Kubus:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume :").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtjari_jari = Entry(mainFrame) 
        self.txtjari_jari.grid(row=0, column=1, padx=5, pady=5)
        self.txttinggi = Entry(mainFrame) 
        self.txttinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        jari_jari = int(self.txtjari_jari.get())
        tinggi = int(self.txttinggi.get())
        luas = round ( 4 * 3.14 * jari_jari ** 2)
        Volume = round (2 * 3.14 * jari_jari * (jari_jari + tinggi))
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(Volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Selinder(root, "Program Luas dan Volume Selinder")
    root.mainloop() 