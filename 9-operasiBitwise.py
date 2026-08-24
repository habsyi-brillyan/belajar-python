# operasi bitwise, operasi biner, binary
# operasi pada masing-masing bit
# 8 bit = 1 byte

# int -> 2 -> 00000010 -> 2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
#                      -> karena angka 1 itu berada tepat di batisan 2^1 ->  2

# syntax format(a, '08b') -> mengubah angka a menjadi string biner sepanjang 8 bit

## bitwise and (&)
print('\n===== AND =====\n')
a = 2
b = 7
print('nilai a =', a, ', binary', format(a, '08b'), '\n')
print('nilai b =', b, ', binary', format(b, '08b'))
print('------------------------------ (&)')
c = a & b
print('nilai c =', c, ', binary', format(c, '08b'))

## bitwise  or (|)
print('\n===== OR =====\n')
a = 4
b = 9
print('nilai a =', a, ', binary', format(a, '08b'), '\n')
print('nilai b =', b, ', binary', format(b, '08b'))
print('------------------------------ (|)')
c = a | b
print('nilai c =', c, ', binary', format(c, '08b'))

## bitwise not (~)
print('\n===== NOT =====\n')
a = 5
print('nilai a =', a, ', binary', format(a, '08b'))
print('------------------------------ (~)')
c = ~a
print('nilai c =', c, ', binary', format(c, '08b'))

## bitwise xor (^)
print('\n===== XOR =====\n')
a = 2
b = 7
print('nilai a =', a, ', binary', format(a, '08b'), '\n')
print('nilai b =', b, ', binary', format(b, '08b'))
print('------------------------------ (^)')
c = a ^ b
print('nilai c =', c, ', binary', format(c, '08b'), '\n')