import os
os.system("cls")

def say_hello(nama = "Ganteng"):
  print(f"Hello {nama}")

say_hello("Ucup")
say_hello()

def sapa_dia(nama, pesan = "Apa kabar?"):
  print(f"Hai {nama}, {pesan}")

sapa_dia("Dudung","Hai ganteng")
sapa_dia("Otong")

def hitung_pangkat(angka, pangkat=2):
  hasil = angka**pangkat
  return hasil

print(hitung_pangkat(2))
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

def fungsi(input1=1, input2=2, input3=3, input4=4):
  hasil = input1 + input2 + input3 + input4
  return hasil

print(fungsi())
print(fungsi(input3=10))


