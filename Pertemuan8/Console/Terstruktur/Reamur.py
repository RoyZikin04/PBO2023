print("Konversi Suhu Reamur")

def get_celcius (suhu): 
    C = (5/4 * float(suhu))
    return C

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_kelvin(suhu): 
    K = (5/4 * float(suhu)) + 273
    return K

# Entry
suhu = input("Masukkan suhu dalam Reamur: ")

# rumus
C = get_celcius (suhu)
F = get_fahrenheit (suhu)
K = get_kelvin (suhu)

# Output
print(suhu, "Reamur sama dengan")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")