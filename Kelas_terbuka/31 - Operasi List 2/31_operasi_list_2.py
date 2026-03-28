data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = {data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")


# ambil index data
data = ["Ucup","Otong","Dudung","Ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
print(f"index si Dudung = {index_dudung}")

# mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

