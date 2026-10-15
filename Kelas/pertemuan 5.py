nama = ["attar", "johan","azka", ]
print(nama)

# for i in(nama):
#     print(i)

nama.append("julpa") # nambah satu list baru

print(nama)

nama.extend(["mirza", "wilie"]) # nambah lebih dari satu list
print(nama)

nama.insert(2, "mustafid") # nenyisipkan elemen di tengah list
print(nama)

nama[0:3] = ["Hafiz", "dewi", "meisya"]
print(nama)

# poin = [1, 2, 3, 4, 5, 6, 7]
# print(poin)
# poin[4:7] = [11, 12, 13]
# print(poin)

del nama[1]
print(nama)

nama.remove("julpa")
print(nama)

ambil_nama = nama.pop(1)
print(nama)
print(ambil_nama)

# poin = [1, 2, 3, 4, 5, 6, 7]
# print(poin[1:5:2]) slicing

# poin1 = [1, 2, 3, 4, 5, 6, 7]
# poin2 = [8, 9, 10]
# poin = poin1 + poin2 
# print(poin) operator penjumlahan/perkalian dll.

line_up = ["ferrari", "Leclerc", 16], # nested list

buah = ("apel", "mangga", "nanas") 
print(buah)

listbuah = list(buah)
listbuah.append("pisang")

buah = tuple(listbuah)
print(buah)


# game = ("ml", "genshin") unpack tuple
# (moba, open_world) = game
# print(moba)
# print(open_world) 



