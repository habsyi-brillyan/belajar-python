# cara membuat string dan karakter khusus

data = '\nIni adalah string menggunakan single quote'
print(data)
data2 = "\nIni adalah string menggunakan double quote\n"
print(data2)
print(type(data), '\n')

# dalam pemakaian string itu ada 2 model penggunaan
# 1. menggunakan single quote '...'
# 2. menggunakan double quote "..."
# 3. bisa menggunakan keduanya sekaligus

print('"Halo semuanya!", -> yang ditampilkan double quote')
print("'Halo semuanya!', -> yang ditampilkan single quote\n")

# karakter khusus (backslash)
# 1. membuat tanda (') menjadi karakter string -> ketika kita ingin menggunakan single quote
print('------------------------------------------------------')
print('Mari kita melakukan sholat jum\'at secara berjamaah')

# 2. membuat tanda (\) menjadi karakter string
print('\nC:\\User\\Habsyi')

# 3. membuat tab
print('\nini adalah ->\ttab')

# 4. membuat enter
print('\nini adalah\nenter')

# 5. membuat backspace
print('\nIni adalah \bbackspace')

# 6. membuat new line
print('\nIni adalah baris pertama.\nIni adalah baris kedua.') # -> LF (line feed) biasanya digunakan oleh OS linux, mac, unix
print('\nIni adalah baris pertama.\rIni adalah baris kedua.') # -> CR (Carriege return) biasanya digunakan oleh OS Commodore, Acorn, Lisp
print('\nIni adalah baris pertama.\n\rIni adalah baris kedua.') # -> CRLF (Carriege return line feed) biasanya digunakan oleh windows

# 7. literal string atau raw string
# raw string digunakan ketika kita ingin menampilkan string khusus ke layar komputer
print('\nIni sebelum menggunakan raw string, C:\new_folder')
print(r'Ini setelah menggunakan raw string, C:\new_folder')

# 8. multiline literal string
print('''\nnama: mas brill
prodi: sistem informasi
fakultas: sains dan teknologi
''')

# 9. menggabungkan multiline literal string dan raw string
print(r'''nama: cak brill
prodi: ilmu perikanan \new normal
url: www.cakbrill.com
''')