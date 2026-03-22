a = 9
b = 5

# OR
c = a | b
print('nilai :',a,', biner :',format(a,'08b'))
print('nilai :',b,', biner :',format(b,'08b'))
print('============================== |')
print('nilai :',c,', biner :',format(c,'08b'))

print('\n')

# AND
c = a & b
print('nilai :',a,', biner :',format(a,'08b'))
print('nilai :',b,', biner :',format(b,'08b'))
print('============================== &')
print('nilai :',c,', biner :',format(c,'08b'))

print('\n')

# XOR
c = a ^ b
print('nilai :',a,', biner :',format(a,'08b'))
print('nilai :',b,', biner :',format(b,'08b'))
print('============================== ^')
print('nilai :',c,', biner :',format(c,'08b'))

print('\n')

# NOT
c = ~a 
print('nilai :',a,', biner :',format(a,'08b'))
print('============================== ~')
print('nilai :',c,', biner :',format(c,'08b'))

print('\n')

# SHIFTING
c = a >> 2 
print('nilai :',a,', biner :',format(a,'08b'))
print('============================== >> 2')
print('nilai :',c,', biner :',format(c,'08b'))

print('\n')

d = b << 2
print('nilai :',b,', biner :',format(b,'08b'))
print('============================== << 2')
print('nilai :',d,', biner :',format(d,'08b'))