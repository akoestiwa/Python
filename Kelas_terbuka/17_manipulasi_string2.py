# Operator dalam bentuk string

# upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# lower case
alay = "aKu KeCe AbiEz"
print("normal = "+ alay)
alay = alay.lower()
print("lower = " + alay)

# cek lower/upper case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() = cek semua huruf
# isalnum() = cek huruf dan angka
# isdecimal() = angka saja
# isspace() = spasi, tab, newline \n
# istitle() = semua kata dimulai huruf besar
# cek komponen startswith() endswith()

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10,"x")
print("'"+tengah+"'")
tengah = "tengah".strip("x")
print("'"+tengah+"'")






