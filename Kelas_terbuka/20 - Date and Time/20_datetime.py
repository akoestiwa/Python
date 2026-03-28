# Latihan date and time

import datetime as dt

'''
hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2005,10,10)
print(tanggal)
print(f"Hari lahir saya = {tanggal:%A}")
'''

print("Silakan masukkkan tanggal, bulan, tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda \t: {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini \t\t: {hari_ini}")

hari = hari_ini - tanggal_lahir
umur_tahun = hari.days // 365
umur_bulan = (hari.days % 365) // 30 
umur_hari = (hari.days % 365) % 30

print(f"Anda lahir hari : {tanggal_lahir:%A}")
print(f"Umur sekarang : {umur_tahun} tahun {umur_bulan} bulan {umur_hari} hari")