''' IMPORT STATEMENT '''

# berfungsi untuk mengenali file eksternal .py

# 1. menyambung program eksternal
import program_print
import program_ucup

# 2. import dengan data
import variable
import kucuy

# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)