print("Konversi Suhu Kelvin")

def get_celcius (suhu): 
    C = float (suhu) - 273
    return C

def get_reamur (suhu):
    R = 4/5 * (float(suhu) - 273)
    return R

def get_fahrenheit(suhu): 
    F = 9/5 * (float(suhu)- 273) + 32
    return F

# Entry
suhu = input("Masukkan suhu dalam Kelvin: ")

# rumus
C = get_celcius (suhu)
R = get_reamur (suhu)
F = get_fahrenheit (suhu)

# Output
print(suhu, "Kelvin sama dengan")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")