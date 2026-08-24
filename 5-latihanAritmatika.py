print("\n=== Sistem Konversi Celcius ===\n")
# celcius
# fahrenheit
# reamur
# kelvin

celcius = float(input("Masukkan suhu dalam Celcius: "))
print("\nSuhu yang anda masukkan = ", celcius, "°C\n")

# konversi celcius ke fahrenheit
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit = ", fahrenheit, "°F")

# konversi celcius ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur = ", reamur, "°R")

# konversi celcius ke kelvin
kelvin = celcius + 273.15
print("Suhu dalam kelvin = ", kelvin, "K")

print('\n=== Konversi fahrenheit ===\n')
fahrenheit = float(input('Masukkan suhu dalam Fahrenheit: '))
print('\nSuhu yang anda masukkan = ', fahrenheit, '°F\n')

# konversi fahrenheit ke celcius
celcius = (5/9) * (fahrenheit - 32)
print('Suhu dalam Celcius = ', celcius, '°C')

# konversi fahrenheit ke reamur
reamur = (4/9) * (fahrenheit - 32)
print('Suhu dalam reamur = ', reamur, '°R')

# konversi fahrenheit ke kelvin
kelvin = (5/9) * (fahrenheit - 32) + 273.15
print('Suhu dalam kelvin = ', kelvin, 'K')

print('\n=== Konversi Kelvin ===\n')
kelvin = float(input('Masukkan suhu dalam Kelvin: '))
print('\nSuhu yang anda masukkan = ', kelvin, 'K\n')

# konversi kelvin ke celcius
celcius = kelvin - 273.15
print('Suhu dalam Celcius = ', celcius, '°C')

# konversi kelvin ke fahrenheit
fahrenheit = (9/5) * (kelvin - 273.15) + 32
print('Suhu dalam Fahrenheit = ', fahrenheit, '°F')

# konversi kelvin ke reamur
reamur = (4/5) * (kelvin - 273.15)
print('Suhu dalam reamur = ', reamur, '°R')

print('\n=== Konversi Reamur ===\n')
reamur = float(input('Masukkan suhu dalam Reamur: '))
print('\nSuhu yang anda masukkan = ', reamur, '°R\n')

# konversi reamur ke celcius
celcius = (5/4) * reamur
print('Suhu dalam Celcius = ', celcius, '°C')

# konversi reamur ke fahrenheit
fahrenheit = (9/4) * reamur + 32
print('Suhu dalam Fahrenheit = ', fahrenheit, '°F')

# konversi reamur ke kelvin
kelvin = (5/4) * reamur + 273.15
print('Suhu dalam Kelvin = ', kelvin, 'K\n')