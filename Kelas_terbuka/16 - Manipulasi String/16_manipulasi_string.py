# Manipulasi String

# menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# operator untuk string
d = "D"
status = d in nama_lengkap # kalau gak ada pake 'not in'
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("aowk"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil/besar di ascii
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))