print ("Konversi Suhu Reamur")

# Entry
suhu = float(input("Masukan :"))

# rumus
C = 5/4 * suhu
F = (9/4 * suhu) + 32
K = 5/9 * suhu + 273

# Output
print(suhu, " Reamur sama dengan")
print(str(C) + " Celcius")
print(str(F)+ " Fahrenheit")
print(str(K)+ " Kelvin")