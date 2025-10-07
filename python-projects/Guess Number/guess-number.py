import random

while True:
    randNumber = random.randint(1,10)

    print("--Program Tebak Angka--")
    pilihan = int(input("Masukkan angka (1-10): "))

    if pilihan == randNumber:
        print("Anda berhasil menebak angkanya!\n")
    else:
        print("Anda gagal menebak angkanya!")
        print("Angka:",randNumber,"\n")