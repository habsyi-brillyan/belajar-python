# operasi komparasi

# macam-macam operator komparasi
# A. Yang dapat berkerja pada syntax literal (bukan memori/nilai langsung)
    # 1. sama dengan (==)
    # 2. tidak sama dengan (!=)
    # 3. lebih besar dari (>)
    # 4. lebih kecil dari (<)
    # 5. lebih besar dari sama dengan (>=)
    # 6. lebih kecil dari sama dengan (<=)

# B. Berfungsi sebagai perbandingan memori/object (variable)
    # 7. identitas (is)
    # 8. bukan identitas (is not)

# setiap hasil operasi komparasi akan menghasilkan nilai boolean (True/False)

print('\n=== Operasi Komparasi ===\n')
a = input('Masukkan nilai a : ')
b = input('Masukkan nilai b : ')

print('\n>> Pengecekan hasil komparasi literal\n')
hasil = a == b
print(a, '==', b, '=', hasil)
hasil = a != b
print(a, '!=', b, '=', hasil)
hasil = a > b
print(a, '>', b, '=', hasil)
hasil = a < b
print(a, '<', b, '=', hasil)
hasil = a >= b
print(a, '>=', b, '=', hasil)
hasil = a <= b
print(a, '<=', b, '=', hasil, '\n')

print('>> Pengecekan hasil komparasi object')
a = 30 # ini adalah assignment membuat object
b = 32
print('\nnilai a = ', a)
print('nilai b = ', b)
hasil = a is b
print('\nhasil dari a is b = ', hasil, '\n')
hasil = a is not b
print('hasil dari a is not b = ', hasil, '\n')