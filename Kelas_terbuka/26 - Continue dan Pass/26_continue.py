# continue, pass, break

angka = 0

while angka < 5:
  angka += 1
  print(angka)
  if angka == 3:
    pass # ini cuma perintah dummy
  if angka == 4:
    print("skip continue")
    continue
  print("-")
print("finish!")
  


