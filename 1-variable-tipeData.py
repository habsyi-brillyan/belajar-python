# a adalah variable dan 100 adalah value-nya
a = 100

# menampilkan variable a
print(a)

# menampilkan tipe data dari variable a
print(type(a))
print("nilai dari variable a : ", a, "dan tipe data dari a : ", type(a))

print("===================================================")

## TIPE DATA

# tipe data integer : angka bulat (int)
data_integer = 1000000
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data float : angka desimal (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data string : kumpulan karakter (str)
data_string = "mas brill"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data boolean : biner true/false (bool)
data_boolean = True
print("data : ", data_boolean)
print("- bertipe : ", type(data_boolean))

## TIPE DATA KHUSUS

# tipe data kompleks : bilangan kompleks (complex)
data_complex = complex(2, 3)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double, c_long, c_char, c_int
data_c_double = c_double(1.9)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
