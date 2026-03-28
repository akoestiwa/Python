# Operasi komparasi
# <, >, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari
hasil = a > b
print(a,'>',b,'=',hasil)

# kurang dari
hasil = a < b
print(a,'<',b,'=',hasil)

# lebih dari sama dengan
hasil = a >= b
print(a,'>=',b,'=',hasil)

# kurang dari sama dengan
hasil = a <= b
print(a,'<=',b,'=',hasil)

# sama dengan
hasil = a == b
print(a,'==',b,'=',hasil)

# tidak sama dengan
hasil = a != b
print(a,'!=',b,'=',hasil)

# komparasi object
x = 5
y = 6
print('nilai x =',x,', id =',hex(id(x)))
print('nilai x =',y,', id =',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)
hasil = x is not y
print('x is not y = ',hasil)



