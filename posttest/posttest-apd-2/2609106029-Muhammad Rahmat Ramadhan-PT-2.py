
#Bagasi
list_bagasi = [12, 18, 7, 15, 20, 10]
bagasi_1 = list_bagasi[0]
bagasi_2 = list_bagasi[1]
bagasi_3 = list_bagasi[2]
bagasi_4 = list_bagasi[3]
bagasi_5 = list_bagasi[4]
bagasi_6 = list_bagasi[5]

#menghitung total murni dan kompensasi
total_murni = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6
biaya_kompensasi = total_murni * 0.05
total_berat_akhir = total_murni + biaya_kompensasi
total_berat_gram = total_berat_akhir * 1000

#Rata rata, bolean dan slicing
rata_rata = total_berat_akhir / len(list_bagasi)
nim = 29
bolean = nim < rata_rata
bagasi_tengah = list_bagasi[2:5]

#Output
print(" =====HASIL KALKULASI BAGASI KABIN MASKAPAI=====")
print(f"Data Seluruh Bagasi (List)  : {list_bagasi}")
print(f"Bagasi 1                    : {bagasi_1} kg")
print(f"Bagasi 2                    : {bagasi_2} kg")
print(f"Bagasi 3                    : {bagasi_3} kg")
print(f"Bagasi 4                    : {bagasi_4} kg")
print(f"Bagasi 5                    : {bagasi_5} kg")
print(f"Bagasi 6                    : {bagasi_6} kg")
print(f"Total Berat Murni           : {total_murni} kg")
print(f"Kompensasi Bahan Bakar (5%) : {biaya_kompensasi} kg")
print(f"Total Berat Akhir (kg)      : {total_berat_akhir} kg")
print(f"Total Berat Akhir (gram)    : {total_berat_gram} gram")
print(f"Rata-Rata Berat Bagasi      : {rata_rata:.2f} kg")
print(f"Bagasi Posisi Tengah        : {bagasi_tengah}")
print(f"NIM                         : {nim}")
print(f"Hasil Boolean               : {bolean}")