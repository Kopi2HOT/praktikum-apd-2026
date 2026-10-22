import os

# data resonator
Resonator = ("jiyan", "yinlin", "jinshi", "changli", "zhezi", "xiangliyao", "shorekeeper", "camellya",
            "carlotta", "roccia", "phoebe", "brant", "cantarella", "zani", "ciaccona", "cartethyia", "lupa", "phrolova",
            "augusta", "iuno", "galbrena", "qiuyuan", "chisa", "lynae", "mornye", "aemeath", "luuk herssen", "sigrika", 
            "hiyuki", "denia", "lucy", "rebecca", "lucilla", "yangyang: xuangling", "suisui", "qingxiao", "jingran", "hsin",
            "suoming")

# Data pengguna menggunakan Dictionary 
dict_pengguna = {
    "rahmat": {"password": "rahmat029", "role": "Admin"},
    "mat": {"password": "mat029", "role": "User"}
}

# Data build resonator menggunakan Dictionary
data_build = { 
    1: {"nama": "Hsin", "role": "DPS", "level": 90, "hp": 20000, "atk": 2500, "def": 1100, "crit_rate": 70.0, "crit_dmg": 255.0, "energy_regen": 130.0, "skor": 650.0, "penilaian": "[GOD Build] Build impian yang sangat sempurna!"},
    2: {"nama": "Shorekeeper", "role": "Support", "level": 80, "hp": 15000, "atk": 1200, "def": 1300, "crit_rate": 15.0, "crit_dmg": 150.0, "energy_regen": 240.0, "skor": 445.0, "penilaian": "[Epic Build] Build sudah sangat layak pakai!"},
    3: {"nama": "Iuno", "role": "Sub-DPS", "level": 75, "hp": 13000, "atk": 1800, "def": 900, "crit_rate": 40.0, "crit_dmg": 160.0, "energy_regen": 110.0, "skor": 340.0, "penilaian": "[Mid Build] Build standar, masih bisa ditingkatkan."}
}
id_counter = 4 

# tampilan menu utama
menu_utama = True

while menu_utama:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 60)
    print("     SISTEM MANEJEMEN BUILD RESONATOR WUTHERING WAVES    ")
    print("=" * 60)
    print("1. Login Akun")
    print("2. Registrasi Akun")
    print("3. Exit")
    print("=" * 60)
    pilihan = input("Masukkan pilihan (1/2/3): ")

    while pilihan not in ("1", "2", "3"):
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")
        pilihan = input("Masukkan pilihan (1/2/3): ")

    # Registrasi Akun
    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("     REGISTRASI AKUN BARU     ")
        print("=" * 60)
        username_baru = input("Masukkan username: ")

        if username_baru in dict_pengguna:
            print("[GAGAL] Username tersebut sudah terpakai. Silahkan gunakan nama lain.")
        else:
            password_baru = input("Masukkan password: ")
            dict_pengguna[username_baru] = {"password": password_baru, "role": "User"}
            print("[BERHASIL] Akun berhasil didaftarkan. Silahkan login untuk melanjutkan.")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("     LOGIN AKUN     ")
        print("=" * 60)
        username_login = input("Masukkan username: ")
        password_login = input("Masukkan password: ")

        role_pengguna = ""
        login_berhasil = False

        if username_login in dict_pengguna:
            if dict_pengguna[username_login]["password"] == password_login:
                login_berhasil = True
                role_pengguna = dict_pengguna[username_login]["role"]

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
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=" * 60)
                    print(f"     [MENU ADMIN: {username_login}]     ")
                    print("=" * 60)
                    print("1. Tambah Build Resonator (Create)")
                    print("2. Tampilkan Daftar Resonator (Read)")
                    print("3. Perbarui Build Resonator (Update)")
                    print("4. Hapus Build Resonator (Delete)")
                    print("5. Logout")
                    print("=" * 60)
                    menu_admin_pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

                    # validasi input menu admin
                    while menu_admin_pilihan not in ("1", "2", "3", "4", "5"):
                        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, 4, atau 5.")
                        menu_admin_pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

                    if menu_admin_pilihan == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("======== Tambah Build Resonator ========")

                        for urutan in range(len(Resonator)):
                            no_tampilan = urutan + 1
                            nama_resonator = Resonator[urutan]
                            print(f"{no_tampilan}. {nama_resonator}")

                        pilihan_char = input("\nPilih nomor karakter: ")

                        while not (1 <= int(pilihan_char) <= len(Resonator)):
                            print("[ERROR] Nomor tidak ada di dalam daftar!")
                            pilihan_char = input("Masukan nomor yang benar: ")

                        posisi_char = int(pilihan_char) - 1
                        nama_char = Resonator[posisi_char]

                        print(f"\nPilih Peran (Role) untuk {nama_char}:")
                        print("1. DPS")
                        print("2. Sub-DPS")
                        print("3. Support")
                        pilihan_role = input("Pilih role (1-3): ")
    
                        while pilihan_role not in ("1", "2", "3"):
                            print("[ERROR] Pilihan role tidak valid!")
                            pilihan_role = input("Pilih role (1-3): ")

                        role_char = "DPS"
                        if pilihan_role == "2":
                            role_char = "Sub-DPS"
                        elif pilihan_role == "3":
                            role_char = "Support"

                        print(f"\n===== Input Stat untuk {nama_char} ({role_char})  =====")

                        # Input Statistik angka
                        input_lvl = input("Level (1-90)         : ")
                        level_valid = False
                        while not level_valid:
                            if input_lvl == "":
                                input_lvl = input("Level tidak boleh kosong (1-90): ")
                                continue
                            cek_lvl = True
                            for angka in input_lvl:
                                if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    cek_lvl = False
                            if not cek_lvl:
                                input_lvl = input("[ERROR] Harus angka! Masukkan level (1-90): ")
                            elif not (1 <= int(input_lvl) <= 90):
                                input_lvl = input("[ERROR] Level harus antara 1 sampai 90: ")
                            else:
                                level_valid = True
                        level = int(input_lvl)

                        # Validasi HP 
                        input_hp = input("Total HP          : ")
                        hp_valid = False
                        while not hp_valid:
                            if input_hp == "":
                                input_hp = input("HP tidak boleh kosong: ")
                                continue
                            cek_hp = True
                            for angka in input_hp:
                                if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    cek_hp = False
                            if not cek_hp:
                                input_hp = input("[ERROR] HP harus berupa angka positif!: ")
                            elif int(input_hp) < 8000:
                                input_hp = input("[ERROR] HP minimal 8000!: ")
                            else:
                                hp_valid = True
                        hp = int(input_hp)

                        # Validasi input nilai ATK 
                        input_atk = input("Total ATK            : ")
                        atk_valid = False
                        while not atk_valid:
                            if input_atk == "":
                                input_atk = input("ATK tidak boleh kosong: ")
                                continue
                            cek_atk = True
                            for angka in input_atk:
                                if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    cek_atk = False
                            if not cek_atk:
                                input_atk = input("[ERROR] ATK harus bernilai valid!: ")
                            elif int(input_atk) < 1200:
                                input_atk = input("[ERROR] ATK minimal 1200!: ")
                            else:
                                atk_valid = True
                        atk = int(input_atk)

                        # Validasi input nilai DEF
                        input_def = input("Total DEF            : ")
                        def_valid = False
                        while not def_valid:
                            if input_def == "":
                                input_def = input("DEF tidak boleh kosong: ")
                                continue
                            cek_def = True
                            for angka in input_def:
                                if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    cek_def = False
                            if not cek_def:
                                input_def = input("[ERROR] DEF harus bernilai valid!: ")
                            elif int(input_def) < 800:
                                input_def = input("[ERROR] DEF minimal 800!: ")
                            else:
                                def_valid = True
                        Def = int(input_def)

                        crit_rate = float(input("Total Crit Rate (%)   : "))
                        crit_dmg = float(input("Total Crit DMG (%)    : "))
                        energy_regen = float(input("Total Energy Regen    : "))

                        # Perhitungan Build
                        crit_value = (crit_rate * 2) + crit_dmg
                        skor_build = crit_value + (atk / 20) + (Def / 30) + (energy_regen * 0.5)

                        if skor_build > 600:
                            penilaian = "[GOD Build] Build impian yang sangat sempurna!"
                        elif skor_build >= 425:
                            penilaian = "[Epic Build] Build sudah sangat layak pakai!"
                        elif skor_build >= 300:
                            penilaian = "[Mid Build] Build standar, masih bisa ditingkatkan."
                        else:
                            penilaian = "[Bad Build] Build kurang, perlu farm echo ulang!"

                        # Menyimpan ke dictionary data_build
                        data_build[id_counter] = {
                            "nama": nama_char,
                            "role": role_char,
                            "level": level,
                            "hp": hp,
                            "atk": atk,
                            "def": Def,
                            "crit_rate": crit_rate,
                            "crit_dmg": crit_dmg,
                            "energy_regen": energy_regen,
                            "skor": skor_build,
                            "penilaian": penilaian
                        }
                        id_counter += 1

                        print(f"\n[BERHASIL] Build untuk {nama_char} ({role_char}) berhasil ditambahkan!")
                        print(f"Skor Build: {skor_build:.2f} | Penilaian: {penilaian}")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        if len(data_build) == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu Tampilan Build Resonator ========")
                            print("1. Tampilkan Semua Build")
                            print("2. Filter Build Berdasarkan Role")
                            sub_menu_tampilan = input("Masukkan pilihan (1/2): ")

                            if sub_menu_tampilan == "1":
                                print("\n" + "=" * 120)
                                print(f"{'ID.':<5}{'Nama Resonator':<20}{'Role':<15}{'Level':<10}{'HP':<10}{'ATK':<10}{'DEF':<10}{'Crit Rate (%)':<15}{'Crit DMG (%)':<15}{'Energy Regen':<15}")
                                print("=" * 120)                                   
                                for id_build, detail in data_build.items():
                                    print(f"{id_build:<5}{detail['nama']:<20}{detail['role']:<15}{detail['level']:<10}{detail['hp']:<10}{detail['atk']:<10}{detail['def']:<10}{detail['crit_rate']:<15}{detail['crit_dmg']:<15}{detail['energy_regen']:<15}")
                                print("=" * 120)
                                
                            elif sub_menu_tampilan == "2":
                                filter_role = input("Masukkan role yang ingin difilter (DPS/Sub-DPS/Support): ")
                                print("\n" + "=" * 120)
                                print(f"{'ID.':<5}{'Nama Resonator':<20}{'Role':<15}{'Level':<10}{'HP':<10}{'ATK':<10}{'DEF':<10}{'Crit Rate (%)':<15}{'Crit DMG (%)':<15}{'Energy Regen':<15}")
                                print("=" * 120)
                                found = False
                                
                                for id_build, detail in data_build.items():
                                    if detail['role'].lower() == filter_role.lower():
                                        print(f"{id_build:<5}{detail['nama']:<20}{detail['role']:<15}{detail['level']:<10}{detail['hp']:<10}{detail['atk']:<10}{detail['def']:<10}{detail['crit_rate']:<15}{detail['crit_dmg']:<15}{detail['energy_regen']:<15}")
                                        found = True
                                print("=" * 120)
                                
                                if not found:
                                    print(f"[INFO] Tidak ada build dengan role '{filter_role}' yang ditemukan.")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        if len(data_build) == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu build Tersimpan ========")
                            for id_build, detail in data_build.items():
                                print(f"{id_build}. {detail['nama']} ({detail['role']})")
                            pilihan_update = input("Pilih nomor ID build yang ingin diperbarui: ")
                            
                            valid_update = False
                            while not valid_update:
                                cek_update = True
                                for angka in pilihan_update:
                                    if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                        cek_update = False
                                if not cek_update or pilihan_update == "":
                                    pilihan_update = input("[ERROR] Pilihan harus berupa angka valid!: ")
                                elif int(pilihan_update) not in data_build:
                                    pilihan_update = input("[ERROR] ID build tidak ditemukan di daftar!: ")
                                else:
                                    valid_update = True

                            id_target = int(pilihan_update)
                            target = data_build[id_target]

                            print(f"\n===== Update Build untuk {target['nama']} =====")
                            print("Tekan Enter langsung jika tidak ingin mengubah stat tertentu.")
                            
                            new_level = input(f"Level ({target['level']}): ")
                            if new_level != "":
                                target['level'] = int(new_level)

                            new_hp = input(f"Total HP ({target['hp']}): ")
                            if new_hp != "":
                                target['hp'] = int(new_hp)

                            new_atk = input(f"Total ATK ({target['atk']}): ")
                            if new_atk != "":
                                target['atk'] = int(new_atk)

                            new_def = input(f"Total DEF ({target['def']}): ")
                            if new_def != "":
                                target['def'] = int(new_def)

                            new_cr = input(f"Crit Rate (%) ({target['crit_rate']}%): ")
                            if new_cr != "":
                                target['crit_rate'] = float(new_cr)

                            new_cdm = input(f"Crit DMG (%) ({target['crit_dmg']}%): ")
                            if new_cdm != "":
                                target['crit_dmg'] = float(new_cdm)

                            new_er = input(f"Energy Regen ({target['energy_regen']}%): ")
                            if new_er != "":
                                target['energy_regen'] = float(new_er)

                            # Perhitungan ulang skor build setelah update
                            crit_value = (target['crit_rate'] * 2) + target['crit_dmg']
                            skor_baru = crit_value + (target['atk'] / 20) + (target['def'] / 30) + (target['energy_regen'] * 0.5)

                            if skor_baru > 600:
                                penilaian_baru = "[GOD Build] Build impian yang sangat sempurna!"
                            elif skor_baru >= 425:
                                penilaian_baru = "[Epic Build] Build sudah sangat layak pakai!"
                            elif skor_baru >= 300:
                                penilaian_baru = "[Mid Build] Build standar, masih bisa ditingkatkan."
                            else:
                                penilaian_baru = "[Bad Build] Build kurang, perlu farm echo ulang!"
                             
                            target['skor'] = skor_baru
                            target['penilaian'] = penilaian_baru
                            print(f"\n[BERHASIL] Build untuk {target['nama']} berhasil diperbarui!")
                            print(f"Skor Baru: {skor_baru:.2f} | Penilaian: {penilaian_baru}")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        if len(data_build) == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu Hapus Build Resonator ========")
                            for id_build, detail in data_build.items():
                                print(f"{id_build}. {detail['nama']} ({detail['role']})")
                            pilihan_hapus = input("Pilih nomor ID build yang ingin dihapus: ")
                            
                            valid_hapus = False
                            while not valid_hapus:
                                cek_hapus = True
                                for angka in pilihan_hapus:
                                    if angka not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                        cek_hapus = False
                                if not cek_hapus or pilihan_hapus == "":
                                    pilihan_hapus = input("[ERROR] Pilihan harus berupa angka valid!: ")
                                elif int(pilihan_hapus) not in data_build:
                                    pilihan_hapus = input("[ERROR] ID build tidak ditemukan di daftar!: ")
                                else:
                                    valid_hapus = True

                            id_target_hapus = int(pilihan_hapus)
                            nama_hapus = data_build[id_target_hapus]['nama']
                            
                            konfirmasi = input(f"Apakah Anda yakin ingin menghapus build untuk {nama_hapus}? (y/n): ")
                            if konfirmasi.lower() == 'y':
                                del data_build[id_target_hapus]
                                print(f"[BERHASIL] Build untuk {nama_hapus} berhasil dihapus.")
                            else:
                                print("[INFO] Penghapusan dibatalkan.")
                        input("Tekan Enter untuk kembali ke menu admin...")

                    elif menu_admin_pilihan == "5":
                        print("[INFO] Logout berhasil. Kembali ke menu utama.")
                        menu_admin = False
                        input("Tekan Enter untuk kembali ke menu utama...")

            elif role_pengguna == "User":
                user_aktif = True
                while user_aktif:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("-" * 55)
                    print(f"     [MENU USER: {username_login}]     ")
                    print("-" * 55)
                    print("1. Tampilkan Daftar Resonator (Read)")
                    print("2. Logout")
                    print("-" * 55)
                    menu_user_pilihan = input("Masukkan pilihan (1/2): ")

                    while menu_user_pilihan not in ("1", "2"):
                        print("Pilihan tidak valid. Silakan masukkan angka 1 atau 2.")
                        menu_user_pilihan = input("Masukkan pilihan (1/2): ")

                    if menu_user_pilihan == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        if len(data_build) == 0:
                            print("[INFO] Belum ada build resonator yang tersimpan.")
                        else:
                            print("======== Menu Tampilan Build Resonator ========")
                            print("1. Tampilkan Semua Build")
                            print("2. Filter Build Berdasarkan Role")
                            sub_menu_tampilan = input("Masukkan pilihan (1/2): ")

                            if sub_menu_tampilan == "1":
                                print("\n" + "=" * 100)
                                print(f"{'ID.':<5}{'Nama Resonator':<20}{'Role':<15}{'Level':<10}{'HP':<10}{'ATK':<10}{'DEF':<10}{'Crit Rate (%)':<15}{'Crit DMG (%)':<15}{'Energy Regen':<15}")
                                print("=" * 100)
                                for id_build, detail in data_build.items():
                                    print(f"{id_build:<5}{detail['nama']:<20}{detail['role']:<15}{detail['level']:<10}{detail['hp']:<10}{detail['atk']:<10}{detail['def']:<10}{detail['crit_rate']:<15}{detail['crit_dmg']:<15}{detail['energy_regen']:<15}")
                                print("=" * 100)
                            elif sub_menu_tampilan == "2":
                                filter_role = input("Masukkan role yang ingin difilter (DPS/Sub-DPS/Support): ")
                                print("\n" + "=" * 100)
                                print(f"{'No.':<5}{'Nama Resonator':<20}{'Role':<15}{'Level':<10}{'HP':<10}{'ATK':<10}{'DEF':<10}{'Crit Rate (%)':<15}{'Crit DMG (%)':<15}{'Energy Regen':<15}")
                                print("=" * 100)
                                found = False
                                for id_build, detail in data_build.items():
                                    if detail['role'].lower() == filter_role.lower():
                                        print(f"{id_build:<5}{detail['nama']:<20}{detail['role']:<15}{detail['level']:<10}{detail['hp']:<10}{detail['atk']:<10}{detail['def']:<10}{detail['crit_rate']:<15}{detail['crit_dmg']:<15}{detail['energy_regen']:<15}")
                                        found = True
                                print("=" * 100)
                                if not found:
                                    print(f"[INFO] Tidak ada build dengan role '{filter_role}' yang ditemukan.")
                        input("Tekan Enter untuk kembali ke menu user...")
                  
                    elif menu_user_pilihan == "2":
                        print("[INFO] Logout berhasil. Kembali ke menu utama.")
                        user_aktif = False
                        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("[INFO] Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        menu_utama = False