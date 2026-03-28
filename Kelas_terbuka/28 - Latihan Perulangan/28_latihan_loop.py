# Latihan perulangan membuat segitiga

sisi = 5

# for
count_for = 1
for i in range(sisi):
  print("*"*count_for)
  count_for += 1
print("-----")

# while
count_while = 1
while True:
  print("*"*count_while)
  count_while += 1 
  if count_while > sisi:
    break
print("-----")

# ganjil aja
count_ganjil = 1
while True:
  if (count_ganjil%2):
    print("*"*count_ganjil)
    count_ganjil += 1
  else:
    count_ganjil += 1
    continue
  if count_ganjil > sisi:
    break
print("-----")

# piramid
count_piramid = 1
spasi = int(sisi/2)

while True:
  if (count_piramid%2):
    print(" "*spasi,"+"*count_piramid)
    spasi -= 1
    count_piramid += 1
  else:
    count_piramid += 1
    continue
  if count_piramid > sisi:
    break
print("-----")

# ketupat
count = 1
spasi = sisi // 2

while count <= sisi:
  if (count%2):
    print(" "*spasi,"+"*count)
    count += 1
    spasi -= 1
  else:
    count += 1
while count > 0:
  if (count == sisi):
    continue
  if (count%2):
    print(" "*,"+"*count)
  else:
    count -= 1


