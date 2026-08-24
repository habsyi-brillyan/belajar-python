# operasi logika atau boolean

# macam-macam operasi boolean
# not, or, and, xor

# NOT
# kebalikan dari value
print('\n=== NOT ===')
a = True
b = not a
print('data a :', a)
print('data b (not a) :', b)

# OR
# bernilai true jika ada salah satu true atau lebih
print('\n=== OR ===')
a = True
b = False
c = a or b
d = a or a
e = b or b
f = b or a
print('value =', a)
print('value =', b)
print('--------------------')
print(a, 'OR', b, '=', c)
print(b, 'OR', a, '=', f)
print(a, 'OR', a, '=', d)
print(b, 'OR', b, '=', e)

# AND
# kedua value harus true
print('\n=== AND ===')
a = True
b = False
c = a and b
d = a and a
e = b and b
f = b and a
print('value =', a)
print('value =', b)
print('--------------------')
print(a, 'AND', b, '=', c)
print(b, 'AND', a, '=', f)
print(a, 'AND', a, '=', d)
print(b, 'AND', b, '=', e)

# XOR -> menggunakan tand (^)
# akan bernilai true jika salah satu value true
print('\n=== XOR ===')
a = True
b = False
c = a ^ b
d = a ^ a
e = b ^ b
f = b ^ a
print('value =', a)
print('value =', b)
print('--------------------')
print(a, 'XOR', b, '=', c)
print(b, 'XOR', a, '=', f)
print(a, 'XOR', a, '=', d)
print(b, 'XOR', b, '=', e, '\n')