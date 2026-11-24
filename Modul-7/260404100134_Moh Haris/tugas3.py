undangan = set()
webinar_a = set()
webinar_b = set()

jumlah_undangan = int(input("Masukkan jumlah daftar undangan: "))
for i in range(jumlah_undangan):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

jumlah_a = int(input("\nMasukkan jumlah peserta Webinar A: "))
for i in range(jumlah_a):
    nama = input("Masukkan nama peserta Webinar A: ")
    webinar_a.add(nama)

jumlah_b = int(input("\nMasukkan jumlah peserta Webinar B: "))
for i in range(jumlah_b):
    nama = input("Masukkan nama peserta Webinar B: ")
    webinar_b.add(nama)

semua_peserta = webinar_a | webinar_b
hadir_keduanya = webinar_a & webinar_b
hanya_satu_webinar = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print("\nHASIL ANALISIS KEHADIRAN WEBINAR:")
print("1. Semua peserta dari kedua webinar        :", semua_peserta)
print("2. Peserta yang hadir di keduanya          :", hadir_keduanya)
print("3. Peserta yang hanya hadir di salah satu  :", hanya_satu_webinar)
print("4. Undangan yang tidak hadir di mana pun   :", tidak_hadir)
