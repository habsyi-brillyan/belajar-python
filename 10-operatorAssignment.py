# operasi assignment
print('\n===== Operator Assignment =====\n')
a = 6 # ini adalah operator assignment
print('nilai a awal =', a)
a += 6 # ini artinya adalah a = a + 6
print('nilai a += 6, maka nilai a menjadi', a)
a -= 5 # ini artinya adalah a = a - 5
print('nilai a -= 5, maka nilai a menjadi', a)
a *= 3 # ini artinya adalah a = a x 3
print('nilai a *= 3, maka nilai a menjadi', a)
a /= 7 # ini artinya adalah a = a : 7
print('nilai a /= 7, maka nilai a menjadi', a)
b = 10
print('\nnilai b awal =', b)
b //= 3
print('nilai b //= 3, maka nilai b menjadi', b)
b **= 2
print('nilai b **= 2, maka nilai b menjadi', b)

# operasi bitwise
# AND
print('\n===== Operator Bitwise =====\n')
print('=== AND ===\n')
a = True
print('nilai a =', a)
a &= True
print('nilai a &= True, maka nilai a menjadi', a)
a = False
print('nilai a =', a)
a &= True
print('nilai a &= True, maka nilai a menjadi', a)
a = False
print('nilai a =', a)
a &= False
print('nilai a &= False, maka nilai a menjadi', a)

# OR
print('\n=== OR ===\n')
a = True
print('nilai a =', a)
a |= True
print('nilai a |= True, maka nilai a menjadi', a)
a = False
print('\nnilai a =', a)
a |= True
print('nilai a |= True, maka nilai a menjadi', a)
a = False
print('\nnilai a =', a)
a |= False
print('nilai a |= False, maka nilai a menjadi', a)

# XOR
print('\n=== XOR ===\n')
a = True
print('nilai a =', a)
a ^= True
print('nilai a ^= True, maka nilai a menjadi', a)
a = False
print('\nnilai a =', a)
a ^= True
print('nilai a ^= True, maka nilai a menjadi', a)
a = False
print('\nnilai a =', a)
a ^= False
print('nilai a ^= False, maka nilai a menjadi', a)

# binary (geser kanan kiri)
print('\n=== Binary ===\n')
c = 0b00100
print('nilai c awal =', format(c, '05b'))
c >>= 2
print('nilai c >>= 2, maka nilai c menjadi', format(c, '05b'))
d = 0b000010
print('\nnilai d awal =', format(d, '06b'))
d <<= 4
print('nilai d <<= 4, maka nilai d menjadi', format(d, '06b'), '\n')