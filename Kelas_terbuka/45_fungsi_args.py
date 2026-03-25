import os
os.system("cls")

def pagi(nama):
  print(f"Selamat pagi {nama}")

pagi("Dodo")

def tambah(angka_1,angka_2):
  hasil = angka_1 + angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,2)

def say_hi(list_peserta):
  data_peserta = list_peserta.copy()
  for peserta in data_peserta:
    print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup","Dudung","Dodo"]

say_hi(anggota_boyband)
