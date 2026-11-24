todo_list = {}

while True:
    print("\nMENU TO-DO LIST:")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai & Belum")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo_list:
            print("Tugas tersebut sudah ada di dalam daftar.")
        else:
            todo_list[tugas] = "Belum Selesai"
            print("Tugas berhasil ditambahkan.")

    elif pilihan == "2":
        if len(todo_list) == 0:
            print("Daftar tugas masih kosong.")
        else:
            print("DAFTAR SEMUA TUGAS:")
            for tugas, status in todo_list.items():
                print("-", tugas, ":", status)

    elif pilihan == "3":
        tugas = input("Masukkan nama tugas yang sudah selesai: ")
        try:
            cek = todo_list[tugas]
            todo_list[tugas] = "Selesai"
            print("Tugas", tugas, "ditandai sebagai Selesai.")
        except KeyError:
            print("Tugas tidak ditemukan di dalam daftar!")

    elif pilihan == "4":
        tugas = input("Masukkan nama tugas yang ingin dihapus: ")
        try:
            del todo_list[tugas]
            print("Tugas", tugas, "berhasil dihapus.")
        except KeyError:
            print("Tugas tidak ditemukan, gagal menghapus!")

    elif pilihan == "5":
        selesai = 0
        belum = 0
        for status in todo_list.values():
            if status == "Selesai":
                selesai = selesai + 1
            else:
                belum = belum + 1
        print("Jumlah tugas Selesai       :", selesai)
        print("Jumlah tugas Belum Selesai :", belum)

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan masukkan angka 1 sampai 6.")
