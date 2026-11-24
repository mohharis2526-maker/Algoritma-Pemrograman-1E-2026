def cek_kelayakan(status, ram):
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris_pc = []
jumlah = int(input("Masukkan jumlah PC yang akan didata: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)
    nama_pc = input("Masukkan Nama PC          : ")
    status = input("Masukkan Status (Normal/Rusak) : ")
    ram = int(input("Masukkan Kapasitas RAM (GB)    : "))
    
    inventaris_pc.append([nama_pc, status, ram])

print("HASIL EVALUASI INVENTARIS PC:")
for pc in inventaris_pc:
    hasil = cek_kelayakan(pc[1], pc[2])
    print("Nama PC:", pc[0], "| Status:", pc[1], "| RAM:", pc[2], "GB ->", hasil)
