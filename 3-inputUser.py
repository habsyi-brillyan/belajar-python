print("===== Contoh =====")
data = input("Masukkan data (bebas):")

print("Data yang berhasil anda masukkan:", data)
print("Data yang anda masukkan bertipe:", type(data))

# inputan user akan selalu bertipe string
# jika ingin mengubah tipe datanya maka harus dilakukan casting tipe data
print("\n===== Contoh inputan dengan casting tipe data =====")
data = float(input("Masukkan data (berupa angka):"))

print("Data yang berhasil anda masukkan:", data)
print("Data yang anda masukkan bertipe:", type(data))