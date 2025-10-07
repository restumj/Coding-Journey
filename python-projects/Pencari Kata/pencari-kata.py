# Program Pencari kata dalam kalimat

while True:
    kalimat = input("Masukkan kalimat: ")
    kata = input("Masukkan kata yang ingin dicari: ")

    if kalimat.find(kata):
        print(f"Kata ditemukan sebanyak {kalimat.count(kata)} kali!\n")
    else:
        print("Kata tidak ditemukan!\n")