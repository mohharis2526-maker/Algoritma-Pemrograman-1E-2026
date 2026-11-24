def cek_palindrom(kata):
    kata_balik = ""
    
    for huruf in kata:
        kata_balik = huruf + kata_balik
        
    if kata == kata_balik:
        return True
    else:
        return False

kata_input = input("Masukkan sebuah kata: ")

hasil = cek_palindrom(kata_input)

if hasil == True:
    print("Kata", kata_input, "adalah PALINDROM (True)")
else:
    print("Kata", kata_input, "BUKAN palindrom (False)")
