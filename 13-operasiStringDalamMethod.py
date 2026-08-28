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
# d. .isalnum() --> untuk mengecek apakah string itu huruf dan angka
# e. .istitle() --> untuk mengecek apakah huruf di awal kata itu upper
# f. .isdecimal() --> untuk mengecek apakah string itu angka semua
# g. .isspace() --> untuk mengecek apakah string itu ada sapce, tab, enter 
# h. .isascii() --> 
# i. .isdigit() --> 
# j. .isidentifier() --> 
# k. .isnumeric() --> 
# l. .isprinttable() --> 
