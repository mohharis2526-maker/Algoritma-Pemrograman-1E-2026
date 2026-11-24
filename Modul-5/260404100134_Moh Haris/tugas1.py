def hitung_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2)

n = int(input("Masukkan hari ke-N (bilangan bulat positif): "))

if n <= 0:
    print("Masukkan bilangan bulat positif (lebih dari 0)!")
else:
    hasil = hitung_pelanggan(n)
    print("Jumlah pelanggan pada hari ke-", n, "adalah:", hasil, "orang")
