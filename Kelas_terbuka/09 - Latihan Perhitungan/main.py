''' LATIHAN PERHITUNGAN '''

'''
# celcius ke lainnya
print("\n Program Konversi Temperatur \n")

celsius = float(input('Masukkan suhu dalam ceisius = '))
print("suhu adalah ", celsius, "C")

# reamur
reamur = (4/5)*celsius
print("suhu dalam reamur adalah ", reamur, "R")

# fahrenheit
fahrenheit = ((9/5)*celsius)
print("suhu dalam reamur adalah ", fahrenheit, "F")

# kelvin
kelvin = celsius + 273
print("suhu dalam kelvin adalah ", kelvin, "K30")
'''

# kelvin ke fahrenheit dan sebaliknya
print("\n Program Konversi Kelvin Fahrenheit \n")

kelvin = float(input('Masukkan suhu dalam kelvin = '))
print("suhu adalah ", kelvin, "K")

# fahrenheit
fahrenheit = ((9/5)*kelvin)+32-273
print("suhu dalam fahrenheit adalah ", fahrenheit, "F")

fahrenheit = float(input('Masukkan suhu dalam fahrenheit = '))
print("suhu adalah ", fahrenheit, "F")

# kelvin
kelvin = (5/9)*(fahrenheit-32)+273
print("suhu dalam kelvin adalah ", kelvin, "K")