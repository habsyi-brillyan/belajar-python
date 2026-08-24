# membuat sistem pengecekan angka dibawah 5 dan diatas 10

print('\n===== Pengecekan Angka =====\n')
# input dari user
inputUser = float(input('Masukkan angka di bawah 5 atau diatas 10 = '))

# pengecekan angka dibawah 5
kurangDari = inputUser < 5
print('Hasil dari angka yang anda masukkan :',kurangDari)

# pengecekan angka diatas 10
lebihDari = inputUser > 10
print('Hasil dari angka yang anda masukkan :', lebihDari)

# menggabungkan dengan operator logika
jikaBenar = lebihDari or kurangDari
print('\n>> Kesimpulan dari angka yang anda masukkan adalah', jikaBenar)

print('\n===== Pengecekan angka =====\n')
inputUser2 = float(input('Masukkan angka di atas 3 dan di bawah 9 = '))

lebihDari3 = inputUser2 > 3
print('Hasil dari angka yang anda masukkan :', lebihDari3)

kurangDari9 = inputUser2 < 9
print('Hasil dari angka yang anda masukkan :', kurangDari9)

isCorrect = lebihDari3 and kurangDari9
print('\n>> Kesimpulan dari angka yang anda masukkan adalah', isCorrect, '\n')