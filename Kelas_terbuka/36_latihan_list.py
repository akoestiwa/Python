# Program list buku

list_buku = []
while True:
  print("Data buku")
  judul = input("Masukkan judul buku\t: ")
  penulis = input("Masukkan nama penulis\t: ")

  buku_baru = [judul,penulis]
  list_buku.append(buku_baru)
  print(buku_baru)

  print("No.\t | Judul\t\t | Penulis")
  for index,buku in enumerate(list_buku):
    print(f"{index}\t | {buku[0]}\t\t | {buku[1]} ")      