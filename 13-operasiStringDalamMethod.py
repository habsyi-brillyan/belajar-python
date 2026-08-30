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

# f. .isdecimal() --> untuk mengecek apakah string itu angka decimal
print('\n===== .isdecimal =====')
kata
# g. .isspace() --> untuk mengecek apakah string itu ada sapce, tab, enter 
# h. .isascii() --> untuk mengecek apakah
# i. .isdigit() --> untuk mengecek apahak 
# j. .isidentifier() --> untuk mengecek apakah
# k. .isnumeric() --> untuk mengecek apakah
# l. .isprintable() --> untuk mengecek apakah
