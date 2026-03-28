## List

# kumpulan data angka
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)

## alternatif list
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# list dengan loop
list_for = [i**2 for i in range(0,10)]
print(list_for)

# list dengan if
list_if = [i for i in range(0,10) if i != 5]
print(list_if)

list_if = [i for i in range(0,10) if i%2 == 0]
print(list_if)

list_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_if)






