# WIdth and multiline

# data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"="+" Data String "+5*"=")
print(data_string)

# string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(5*"="+" Data String "+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""
print(5*"="+" Data String "+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama = {data_nama:>10}
umur = {data_umur:>}
tinggi = {data_tinggi:>10}
nomor sepatu = {data_nomor_sepatu:>10}
"""
print(5*"="+" Data String "+5*"=")
print(data_string)