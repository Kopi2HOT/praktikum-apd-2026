# angka = 11 

# if angka < 10:
#     print("Angka kurang dari 10")


# umur = int(input("Masukkan umur anda: "))
# if umur >= 17:
#     print("kamu sudah bisa membuat KTP")
# else:
#     print("kamu belum bisa membuat KTP")


# kendaraan = input("Masukkan jenis kendaraan (mobil/motor/lainnya): ")
# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# if yang didalam if
# nilai = int(input("Masukan nilai: "))

# if nilai >= 10:
#     if nilai >= 20:
#         if nilai >= 30:
#             print("Angka besar") 
#         print("Angka sedang")
#     print("Angka kecil") 



# usia = int(input("Masukkan umur anda: "))
# keterangan = "Anda boleh masuk" if usia >= 16 else "Anda tidak boleh masuk"

# print(keterangan)

total_pembelian = int(input("Masukkan total pembelian: "))

if total_pembelian >= 200000:
    diskon = total_pembelian * 0.3
    print("total pembelian anda adalah", total_pembelian)
elif total_pembelian >= 100000:
    diskon = total_pembelian * 0.1
    print("total pembelian anda adalah", total_pembelian)
else:
    diskon = 0
    print("total pembelian anda adalah", total_pembelian)