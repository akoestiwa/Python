# format string

# string
nama = "marlene"
format_str = f"hello {nama}"

print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 20000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"bilangan desimal = {angka:.2f}"
print(format_str)

# leading zero
angka = 2005.54321
format_str = f"bilangan leading zero = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
plus = +10.1234
minus = -10
format_minus = f"minus = {minus:+d}"
print(format_minus)
format_plus = f"plus = {plus:+.2f}"
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.1%}"
print(format_persen)

# operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain: bin(var), oct(var), hex(var)