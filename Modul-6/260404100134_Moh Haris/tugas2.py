list_asisten_awal = []
while True:
    nama = input("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    list_asisten_awal.append(nama)

asisten_awal = tuple(list_asisten_awal)

asisten_baru = input("\nMasukkan satu nama asisten tambahan: ")
asisten_akhir = asisten_awal + (asisten_baru,)

list_hari = []
print()
while True:
    hari = input("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    list_hari.append(hari)

hari_tugas = tuple(list_hari)

asisten_kecuali = input("\nMasukkan nama asisten pengecualian: ")
hari_kecuali = input("Masukkan hari pengecualian: ")

print("\nJADWAL SHIFT ASISTEN LABORATORIUM:")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == asisten_kecuali and hari == hari_kecuali:
            continue
        print(asisten, "-", hari)
