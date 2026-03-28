import os

os.system("cls")

def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup",170,40)

def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Dudung",120,120])

def tambah(*data):
  output = 0
  for angka in data:
    output += angka
  return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

