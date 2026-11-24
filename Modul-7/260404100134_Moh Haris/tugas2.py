playlists = {}

while True:
    print("\nMENU PENGELOLA PLAYLIST MUSIK:")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist beserta Lagunya")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist baru: ")
        if nama_playlist in playlists:
            print("Playlist tersebut sudah ada.")
        else:
            playlists[nama_playlist] = {}
            print("Playlist", nama_playlist, "berhasil dibuat.")

    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist tujuan: ")
        try:
            target_playlist = playlists[nama_playlist]
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            target_playlist[judul] = penyanyi
            print("Lagu", judul, "berhasil ditambahkan ke playlist", nama_playlist)
        except KeyError:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        if len(playlists) == 0:
            print("Belum ada playlist yang tersimpan.")
        else:
            print("DAFTAR SEMUA PLAYLIST:")
            for nama_playlist, daftar_lagu in playlists.items():
                print("Playlist:", nama_playlist)
                if len(daftar_lagu) == 0:
                    print("  (Belum ada lagu)")
                else:
                    for judul, penyanyi in daftar_lagu.items():
                        print("  -", judul, "-", penyanyi)

    elif pilihan == "4":
        cari_judul = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False
        for nama_playlist, daftar_lagu in playlists.items():
            if cari_judul in daftar_lagu:
                print("Lagu ditemukan di playlist:", nama_playlist, "| Penyanyi:", daftar_lagu[cari_judul])
                ditemukan = True
        if ditemukan == False:
            print("Lagu", cari_judul, "tidak ditemukan di playlist mana pun.")

    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")
        judul = input("Masukkan judul lagu yang ingin dihapus: ")
        try:
            del playlists[nama_playlist][judul]
            print("Lagu", judul, "berhasil dihapus dari playlist", nama_playlist)
        except KeyError:
            print("Playlist atau lagu tidak ditemukan, gagal menghapus!")

    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ")
        try:
            del playlists[nama_playlist]
            print("Playlist", nama_playlist, "berhasil dihapus.")
        except KeyError:
            print("Playlist tidak ditemukan, gagal menghapus!")

    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan masukkan angka 1 sampai 7.")
