data = []

def tambah_data():
    print("\n=== TAMBAH DATA ===")
    id_siswa = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    siswa = {
        "id": id_siswa,
        "nama": nama,
        "kelas": kelas
    }

    data.append(siswa)
    print("✅ Data berhasil ditambahkan")


def tampil_data():
    print("\n=== DATA SISWA ===")

    if len(data) == 0:
        print("❌ Data masih kosong")
        return

    for siswa in data:
        print(
            "ID:",siswa["id"],
            "| Nama:",siswa["nama"],
            "| Kelas:",siswa["kelas"]

        )


def ubah_data():
    print("\n=== UBAH DATA ===")
    id_cari = int(input("Masukkan ID yang ingin diubah: "))

    for siswa in data:
        if siswa["id"] == id_cari:
            siswa["nama"] = input("Nama baru: ")
            siswa["kelas"] = input("Kelas baru: ")
            print("✅ Data berhasil diubah")
            return

    print("❌ Data tidak ditemukan")


def hapus_data():
    print("\n=== HAPUS DATA ===")
    id_cari = int(input("Masukkan ID yang ingin dihapus: "))

    for siswa in data:
        if siswa["id"] == id_cari:
            data.remove(siswa)
            print("✅ Data berhasil dihapus")
            return

    print("❌ Data tidak ditemukan")


while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("👋 Program selesai")
        break
    else:
        print("❌ Menu tidak valid")
