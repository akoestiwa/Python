# Input user

# data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data = ", data, ", type = ", type(data))

# jika ingin mengambil int
number_flo = float(input("Masukkan angka float: "))
print("number_flo = ", number_flo, ",type = ", type(number_flo))
number_int = int(input("Masukkan angka integer: "))
print("number_int = ", number_int, ",type = ", type(number_int))

# jika ingin mengambil boolean
biner = bool(int(input("Masukkan nilai boolean: ")))
print("biner = ", biner, ",type = ", type(biner))