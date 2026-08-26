# Operasi dan manipulasi string

# Menyambung string
print('\n=== concatenate string ===')
nama_depan = 'ucok'
nama_tengah = 'bin'
nama_belakang = 'mail'
nama_lengkap = nama_depan + ' ' + nama_tengah + ' ' + nama_belakang
print('nama depan', nama_depan)
print('\nnama tengah', nama_tengah)
print('\nnama belakang', nama_belakang)
print('\nnama lengkap', nama_lengkap)

# mengetahui panjang string
print('\n=== len ===')
data = len(nama_lengkap)
print('banyak karakter dari ' + nama_lengkap + ' adalah ' + str(data)) 
# kenapa pakai tanda (+) dan variable data itu di casting dulu?
# karena kita ini sedang melakukan cocatenate (menyambung kata)
# jadi yang bisa disambungkan itu hanya string saja, sedangkan variable data itu adalah integer maka harus di casting ke string dulu

# operasi untuk string

# 1. mengecek apakah ada dan tidak ada karakter char atau string di dalam string
print('\n=== in dan not in ===')
a = 'bin'
status = a in nama_lengkap
print('apakah kata ' + a + ' ada di dalam kalimat : ' + str(status))
# variable status di casting ke string karena variable status itu menghasilkan output boolean

b = 'binti'
status = a not in nama_lengkap
print('\napakah kata ' + b + ' ada di dalam kalimat : ' + str(status))

print('\n=== pengulangan string ===')
# mengulang string
print('mengulang kata wk dengan menggunakan operator (*) 10 : ' + 'wk' * 10 )

# indexing
print('\n=== Indexing ===')
print('index ke-0 dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[0])
print('\nindex ke-1 dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[1])
print('\nindex ke-2 dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[2])
print('\nindex ke-(-1) dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[-1])
print('\nindex ke-(-2) dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[-2])
# indexing (range)
print('\nindex ke-[0:5] dari kata ' + nama_lengkap + ' adalah : ' + nama_lengkap[0:5])
print('\nindex ke-[3:7] dari kata ' + nama_lengkap + ' adalah : ' + nama_lengkap[3:7])
# indexing dengan dijeda dengan cara diincrement kan
print('\nindex ke-[0,2,4,6,8] dari kata ' + nama_lengkap + ' adalah ' + nama_lengkap[0:8:2]) #2 adalah increment 2

# item terkecil dan item terbesar
print('\n=== min dan max ===')
print('item terkecil : ' + min(nama_lengkap))
print('item terbesar : ' + max(nama_lengkap))

ascii_code = ord(" ")
print('ASCII CODE untuk spasi adalah = ' + str(ascii_code))
data = 123
print('char untuk ascii 123 adalah = ' + chr(data))

# operator dalam bentuk method
data = 'adek adek kentang'
jumlah = data.count('a')
print('huruf a dalam kalimat ' + data + ' adalah = ' + str(jumlah))