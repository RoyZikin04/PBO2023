#menghitung luas dan volume Prisma Segitiga
alas = 6
tinggi_alas = 5
tinggi_prisma = 4

#rumus
luas_permukaan = 2 * (0.5 * alas * tinggi_alas + alas * tinggi_prisma + 0.5 * alas * tinggi_alas)
volume = 0.5 * alas * tinggi_alas * tinggi_prisma 

print("Luas permukaan prisma segitiga adalah:", luas_permukaan)
print("Volume prisma segitiga adalah:", volume)