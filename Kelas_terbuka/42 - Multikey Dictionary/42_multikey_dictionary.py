import datetime

mahasiswa1 = {
  'nama':'Ucup Surucup',
  'nim':'19022001',
  'sks_lulus':130,
  'beasiswa':False,
  'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
  'nama':'Otong Surotong',
  'nim':'19022002',
  'sks_lulus':140,
  'beasiswa':True,
  'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
  'nama':'Asep Kasyep',
  'nim':'19022003',
  'sks_lulus':100,
  'beasiswa':False,
  'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
  'MAH001':mahasiswa1,
  'MAH002':mahasiswa2,
  'MAH003':mahasiswa3,
}

print(f"{'Kode':<6} {'Nama':<15} {'SKS':<3} {"Beasiswa":<9} {"Lahir":<8}")
print("-"*40)


for mahasiswa in data_mahasiswa:
  NAMA = data_mahasiswa[mahasiswa]['nama']
  SKS = data_mahasiswa[mahasiswa]['sks_lulus']
  BEASISWA = data_mahasiswa[mahasiswa]['beasiswa']
  LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")
  
  print(mahasiswa,f"{NAMA:<15} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}" )
