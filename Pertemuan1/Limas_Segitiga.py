#menghitung Luas dan Volume Limas Segitiga
alas = 8
tinggi_alas = 6
tinggi_limas = 7

#rumus
luas_permukaan = 0.5 * alas * tinggi_alas + 3 * (0.5 * alas * tinggi_limas)
volume = 1/3 * 0.5 * alas * tinggi_alas * tinggi_limas

print("Luas permukaan limas segitiga adalah:", luas_permukaan)
print("Volume limas segitiga adalah:", volume)