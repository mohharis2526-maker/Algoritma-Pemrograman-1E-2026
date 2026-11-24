def hitung_nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("HASIL PERHITUNGAN NILAI")
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)

nama_input = input("Masukkan Nama Mahasiswa : ")
tugas_input = float(input("Masukkan Nilai Tugas    : "))
uts_input = float(input("Masukkan Nilai UTS      : "))
uas_input = float(input("Masukkan Nilai UAS      : "))

hitung_nilai_mahasiswa(nama_input, tugas_input, uts_input, uas_input)
