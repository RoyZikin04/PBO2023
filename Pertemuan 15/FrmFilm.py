
# filename : FrmFilm.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Film import Film
class FormFilm:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("450x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.update_main_window = None
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # int 
        Label(mainFrame, text='NO:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO
        self.txtNO = Entry(mainFrame) 
        self.txtNO.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='HARI:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtHARI = StringVar()
        CboHARI = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtHARI) 
        CboHARI.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboHARI['values'] = ('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu')
        CboHARI.current()
        
         # varchar 
        Label(mainFrame, text='FILM:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox FILM
        self.txtFILM = Entry(mainFrame) 
        self.txtFILM.grid(row=2, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','no','hari','film')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('no', text='no')
        self.tree.column('no', width="30")
        self.tree.heading('hari', text='hari')
        self.tree.column('hari', width="100")
        self.tree.heading('film', text='film')
        self.tree.column('film', width="200")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNO.delete(0,END)
        self.txtNO.insert(END,"")
                                
        self.txtHARI.set("")
            
        self.txtFILM.delete(0,END)
        self.txtFILM.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data film
        obj = Film()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        no = self.txtNO.get()
        obj = Film()
        res = obj.getByNO(no)
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
        no = self.txtNO.get()
        obj = Film()
        res = obj.getByNO(no)
            
        self.txtHARI.set(obj.hari)
            
        self.txtFILM.delete(0,END)
        self.txtFILM.insert(END,obj.film)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        no = self.txtNO.get()
        hari = self.txtHARI.get()
        film = self.txtFILM.get()       
        obj = Film()
        obj.no = no
        obj.hari = hari
        obj.film = film
        if(self.ditemukan==True):
            res = obj.updateByNO(no)
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
        no = self.txtNO.get()
        obj = Film()
        obj.no = no
        if(self.ditemukan==True):
            res = obj.deleteByNO(no)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormFilm(root, "Aplikasi Data Film")
    root.mainloop()