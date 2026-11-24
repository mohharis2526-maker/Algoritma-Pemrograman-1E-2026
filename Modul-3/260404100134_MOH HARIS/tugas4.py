kuota_penuh = 0

for i in range(1, 11):
    print("Data Mahasiswa ke-", i)
    nama = input("Masukkan Nama : ")
    ipk = float(input("Masukkan IPK : "))

    
    if ipk < 3.00:
        print("Hasil Seleksi :", nama, "tidak memenuhi syarat (IPK < 3.00)")
        continue

    penghasilan = int(input("Masukkan Penghasilan Orang Tua : "))


    if penghasilan <= 3000000:
        print("Hasil Seleksi :", nama, "mendapatkan Beasiswa Penuh")
        kuota_penuh = kuota_penuh + 1
    elif penghasilan <= 5000000:
        print("Hasil Seleksi :", nama, "mendapatkan Beasiswa Sebagian")
    else:
        print("Hasil Seleksi :", nama, "tidak mendapatkan beasiswa")


    if kuota_penuh == 3:
        print("Kuota beasiswa penuh (3 mahasiswa) telah terpenuhi. Proses seleksi dihentikan.")
        break
