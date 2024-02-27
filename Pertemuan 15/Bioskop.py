	# filename : Bioskop.py
from db import DBConnection as mydb
class Bioskop:
    def __init__(self):
        self.__id=None
        self.__no_kursi=None
        self.__hari=None
        self.__film=None
        self.__harga=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def no_kursi(self):
        return self.__no_kursi
        
    @no_kursi.setter
    def no_kursi(self, value):
        self.__no_kursi = value
    @property
    def hari(self):
        return self.__hari
        
    @hari.setter
    def hari(self, value):
        self.__hari = value
    @property
    def film(self):
        return self.__film
        
    @film.setter
    def film(self, value):
        self.__film = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__no_kursi,self.__hari,self.__film,self.__harga)
        sql="INSERT INTO bioskop (no_kursi,hari,film,harga) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__no_kursi,self.__hari,self.__film,self.__harga, id)
        sql="UPDATE bioskop SET no_kursi = %s,hari = %s,film = %s,harga = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNO_KURSI(self, no_kursi):
        self.conn = mydb()
        val = (self.__hari,self.__film,self.__harga, no_kursi)
        sql="UPDATE bioskop SET hari = %s,film = %s,harga = %s WHERE no_kursi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM bioskop WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNO_KURSI(self, no_kursi):
        self.conn = mydb()
        sql="DELETE FROM bioskop WHERE no_kursi='" + str(no_kursi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM bioskop WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__no_kursi = self.result[1]
        self.__hari = self.result[2]
        self.__film = self.result[3]
        self.__harga = self.result[4]
        self.conn.disconnect
        return self.result
    def getByNO_KURSI(self, no_kursi):
        a=str(no_kursi)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM bioskop WHERE no_kursi='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__no_kursi = self.result[1]
           self.__hari = self.result[2]
           self.__film = self.result[3]
           self.__harga = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__no_kursi = ''
           self.__hari = ''
           self.__film = ''
           self.__harga = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM bioskop"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,hari FROM bioskop"
        self.result = self.conn.findAll(sql)
        return self.result 
    
# Tampilkan Data
A = Bioskop()
B = A.getAllData()
print(B)