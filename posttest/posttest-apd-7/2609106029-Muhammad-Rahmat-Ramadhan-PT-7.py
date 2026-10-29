import os

resonator = (
    "jiyan", "yinlin", "jinshi", "changli", "zhezi", "xiangliyao", "shorekeeper", "camellya",
    "carlotta", "roccia", "phoebe", "brant", "cantarella", "zani", "ciaccona", "cartethyia", "lupa", "phrolova",
    "augusta", "iuno", "galbrena", "qiuyuan", "chisa", "lynae", "mornye", "aemeath", "luuk herssen", "sigrika", 
    "hiyuki", "denia", "lucy", "rebecca", "lucilla", "yangyang: xuangling", "suisui", "qingxiao", "jingran", "hsin",
    "suoming"
)

data_akun = {
    "rahmat": {"password": "rahmat029", "role": "Admin"},
    "mat": {"password": "mat029", "role": "User"}
}

daftar_build = { 
    1: {"nama": "Hsin", "role": "DPS", "level": 90, "hp": 20000, "atk": 2500, "def": 1100, "crit_rate": 70.0, "crit_dmg": 255.0, "energy_regen": 130.0, "skor": 650.0, "penilaian": "[GOD Build] Build impian yang sangat sempurna!"},
    2: {"nama": "Shorekeeper", "role": "Support", "level": 80, "hp": 15000, "atk": 1200, "def": 1300, "crit_rate": 15.0, "crit_dmg": 150.0, "energy_regen": 240.0, "skor": 445.0, "penilaian": "[Epic Build] Build sudah sangat layak pakai!"},
    3: {"nama": "Iuno", "role": "Sub-DPS", "level": 75, "hp": 13000, "atk": 1800, "def": 900, "crit_rate": 40.0, "crit_dmg": 160.0, "energy_regen": 110.0, "skor": 340.0, "penilaian": "[Mid Build] Build standar, masih bisa ditingkatkan."}
}

nomor_id = 4

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_tabel_build(tampil_data):
    if not tampil_data:
        print("[INFO] Tidak ada data build resonator yang tersimpan.")
        return
    print("\n" + "=" * 120)
    print(f"{'ID.':<5}{'Nama Resonator':<20}{'Role':<15}{'Level':<10}{'HP':<10}{'ATK':<10}{'DEF':<10}{'Crit Rate (%)':<15}{'Crit DMG (%)':<15}{'Energy Regen':<15}")
    print("=" * 120)                                   
    for id_build, detail in tampil_data.items():
        print(f"{id_build:<5}{detail['nama']:<20}{detail['role']:<15}{detail['level']:<10}{detail['hp']:<10}{detail['atk']:<10}{detail['def']:<10}{detail['crit_rate']:<15}{detail['crit_dmg']:<15}{detail['energy_regen']:<15}")
    print("=" * 120)


def hitung_jumlah_build():
    return len(daftar_build)

def info_versi():
    return "Wuthering Waves Build Management System v3.0"


def hitung_skor(crit_rate, crit_dmg, atk, Def, energy_regen):
    crit_value = (crit_rate * 2) + crit_dmg
    atk_tambahan = atk / 20
    def_tambahan = Def / 30
    er_tambahan = energy_regen * 0.5
    hasil_skor = crit_value + atk_tambahan + def_tambahan + er_tambahan
    return hasil_skor

def penilaian(skor):
    if skor > 600:
        return "[GOD Build] Build impian yang sangat sempurna!"
    elif skor >= 425:
        return "[Epic Build] Build bagus! layak pakai!"
    elif skor >= 300:
        return "[Mid Build] Build standar, masih bisa di upgrade!"
    else:
        return "[Bad Build] Build kurang, perlu farm echo lebih bagus lagi!"

def cari_id(daftar_key, target_id, indeks=0):
    if indeks >= len(daftar_key):
        return False
    if daftar_key[indeks] == target_id:
        return True
    return cari_id(daftar_key, target_id, indeks + 1)

menu_utama = True

while menu_utama:
    bersihkan_layar()
    print("=" * 60)
    print("         SISTEM MANAJEMEN BUILD RESONATOR WUTHERING WAVES        ")
    print(f"        ({info_versi()}) | Total Build: {hitung_jumlah_build()}     ")
    print("=" * 60)
    print("1. Login Akun")
    print("2. Registrasi Akun")
    print("3. Keluar")
    print("=" * 60)

    try:
        pilihan = int(input("Masukan pilihan (1/2/3): "))
    except ValueError:
        print("[ERROR] Input harus berupa angka (1, 2, atau 3)!")
        input("Tekan Enter untuk melanjutkan...")
        continue

    if pilihan == 2:
        bersihkan_layar()
        print("=" * 60)
        print("     REGISTRASI AKUN BARU     ")
        print("=" * 60)
        username_baru = input("Masukkan username: ")

        if username_baru in data_akun:
            print("[GAGAL] Username tersebut sudah terpakai. Silahkan gunakan nama lain.")
        else:
            password_baru = input("Masukkan password: ")
            data_akun[username_baru] = {"password": password_baru, "role": "User"}
            print("[BERHASIL] Akun berhasil didaftarkan. Silahkan login untuk melanjutkan.")
        input("Tekan Enter untuk kembali ke menu utama...")
    
    elif pilihan == 1:
        bersihkan_layar()
        print("=" * 60)
        print("     LOGIN AKUN     ")
        print("=" * 60)
        username_login = input("Masukkan username: ")
        password_login = input("Masukkan password: ")

        role_pengguna = ""
        login_berhasil = False

        if username_login in data_akun:
            if data_akun[username_login]["password"] == password_login:
                login_berhasil = True
                role_pengguna = data_akun[username_login]["role"]

        if not login_berhasil:
            print("[GAGAL] Username atau password salah. Silahkan coba lagi.")
            input("Tekan Enter untuk kembali ke menu utama...")
        else:
            print(f"[BERHASIL] Selamat datang, {username_login}! Anda login sebagai {role_pengguna}.")
            input("Tekan Enter untuk melanjutkan...")


            # MENU ADMIN
            if role_pengguna == "Admin":
                menu_admin = True
                while menu_admin:
                    bersihkan_layar()
                    print("=" * 60)
                    print(f"    [MENU ADMIN: {username_login}]")
                    print("=" * 60)
                    print("1. Tambah Build Resonator (Create)")
                    print("2. Tampilkan Daftar Resonator (Read)")
                    print("3. Perbarui Build Resonator (Update)")
                    print("4. Hapus Build Resonator (Delete)")
                    print("5. Logout")
                    print("=" * 60)

                    try:
                        menu_admin_pilihan = int(input("Masukkan pilihan (1-5): "))
                    except ValueError:
                        print("[ERROR] Masukan angka dari 1 sampai 5!")
                        input('Tekan Enter untuk melanjutkan...')
                        continue
                    
                    if menu_admin_pilihan == 1:
                        bersihkan_layar()
                        print("=" * 60)
                        print("         Tambah Build Resonator          ")
                        print("=" * 60)

                        for urutan in range(len(resonator)):
                            print(f"{urutan + 1}. {resonator[urutan]}")

                        try:
                            pilihan_char = int(input("\nPilih nomor karakter: "))
                            if not (1 <= pilihan_char <= len(resonator)):
                                raise ValueError
                        except ValueError:
                            print("[ERROR] Nomor karakter tidak valid!")
                            input("Tekan Enter untuk kembali...")
                            continue

                        nama_char = resonator[pilihan_char - 1]

                        print(f"\nPilih Peran (Role) untuk {nama_char}:")
                        print("1. DPS")
                        print("2. Sub-DPS")
                        print("3. Support")
                        
                        try:
                            pilihan_role = int(input("Pilih role (1-3): "))
                            if pilihan_role == 1:
                                role_char = "DPS"
                            elif pilihan_role == 2:
                                role_char = "Sub-DPS"
                            elif pilihan_role == 3:
                                role_char = "Support"
                            else:
                                raise ValueError
                        except ValueError:
                            print("[ERROR] Pilihan role tidak valid! Default ke DPS.")
                            role_char = "DPS"

                        print(f"\n===== Input Stat untuk {nama_char} ({role_char})  =====")

                        # Error Handling untuk input nilai statistik
                        try:
                            level = int(input("Level (1-90)          : "))
                            if not (1 <= level <= 90): raise ValueError
                            
                            hp = int(input("Total HP (min 8000)   : "))
                            if hp < 8000: raise ValueError
                            
                            atk = int(input("Total ATK (min 1200)  : "))
                            if atk < 1200: raise ValueError
                            
                            def_val = int(input("Total DEF (min 800)   : "))
                            if def_val < 800: raise ValueError
                            
                            crit_rate = float(input("Total Crit Rate (%)   : "))
                            crit_dmg = float(input("Total Crit DMG (%)    : "))
                            energy_regen = float(input("Total Energy Regen    : "))
                        except ValueError:
                            print("[ERROR] Input statistik tidak valid atau di luar batas ketentuan! Gagal menambahkan build.")
                            input("Tekan Enter untuk kembali ke menu admin...")
                            continue

                        # Pemanggilan Fungsi dengan Parameter
                        skor_build = hitung_skor(crit_rate, crit_dmg, atk, def_val, energy_regen)
                        hasil_penilaian = penilaian(skor_build)

                        daftar_build[nomor_id] = {
                            "nama": nama_char,
                            "role": role_char,
                            "level": level,
                            "hp": hp,
                            "atk": atk,
                            "def": def_val,
                            "crit_rate": crit_rate,
                            "crit_dmg": crit_dmg,
                            "energy_regen": energy_regen,
                            "skor": skor_build,
                            "penilaian": hasil_penilaian
                        }
                        nomor_id += 1

                        print(f"\n[BERHASIL] Build untuk {nama_char} ({role_char}) berhasil ditambahkan!")
                        print(f"Skor Build: {skor_build:.2f} | Penilaian: {hasil_penilaian}")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == 2:
                        bersihkan_layar()
                        if hitung_jumlah_build() == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu Tampilan Build Resonator ========")
                            print("1. Tampilkan Semua Build")
                            print("2. Filter Build Berdasarkan Role")
                            try:
                                sub_menu_tampilan = int(input("Masukkan pilihan (1/2): "))
                            except ValueError:
                                sub_menu_tampilan = 0

                            if sub_menu_tampilan == 1:
                                tampilkan_tabel_build(daftar_build)
                            elif sub_menu_tampilan == 2:
                                filter_role = input("Masukkan role yang ingin difilter (DPS/Sub-DPS/Support): ")
                                filtered_data = {}
                                for k, v in daftar_build.items():
                                    if v["role"].lower() == filter_role.lower():
                                        filtered_data[k] = v
                                tampilkan_tabel_build(filtered_data)
                            else:
                                print("[ERROR] Pilihan sub-menu tidak valid.")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == 3:
                        bersihkan_layar()
                        if hitung_jumlah_build() == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu Update Build Resonator ========")
                            tampilkan_tabel_build(daftar_build)
                            try:
                                id_target = int(input("Pilih nomor ID build yang ingin diperbarui: "))
                                daftar_kunci = list(daftar_build.keys())
                                
                                # Menggunakan Fungsi Rekursif untuk cek ID
                                if not cari_id(daftar_kunci, id_target):
                                    print("[ERROR] ID build tidak ditemukan!")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                            except ValueError:
                                print("[ERROR] ID harus berupa angka!")
                                input("Tekan Enter untuk kembali...")
                                continue

                            target = daftar_build[id_target]
                            print(f"\n===== Update Build untuk {target['nama']} =====")
                            print("Tekan Enter langsung jika tidak ingin mengubah suatu stat.")

                            # Simpan perubahan sementara agar data lama tidak berubah
                            # jika ada input yang salah di tengah proses.
                            try:
                                new_level = input(f"Level ({target['level']}): ")
                                level_baru = target['level'] if new_level == "" else int(new_level)
                                if not (1 <= level_baru <= 90):
                                    raise ValueError

                                new_hp = input(f"Total HP ({target['hp']}): ")
                                hp_baru = target['hp'] if new_hp == "" else int(new_hp)
                                if hp_baru < 8000:
                                    raise ValueError

                                new_atk = input(f"Total ATK ({target['atk']}): ")
                                atk_baru = target['atk'] if new_atk == "" else int(new_atk)
                                if atk_baru < 1200:
                                    raise ValueError

                                new_def = input(f"Total DEF ({target['def']}): ")
                                def_baru = target['def'] if new_def == "" else int(new_def)
                                if def_baru < 800:
                                    raise ValueError

                                new_cr = input(f"Crit Rate (%) ({target['crit_rate']}): ")
                                crit_rate_baru = target['crit_rate'] if new_cr == "" else float(new_cr)
                                if not (0 <= crit_rate_baru <= 100):
                                    raise ValueError

                                new_cdm = input(f"Crit DMG (%) ({target['crit_dmg']}): ")
                                crit_dmg_baru = target['crit_dmg'] if new_cdm == "" else float(new_cdm)
                                if crit_dmg_baru < 0:
                                    raise ValueError

                                new_er = input(f"Energy Regen ({target['energy_regen']}): ")
                                energy_regen_baru = target['energy_regen'] if new_er == "" else float(new_er)
                                if energy_regen_baru < 0:
                                    raise ValueError
                            except ValueError:
                                print("[ERROR] Input update tidak valid atau di luar batas. Data lama tetap dipertahankan.")
                                input("Tekan Enter...")
                                continue

                            # Terapkan perubahan setelah semua input valid
                            target['level'] = level_baru
                            target['hp'] = hp_baru
                            target['atk'] = atk_baru
                            target['def'] = def_baru
                            target['crit_rate'] = crit_rate_baru
                            target['crit_dmg'] = crit_dmg_baru
                            target['energy_regen'] = energy_regen_baru

                            # Hitung ulang skor & penilaian
                            skor_baru = hitung_skor(crit_rate_baru, crit_dmg_baru, atk_baru, def_baru, energy_regen_baru)
                            penilaian_baru = penilaian(skor_baru)

                            target['skor'] = skor_baru
                            target['penilaian'] = penilaian_baru
                            print(f"\n[BERHASIL] Build untuk {target['nama']} berhasil diperbarui!")
                            print(f"Skor Baru: {skor_baru:.2f} | Penilaian: {penilaian_baru}")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == 4:
                        bersihkan_layar()
                        if hitung_jumlah_build() == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("=" * 60)
                            print("     Menu Hapus Build Resonator          ")
                            print("=" * 60)
                            tampilkan_tabel_build(daftar_build)
                            try:
                                id_target_hapus = int(input("Pilih nomor ID build yang ingin dihapus: "))
                                daftar_kunci = list(daftar_build.keys())
                                
                                if not cari_id(daftar_kunci, id_target_hapus):
                                    print("[ERROR] ID build tidak ditemukan!")
                                    input("Tekan Enter...")
                                    continue

                            except ValueError:
                                print("[ERROR] ID harus berupa angka!")
                                input("Tekan Enter...")
                                continue

                            nama_hapus = daftar_build[id_target_hapus]['nama']
                            konfirmasi = input(f"Apakah Anda yakin ingin menghapus build untuk {nama_hapus}? (y/n): ")
                            if konfirmasi.lower() == 'y':
                                del daftar_build[id_target_hapus]
                                print(f"[BERHASIL] Build untuk {nama_hapus} berhasil dihapus.")
                            else:
                                print("[INFO] Penghapusan dibatalkan.")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == 5:
                        print("[INFO] Logout berhasil. Kembali ke menu utama.")
                        menu_admin = False
                        input("Tekan Enter untuk melanjutkan...")

            # MENU USER
            elif role_pengguna == "User":
                user_aktif = True
                while user_aktif:
                    bersihkan_layar()
                    print("-" * 55)
                    print(f"     [MENU USER: {username_login}]     ")
                    print("-" * 55)
                    print("1. Tampilkan Daftar Resonator (Read)")
                    print("2. Logout")
                    print("-" * 55)
                    
                    try:
                        menu_user_pilihan = int(input("Masukkan pilihan (1/2): "))
                    except ValueError:
                        print("[ERROR] Pilihan tidak valid.")
                        input("Tekan Enter...")
                        continue

                    if menu_user_pilihan == 1:
                        bersihkan_layar()
                        if hitung_jumlah_build() == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("=" * 60)
                            print("         Menu Tampilan Build Resonator       ")
                            print("=" * 60)
                            print("1. Tampilkan Semua Build")
                            print("2. Filter Build Berdasarkan Role")
                            try:
                                sub_menu_tampilan = int(input("Masukkan pilihan (1/2): "))
                            except ValueError:
                                sub_menu_tampilan = 0

                            if sub_menu_tampilan == 1:
                                tampilkan_tabel_build(daftar_build)
                            elif sub_menu_tampilan == 2:
                                filter_role = input("Masukkan role yang ingin difilter (DPS/Sub-DPS/Support): ")
                                filtered_data = {}
                                for k, v in daftar_build.items():
                                    if v["role"].lower() == filter_role.lower():
                                        filtered_data[k] = v
                                tampilkan_tabel_build(filtered_data)
                            else:
                                print("[INFO] Pilihan tidak valid.")
                        input("Tekan Enter untuk kembali ke menu user...")
                  
                    elif menu_user_pilihan == 2:
                        print("[INFO] Logout berhasil. Kembali ke menu utama.")
                        user_aktif = False
                        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == 3:
        bersihkan_layar()
        print("[INFO] Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        menu_utama = False