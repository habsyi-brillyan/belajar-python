# casting adalah merubah dari tipe data satu ke tipe data yang lain
data_int = 67
print("data = ", data_int, ", bertipe = ", type(data_int))

# casting integer
print("===== casting integer =====")
data_int = 76
print("data = ", data_int, ", bertipe = ", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan bernilai false jika data_int = 0
print("data = ", data_float, ", diubah ke tipe = ", type(data_float))
print("data = ", data_str, ", diubah ke tipe = ", type(data_str))
print("data = ", data_bool, ", diubah ke tipe = ", type(data_bool))

# casting float
print("===== casting float =====")
data_float = 7.6
print("data = ", data_float, ", bertipe = ", type(data_float))
data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan bernilai false jika data_int = 0
print("data = ", data_int, ", diubah ke tipe = ", type(data_int))
print("data = ", data_str, ", diubah ke tipe = ", type(data_str))
print("data = ", data_bool, ", diubah ke tipe = ", type(data_bool))

# casting string
print("===== casting string =====") 
data_str = "89"
print("data = ", data_str, ", bertipe = ", type(data_str))
data_float = float(data_str) # harus string angka
data_int = int(data_str) # harus string angka
data_bool = bool(data_str) # akan bernilai false jika data_str = "" atau kosong
print("data = ", data_float, ", diubah ke tipe = ", type(data_float))
print("data = ", data_int, ", diubah ke tipe = ", type(data_int))
print("data = ", data_bool, ", diubah ke tipe = ", type(data_bool))

# casting boolean
print("===== casting boolean =====") 
data_bool = True
print("data = ", data_bool, ", bertipe = ", type(data_bool))
data_float = float(data_bool)
data_int = int(data_bool)
data_str = str(data_bool) # akan diubah menjadi kata string "True" atau "False"
print("data = ", data_float, ", diubah ke tipe = ", type(data_float))
print("data = ", data_int, ", diubah ke tipe = ", type(data_int))
print("data = ", data_str, ", diubah ke tipe = ", type(data_str))