# Latihan logika dan komparasi
'''
# Gabungan
inputdata = float(input("Masukkan angka < 3 atau > 10 : "))
isKurangDari = (inputdata < 3)
isLebihDari = (inputdata > 10)
isBenar = (isKurangDari or isLebihDari)
print("apakah benar?",isBenar)

# Irisan
inputdata = float(input("Masukkan 3 < angka < 10  : "))
isLebihDari = (inputdata > 3)
isKurangDari = (inputdata < 10)
isBenar = (isKurangDari and isLebihDari)
print("apakah benar?",isBenar)
'''

# PR
inputdata = float(input("Masukkan angka lebih dari 0 dan kurang dari 5, atau lebih dari 8 dan kurang dari 11 : "))
isLebihDari1 = (inputdata > 0)
isKurangDari1 = (inputdata < 5)
isLebihDari2 = (inputdata > 8)
isKurangDari2 = (inputdata < 11)
isBenar = (isLebihDari1 and isKurangDari1) or (isLebihDari2 and isKurangDari2)
print("apakah benar?",isBenar)

inputdata = float(input("Masukkan angka kurang dari 0, atau lebih dari 5 dan kurang dari 8, atau lebih dari 11 : "))
isKurangDari1 = (inputdata < 0)
isLebihDari1= (inputdata > 5)
isKurangDari2 = (inputdata < 8)
isLebihDari2 = (inputdata > 11)
isBenar = (isKurangDari1) or (isLebihDari1 and isKurangDari2) or (isLebihDari2)
print("apakah benar?",isBenar)