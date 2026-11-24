baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for i in range(1, baris + 1):
    print(" Pemeriksaan Baris ke-", i,)
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print("Lampu nomor", j, ": Mengalami gangguan")
        else:
            print("Lampu nomor", j, ": Berfungsi normal")

print("Seluruh lampu telah diperiksa. Silakan periksa sumber listrik utama taman.")
