# Operator dictionary

data_dict = {
  "cup":"ucup surucup",
  "tong":"otong surotong",
  "dung":"dudung surudung",
}

# panjang dictionary
len_dict = len(data_dict)
print(f"panjang dictionary: {len_dict}")

# mengecek key exist atau tidak
key = "cup"
check_key = "cup" in data_dict
print(f"apakah {key} ada di data_dict: {check_key}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan"))

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)
