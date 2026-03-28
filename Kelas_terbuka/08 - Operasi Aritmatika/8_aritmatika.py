# Operasi aritmatika

a = 10
b = 3

# Operasi tambah
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi kurang
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi kali
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi bagi
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi eksponen
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi modulus
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi floor division (dibulatkan kebawah)
hasil = a // b
print(a,'//',b,'=',hasil)

# Prioritas operasi
'''
    1. ()
    2. eksponen **
    3. perkalian, pembagian, eksponen, mod, floor division
    4. pertambahan, pengurangan
'''
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)




