import os
os.system("cls")

def kuadrat(input_angka):
  output_kuadrat = input_angka**2
  return output_kuadrat

y = kuadrat(7)
print(y)

def tambah(angka1,angka2):
  return angka1 + angka2

x = tambah(8,2)
print(x)

def aritmatika(angka1,angka2):
  tambah = angka1 + angka2
  kurang = angka1 - angka2
  kali = angka1 * angka2
  bagi = angka1 / angka2
  return tambah,kurang,kali,bagi

k,l,m,n = aritmatika(3,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")
