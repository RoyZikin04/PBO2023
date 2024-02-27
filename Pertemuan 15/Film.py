
# filename : Film.py
from db import DBConnection as mydb
class Film:
    def __init__(self):
        self.__id=None
        self.__no=None
        self.__hari=None
        self.__film=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def no(self):
        return self.__no
        
    @no.setter
    def no(self, value):
        self.__no = value
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
    def simpan(self):
        self.conn = mydb()
        val = (self.__no,self.__hari,self.__film)
        sql="INSERT INTO Film (no,hari,film) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__no,self.__hari,self.__film, id)
        sql="UPDATE film SET no = %s,hari = %s,film = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNO(self, no):
        self.conn = mydb()
        val = (self.__hari,self.__film, no)
        sql="UPDATE film SET hari = %s,film = %s WHERE no=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM film WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNO(self, no):
        self.conn = mydb()
        sql="DELETE FROM film WHERE no='" + str(no) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM film WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__no = self.result[1]
        self.__hari = self.result[2]
        self.__film = self.result[3]
        self.conn.disconnect
        return self.result
    def getByNO(self, no):
        a=str(no)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM film WHERE no='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__no = self.result[1]
           self.__hari = self.result[2]
           self.__film = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__no = ''
           self.__hari = ''
           self.__film = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM film"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,hari FROM film"
        self.result = self.conn.findAll(sql)
        return self.result