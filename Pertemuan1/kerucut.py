#menghitung Luas dan Rumus kerucut
jari_jari = 4
tinggi = 6

#rumus
luas_permukaan = 3.14 * jari_jari * (jari_jari + ((tinggi ** 2) + (jari_jari ** 2)) ** 0.5)
volume = 1/3 * 3.14 * jari_jari ** 2 * tinggi

print("Luas permukaan kerucut adalah:", luas_permukaan)
print("Volume kerucut adalah:", volume)