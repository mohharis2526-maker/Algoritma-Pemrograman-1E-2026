jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

total_nilai = 0
nilai_tertinggi = -1
nama_tertinggi = ""
nilai_terendah = 101
nama_terendah = ""

for i in range(1, 11):
    print("Data Mahasiswa ke-", i)
    nama = input("Masukkan Nama        : ")
    tugas = float(input("Masukkan Nilai Tugas : "))
    uts = float(input("Masukkan Nilai UTS   : "))
    uas = float(input("Masukkan Nilai UAS   : "))

    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a = jumlah_a + 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_b = jumlah_b + 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c = jumlah_c + 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d = jumlah_d + 1
    else:
        kategori = "E"
        jumlah_e = jumlah_e + 1

    print("Nama         :", nama)
    print("Nilai Tugas  :", tugas)
    print("Nilai UTS    :", uts)
    print("Nilai UAS    :", uas)
    print("Nilai Akhir  :", nilai_akhir)
    print("Kategori     :", kategori)

    total_nilai = total_nilai + nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

rata_rata = total_nilai / 10
print("REKAPITULASI NILAI KELAS")
print("Jumlah Kategori A :", jumlah_a)
print("Jumlah Kategori B :", jumlah_b)
print("Jumlah Kategori C :", jumlah_c)
print("Jumlah Kategori D :", jumlah_d)
print("Jumlah Kategori E :", jumlah_e)
print("Nilai Tertinggi   :", nilai_tertinggi, "(", nama_tertinggi, ")")
print("Nilai Terendah    :", nilai_terendah, "(", nama_terendah, ")")
print("Rata-rata Kelas   :", rata_rata)
