# Lambda function
import os
os.system("cls")

def f_kuadrat(angka):
  return angka**2
print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda kuadrat = {pangkat(5,2)}")

data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")


