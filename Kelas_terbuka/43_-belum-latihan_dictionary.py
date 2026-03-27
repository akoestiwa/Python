import datetime
import os
import string
import random

mahasiswa_template = {
  'nama':'nama',
  'nim':'00000000',
  'sks_lulus':0,
  'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
  os.system("cls")

  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'DATA MAHASISWA':^20}")
  print("-"*20)

  mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # mengisi keys
  
  mahasiswa['nama'] = input("nama: ")
  mahasiswa['nim'] = input("NIM: ")
  mahasiswa['sks_lulus'] = input("SKS: ")
  
  TAHUN_LAHIR = int(input("Tahun lahir: "))
  BULAN_LAHIR = int(input("Bulan lahir: "))
  TANGGAL_LAHIR = int(input("Tanggal lahir: "))
  
  mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

  data_mahasiswa.update({'key':mahasiswa})

  print(f"{'Kode':<6} {'Nama':<15} {'SKS':<3} {"Lahir":<8}")
  print("-"*40)

  for mahasiswa in data_mahasiswa:
    NAMA = data_mahasiswa[mahasiswa]['nama']
    SKS = data_mahasiswa[mahasiswa]['sks_lulus']
    LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")
  
    print(f"{NAMA:<15} {SKS:<3} {LAHIR:<10}" )
  
  print("\n")
  is_done = input("Sudah selesai (y/n)? ")
  if is_done == "n":
    break
print("Done!")

  


