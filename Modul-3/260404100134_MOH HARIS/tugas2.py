n = int(input("Masukkan n (2-15): "))

while n < 2 or n > 15:
    print("n tidak valid, ulangi!")
    n = int(input("Masukkan n (2-15): "))

for k in range(1, 2 * n):
    if k <= n:
        i = k
    else:
        i = 2 * n - k

    baris = " " * (n - i)

    for j in range(1, i + 1):
        baris += str(j % 10)
    for j in range(i - 1, 0, -1):
        baris += str(j % 10)

    print(baris)
