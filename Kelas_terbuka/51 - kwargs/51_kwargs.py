import os
os.system("cls")
          
def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup",170,60)

def fungsi(**kwargs):
  nama = kwargs["nama"]
  tinggi = kwargs["tinggi"]
  berat = kwargs["berat"]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="Ucup",tinggi=183,berat=79)

def math(*args,**kwargs):
  output = 0
  if kwargs["option"] == "tambah":
    for angka in args:
      output += angka
  elif kwargs["option"] == "kali":
    output = 1
    for angka in args:
      output *= angka
  else:
    print("tidak ada operasi")
  return output

hasil = math(1,2,3,4,option="tambah")
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="")
print(f"hasil jumlah {hasil}")

  

