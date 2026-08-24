# Operasi aritmatika dasar dalam python
print("== Operasi Aritmatika Dasar dalam Python ==")
a = 10
b = 4

# penjumlahan (+)
hasil = a + b
print("hasil penjumlahan",a, "+", b, "=", hasil)

# pengurangan (-)
hasil = a - b
print("hasil pengurangan",a, "-", b, "=", hasil)

# perkalian (*)
hasil = a * b
print("hasil perkalian",a, "*", b, "=", hasil)

# pembagian (/)
hasil = a / b
print("hasil pembagian",a, "/", b, "=", hasil)

# eksponen/pangkat (**)
hasil = a ** b
print("hasil eksponen",a, "**", b, "=", hasil)

# modulus/sisa bagi (%)
hasil = a % b
print("hasil modulus",a, "%", b, "=", hasil)

# floor division/pembulatan ke bawah (//)
hasil = a // b
print("hasil floor division",a, "//", b, "=", hasil)

# urutan operasi aritmatika
# 1. tanda kurung ()
# 2. eksponen (**)
# 3. perkalian (*) dan pembagian (/) dan modulus (%) dan floor division (//)
# 4. penjumlahan (+) dan pengurangan (-)
print("\n== contoh urutan operasi aritmatika ==")
a = 10
b = 4
c = 2
hasil = a + b * c ** b / c - b // c
print("hasil urutan operasi aritmatika", a, "+", b, "*", c, "**", b, "/", c, "-", b, "//", c, "=", hasil)