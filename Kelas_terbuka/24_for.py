# Perulangan (loop)

# for kondisi:
#   aksi

# dengan list
angka = [0,2,4,6,8,10]
print(angka)

for i in angka:
  print(f"i sekarang -> {i}")

print("finish!")

# dengan range
angka_range = range(5)

for i in angka_range:
  print(f"i sekarang -> {i}")

print("finish!")

angka_range_2 = range(1,10)

for i in angka_range_2:
  print(f"i sekarang -> {i}")
print("finish!")

# dengan string
data_str = "woi"

for huruf in data_str:
  print(huruf)
print("finish!")
