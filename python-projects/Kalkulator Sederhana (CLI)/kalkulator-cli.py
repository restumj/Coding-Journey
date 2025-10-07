print("--Kalkulator Sederhana--")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian\n")

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
pilihan = int(input("Masukkan pilihan operasi: "))

if (pilihan==1):
    print(a+b)
elif (pilihan==2):
    print(a-b)
elif (pilihan==3):
    print(a*b)
elif (pilihan==4):
    print(f"{a/b:.2f}")