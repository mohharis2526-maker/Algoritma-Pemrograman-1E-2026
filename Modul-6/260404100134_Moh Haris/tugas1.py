daftar_anggota = []

while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar_anggota.append(nama)

print("HASIL EVALUASI PENDAFTARAN:")
for anggota in daftar_anggota:
    if anggota == "admin" or len(anggota) < 4:
        print(anggota, "-> Nama tidak valid")
    else:
        print(anggota, "-> Nama valid")

penyusup = input("Masukkan nama penyusup yang ingin dihapus: ")

if penyusup in daftar_anggota:
    daftar_anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus dari sistem.")
else:
    print("Nama", penyusup, "tidak ditemukan di dalam daftar pendaftaran.")

print("Daftar anggota akhir:", daftar_anggota)
