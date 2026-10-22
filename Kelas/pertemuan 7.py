# def luas_persegi_panjang(): # tanpa parameter
#     luas = 3 * 5
#     return luas

# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi(sisi): # dengan parameter
#     luas = sisi * sisi
#     return luas

# #Kita panggil fungsinya lalu argumen kita adalah angka 7
# print("Luas persegi:", luas_persegi(7))
# print("Luas persegi:", luas_persegi(10))
# print("Luas persegi:", luas_persegi(15))



# ===== 4. prosedur bisa buat menampilkan menu =====
#Tanpa parameter
# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")

# #Pemanggilan Prosedur
# pengumuman()

# #Dengan parameter
# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")

# #Pemanggilan Prosedur
# sapa_pengguna("Citra")


# ===== 5. variabel global =====
#Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"
# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# #Mengakses variabel lokal
# data()
# #Mengakses variabel global
# print("Nama:", nama)
# print("Prodi:", prodi)

# ===== 6. fungsi rekrusif =====
# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
# #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

# buku = []

# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#         for indeks in range(len(buku)):
#             print(indeks, "|", buku[indeks])

# lihat_buku()

# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")


# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     menu = input("PILIH MENU > ")
#     print("\n")

#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")

# while True:
#         tampilkan_menu()



# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')


# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(f'Angka yang kamu input : {angka}')
# finally:
#     print('Blok Try Selesai')

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as coba:
#     print(coba)

