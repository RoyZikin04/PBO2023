#ini adalah modul yang berisi fungsi dari berbagai rumus bangunan dan di pakai

#kubus
def luaskubus ( sisi ):
    lkubus = round (6 * sisi **2)
    return lkubus 

def volumekubus (sisi) :
    vkubus =  round (sisi **3)
    return vkubus

#balok
def luasbalok (panjang, tinggi, lebar) :
    lbalok = round (2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    return lbalok

def volumebalok (panjang , lebar, tinggi) : 
    vbalok = round (panjang * lebar * tinggi) 
    return vbalok

#kerucut
def luaskerucut (jari_jari, tinggi ) :
    L = round (3.14 * jari_jari * (jari_jari + ((tinggi ** 2) + (jari_jari ** 2)) ** 0.5))
    return L

def volumekerucut (jari_jari, tinggi) : 
    V = round (1/3 * 3.14 * jari_jari ** 2 * tinggi)
    return V

#limas Segiempat
def luas_limas_segiempat (sisi, tinggi) : 
    L = round (2 * sisi ** 2 + 4 * sisi * tinggi)
    return L

def volume_limas_segiempat (sisi, tinggi) :
    V = round (1/3 * sisi ** 2 * tinggi)
    return V

#limas segitiga
def luas_limas_segitiga (alas, t_alas, t_limas) :
    L = round (0.5 * alas * t_alas + 3 * (0.5 * alas * t_limas))
    return  L

def volume_limas_segitiga (alas, t_alas, t_limas) :
    V = round (1/3 * 0.5 * alas * t_alas * t_limas)
    return V

#Prisma Segitiga
def Luas_Prisma_segitiga (alas, t_alas, t_prisma) :
    L = round (2 * (0.5 * alas * t_alas + alas * t_prisma + 0.5 * alas * t_alas))
    return L

def volume_Prisma_segitiga (alas, t_alas, t_prisma) :
    V = round (0.5 * alas * t_alas * t_prisma)
    return V

#selinder
def luas_selinder (jari_jari, tinggi) :
    L = round (2 * 3.14 * jari_jari * (jari_jari + tinggi))
    return L

def volume_selinder (jari_jari, tinggi) :
    V = round (2 * 3.14 * jari_jari * (jari_jari + tinggi))
    return V

#Bola
def luas_bola (jari_jari):
    L = round (4 * 3.14 * jari_jari ** 2 )
    return L

def Volume_bola (jari_jari):
    V = round (4/3 * 3.14 * jari_jari ** 3)
    return V