# operasi string dalam bentuk method

# 1. untuk mengecilkan string
print('\n===== .lower() =====')
kata = 'BelajAR pYThoN'
print('\nkata awal = ' + kata)
kata = kata.lower()
print('\nkata setelah dilakukan lower = ' + kata)

# 2. untuk membesarkan string
print('\n===== .upper() =====')
kata = 'BelajAR pYThoN'
print('\nkata awal = ' + kata)
kata = kata.upper()
print('\nkata setelah dilakukan upper = ' + kata)

# 3. pengecekan string dengan menggunakan isx()

# a. .islower() --> untuk mengecek apakah string itu lower semua
print('\n===== .islower() =====')
kata = 'BELAJAR PYTHON'
print('\nkata awal = ' + kata)
kata = kata.islower()
print('\napakah kata sudah lower semua = ' + str(kata))

# b. .isupper() --> untuk mengecek apakah string itu upper semua
print('\n===== .isupper() =====')
kata = 'BELAJAR PYTHON'
print('\nkata awal = ' + kata)
kata = kata.isupper() # akan menghasilkan boolean
print('\napakah kata sudah upper semua  = ' + str(kata))

# c. .isalpha() --> untuk mengecek apakah string itu huruf semua
print('\n===== .isalpha =====')
kata = 'cac4'
print('\nkata awal = ' + kata)
isalpha = kata.isalpha()
print('\napakah kata ' + kata + ' = ' + str(isalpha))

# d. .isalnum() --> untuk mengecek apakah string itu huruf dan angka dan akan menghasilkan nilai boolean
print('\n===== .isalnum =====')
kata = 'brill123'
status = kata.isalnum()
kata2 = 'brill 123'
status2 = kata2.isalnum()
kata3 = 'brill'
status3 = kata3.isalnum()
print('\nkata 1 = ' + kata + ' = ' + str(status))
print('\nkata 1 = ' + kata2 + ' = ' + str(status2))
print('\nkata 1 = ' + kata3 + ' = ' + str(status3))

# e. .istitle() --> untuk mengecek apakah huruf di awal kata itu upper
print('\n===== .istitle =====')
kata1 = 'sAyoNAra'
status1 = kata.istitle()
kata2 = 'Sayonara'
status2 = kata2.istitle()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\napakah awal kata 1 huruf kapital = ' + str(status1))
print('\napakah awal kata 2 huruf kapital = ' + str(status2))

# f. .isdecimal() --> untuk mengecek apakah string itu angka decimal dan tidak ada spasi
print('\n===== .isdecimal =====')
kata1 = '123'
kata2 = '123a'
kata3 = '1 2 3'
status1 = kata1.isdecimal()
status2 = kata2.isdecimal()
status3 = kata3.isdecimal()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah kata 1 itu termasuk angka decima = ' + str(status1))
print('\napakah kata 2 itu termasuk angka decima = ' + str(status2))
print('\napakah kata 3 itu termasuk angka decima = ' + str(status3))

# g. .isspace() --> untuk mengecek apakah string itu hanya terdapat sapce, tab, enter
print('\n===== .isspace =====')
kata1 = 'brill cihuy'
kata2 = ' '
kata3 = ' \n'
status1 = kata1.isspace()
status2 = kata2.isspace()
status3 = kata3.isspace()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah kata 1 hanya terdapat spasi, tab, atau enter = ' + str(status1))
print('\napakah kata 2 hanya terdapat spasi, tab, atau enter = ' + str(status2))
print('\napakah kata 3 hanya terdapat spasi, tab, atau enter = ' + str(status3))

# h. .isascii() --> untuk mengecek apakah karakter dalam string termasuk karakter ascii
# karakter ascii --> a - z, A - Z, 0 - 9, spasi, !, @, #, $, dan %
print('\n===== .isascii =====')
kata1 = 'brill123'
kata2 = 'brill@gmail.com'
kata3 = 'brill 100%'
status1 = kata1.isascii()
status2 = kata2.isascii()
status3 = kata3.isascii()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah kata 1 merupakan karakter ascii = ' + str(status1))
print('\napakah kata 2 merupakan karakter ascii = ' + str(status2))
print('\napakah kata 3 merupakan karakter ascii = ' + str(status3))

# i. .isdigit() --> untuk mengecek apakah semua karakter string digit/angka semua, tidak termasuk karakter khusus (.,-,dll)
print('\n===== .isdigit =====')
kata1 = '123'
kata2 = '12.3'
kata3 = '-123'
status1 = kata1.isdigit()
status2 = kata2.isdigit()
status3 = kata3.isdigit()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah string kata 1 digit semua = ' + str(status1))
print('\napakah string kata 2 digit semua = ' + str(status2))
print('\napakah string kata 3 digit semua = ' + str(status3))

# j. .isidentifier() --> untuk mengecek apakah string bisa digunakan untuk identifier di python
print('\n===== .isidentifier =====')
nama = 'brill ahay'
fakultas = 'saintek'
status1 = nama.isidentifier()
status2 = fakultas.isidentifier()
print('\napakah kata \'brill ahay\' bisa digunakan sebagai identifier = ' + str(status1))
print('\napakah kata \'saintek\' bisa digunakan sebagai identifier = ' + str(status2))

# k. .isnumeric() --> untuk mengecek apakah semua karakter dalam string termasuk numeric
print('\n===== .isnumeric =====')
kata1 = '123'
kata2 = '20²²'
kata3 = '-123'
status1 = kata1.isnumeric()
status2 = kata2.isnumeric()
status3 = kata3.isnumeric()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah kata 1 termasuk numeric semua = ' + str(status1))
print('\napakah kata 2 termasuk numeric semua = ' + str(status2))
print('\napakah kata 3 termasuk numeric semua = ' + str(status3))

# l. .isprintable() --> untuk mengecek apakah semua karakter string bisa di-print/ditampilkan secara normal, \t, \n tidak bisa
print('\n===== .isprintable =====')
kata1 = 'Hello World'
kata2 = 'Hello \tWorld'
kata3 = 'Hello \nWorld'
status1 = kata1.isprintable()
status2 = kata2.isprintable()
status3 = kata3.isprintable()
print('\nkata 1 = ' + kata1)
print('\nkata 2 = ' + kata2)
print('\nkata 3 = ' + kata3)
print('\napakah kata 1 bisa di-print dengan normal = ' + str(status1))
print('\napakah kata 2 bisa di-print dengan normal = ' + str(status2))
print('\napakah kata 3 bisa di-print dengan normal = ' + str(status3))

# 4. mengecek komponen startswith() dan endswith()

# startswith('...') --> mengecek apakah string tersebut dimulai dengan kata tertentu
print('\n===== .startswith(\'...\') =====')
nama = 'om brill'
no_hp = '08123456789'
status = nama.startswith('om')
status2 = no_hp.startswith('08')
print('\nnama = ' + nama)
print('\nnomor hp = ' + no_hp)
print('\napakah kata ' + nama + ' dimulai dengan kata om = ' + str(status))

# .endswith('...') --> kebalikan dari startswith('...')
print('\n===== .endswith(\'...\') =====')
nama = 'om brill ganteng'
nama_file = 'word.docs'
status1 = nama.endswith('ganteng')
status1 = nama_file.endswith('.docs')
print('\nnama = ' + nama)
print('\nnama file = ' + nama_file)
print('\napakah kata ' + nama + 'diakhiri dengan kata ganteng = ' + str(status1))
print('\napakah kata ' + nama + 'diakhiri dengan kata .docs = ' + str(status2))

# 5. penggabungan beberapa string --> .join()
# pemisahan beberapa string --> .split()
print('\n===== .join() =====')
kata = ['aku', 'sayang', 'adik'] # --> ini namanya list
gabungan = ",".join(kata)
print( kata)
print('\ngabungan = ' + gabungan)

print('\n===== .split() =====')
print('gabungan = ' + gabungan)
pisah = gabungan.split(',')
print(pisah)

# 6. alokasi string .rjust() --> mepet kanan
# .ljust() --> mepet kiri
# .center() --> tengah
print('\n===== posisi string =====')
kanan = 'kanan'.rjust(30)
kiri = 'kiri'.ljust(30)
tengah = 'tengah'.center(30)
print('\n|' + kanan + '|')
print('\n|' + tengah + '|')
print('\n|' + kiri + '|')

# kebalikannya .strip()
print('\n===== .strip() =====')
tengah = 'kiri'.ljust(30)
print(kiri.strip())
print(kanan.strip())
print(tengah.strip())