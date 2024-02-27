
# filename : FrmBioskop.py
import tkinter as tk
from db import DBConnection as mydb
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Bioskop import Bioskop
# from FrmFilm import FormFilm
class FormBioskop:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("550x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.CboFILM = None
        self.update_main_window = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        


         # int 
        Label(mainFrame, text='Nomor Kursi:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO_KURSI
        self.txtNO_KURSI = Entry(mainFrame) 
        self.txtNO_KURSI.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO_KURSI.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='HARI :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
    
        self.txtHARI = StringVar()
        CboHARI = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtHARI) 
        CboHARI.grid(row=1, column=1, padx=5, pady=5)
        

        # Adding combobox drop down list
        CboHARI['values'] = ('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu')
        CboHARI.current()
        
         # enum 
        Label(mainFrame, text='FILM :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtFILM = StringVar()
        CboFILM = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtFILM) 
        CboFILM.grid(row=2, column=1, padx=5, pady=5)
        self.CboFILM = CboFILM 

         # int 
        Label(mainFrame, text='HARGA :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox HARGA
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=3, column=1, padx=5, pady=5)              


        def updateFilmByHari():
            hari_terpilih = self.txtHARI.get()
            if hari_terpilih in ['Senin']:
                self.txtFILM.set("Film Senin")
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Senin'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.CboFILM['values'] = film_values
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 25000)
            elif hari_terpilih in ['Selasa']:
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Selasa'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.CboFILM['values'] = film_values
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 25000)
            elif hari_terpilih in ['Rabu']:
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Rabu'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.CboFILM['values'] = film_values
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 25000)
            elif hari_terpilih in ['Kamis']:
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Kamis'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.CboFILM['values'] = film_values
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 25000)
            elif hari_terpilih in ['Jumat']:
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Jumat'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.CboFILM['values'] = film_values
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 25000)
            elif hari_terpilih in ['Sabtu']:
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Sabtu'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 35000)
                self.CboFILM['values'] = film_values
            elif hari_terpilih in ['Minggu']:
                self.txtFILM.set("Film Minggu")
                db = mydb()
                films = db.findAll("SELECT film FROM film WHERE hari = 'Minggu'")
                film_values = [film[0] for film in films]
                self.txtFILM.set(film_values[0])
                self.txtHARGA.delete (0,END)
                self.txtHARGA.insert(0, 35000)
                self.CboFILM['values'] = film_values
                


        updateFilmByHari()  # Panggil fungsi pertama kali untuk menginisialisasi nilai film berdasarkan hari yang dipilih

        CboHARI.bind("<<ComboboxSelected>>", lambda event: updateFilmByHari())  


    
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','no_kursi','hari','film','harga')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('no_kursi', text='no_kursi')
        self.tree.column('no_kursi', width="60")
        self.tree.heading('hari', text='hari')
        self.tree.column('hari', width="100")
        self.tree.heading('film', text='film')
        self.tree.column('film', width="200")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="75")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()


    
    def onClear(self, event=None):
        self.txtNO_KURSI.delete(0,END)
        self.txtNO_KURSI.insert(END,"")
                                
        self.txtHARI.set("")
            
        self.txtFILM.set("")
            
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data bioskop
        obj = Bioskop()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        no_kursi = self.txtNO_KURSI.get()
        obj = Bioskop()
        res = obj.getByNO_KURSI(no_kursi)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        no_kursi = self.txtNO_KURSI.get()
        obj = Bioskop()
        res = obj.getByNO_KURSI(no_kursi)
            
        self.txtHARI.set(obj.hari)
            
        self.txtFILM.set(obj.film)
            
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        no_kursi = self.txtNO_KURSI.get()
        hari = self.txtHARI.get()
        film = self.txtFILM.get()
        harga = self.txtHARGA.get()       
        obj = Bioskop()
        obj.no_kursi = no_kursi
        obj.hari = hari
        obj.film = film
        obj.harga = harga
        if(self.ditemukan==True):
            res = obj.updateByNO_KURSI(no_kursi)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        no_kursi = self.txtNO_KURSI.get()
        obj = Bioskop()
        obj.no_kursi = no_kursi
        if(self.ditemukan==True):
            res = obj.deleteByNO_KURSI(no_kursi)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasia
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi_bioskop = FormBioskop(root, "Aplikasi Data Bioskop")
    root.mainloop()
