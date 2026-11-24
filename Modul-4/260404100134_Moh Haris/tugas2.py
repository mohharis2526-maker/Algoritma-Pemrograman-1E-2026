total_gaji = 0
gaji_pokok = 100000

for hari in range(1, 8):
    print("Data Kerja Hari ke-", hari)
    
    lembur = int(input("Masukkan jam lembur (1-8): "))
    
    while lembur < 0 or lembur > 8 or lembur == 5 or lembur == 7:
        if lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan dan tidak dihitung!")
        else:
            print("Jam lembur tidak sesuai ketentuan! Silakan masukkan ulang.")
        lembur = int(input("Masukkan ulang jam lembur: "))
        
    if lembur == 0:
        upah_lembur = 0
    elif lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000

    shift = input("Apakah bekerja pada shift malam? (y/t): ")
    if shift == "y":
        tunjangan_malam = 50000
    else:
        tunjangan_malam = 0

    gaji_harian = gaji_pokok + upah_lembur + tunjangan_malam
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ke-", hari, ": Rp", gaji_harian)

print("Total Gaji Mingguan Karyawan : Rp", total_gaji)
