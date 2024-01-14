print ("Konversi Suhu Kelvin")

# Entry
suhu = float(input("Masukan :"))

# rumus
C = suhu - 273
R = 4/5 * (suhu - 273)
F = 9/5 * (suhu - 273) + 32

# Output
print(suhu, " Kelvin sama dengan")
print(str(C) + " Celcius")
print(str(R)+ " Reamur")
print(str(F)+ " Fahrenheit")