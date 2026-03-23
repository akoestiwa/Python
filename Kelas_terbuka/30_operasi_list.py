# Operasi

# index 
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index-0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir index-(-1) = {data_terakhir}")

# info jumlah data
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# menambahkan item
print(f"data sebelum ditambah = {data}")

data.insert(1,"Asep")
print(f"data sesudah ditambah = {data}")

data.append("Jajang")
print(f"data ditambah lagi = {data}")

data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan = {data}")

# merubah item
data[2] = "Michael"
print(f"data rubah = {data}")

# remove item
data.remove("Ujang")
print(f"data remove = {data}")

# remove item paling belakang
data_akhir = data.pop()
print(f"data akhir = {data}")
print(data_akhir)






