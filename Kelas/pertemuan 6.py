# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.add("kuning")
# kartu.remove
# kartu.discard



# for i in kartu:
#     print(i)


# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)


# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(Biodata["Instagram"])
# print(Biodata.get("coba"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)
# for i in game.values():
#     print(i)
# for i, j in game.items():
#      print(f"{i} adalah jenis game {j}")

# game["resident evil"] = "horror" , menambahkan item baru ke dictionary
# print(game)

# game.update({"resident evil" : "horror"})
# print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# coba = game.pop("resident evil")
# print(game)
# print(coba)
# game.clear()
# print(game)
# print(len(game))

# gamebaru = game.copy()
# print(gamebaru)
# print(game)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000, 14000 
# menu = dict.fromkeys(key, value)
# print(menu)


# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("") 


data_siswa ={
    "siswa1" :{
        "nama" : "Johan",
        "kelas" : "A2",
        "nilai" : 95
    },
    "siswa2" :{
        "nama" : "Rizky",
        "kelas" : "A1",
        "nilai" : 90
    },
}
