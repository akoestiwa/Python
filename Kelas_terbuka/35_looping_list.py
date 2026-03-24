# Looping dari list

# for loop
print("--- For loop ---")
list_angka = [4,3,2,5,6,1]

for angka in list_angka:
  print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "diding"]

for nama in peserta:
  print(f"nama = {nama}")

# for loop dan range
print("\n--- For loop dan range ---")
list_angka = [10,5,4,3,6,5]
panjang = len(list_angka)

for i in range(panjang):
  print(f"angka = {list_angka[i]}")

# while
print("\n--- While loop ---")
list_angka = [10,5,4,3,6,5]
panjang = len(list_angka)
i = 0

while i < panjang:
  print(f"angka = {list_angka[i]}")
  i += 1

#list comprehension
print("\n--- List comprehension ---")
data = ["ucup",1,2,3,"otong"]
[print(f"data = {i}") for i in data]
list_angka = [10,5,4,3,6,5]
angka_kuadrat = [i**2 for i in list_angka]
print(angka_kuadrat)

# enumerate
print("\n--- Enumerate ---")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
  print(f"index = {index}, data = {data}")
