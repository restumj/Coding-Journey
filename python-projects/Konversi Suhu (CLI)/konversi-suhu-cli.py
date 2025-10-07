print("--Program Konversi Suhu--")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Reamur\n")

temp = [[0,100,"Celcius"],[32,212,"Fahrenheit"],[273,373,"Kelvin"],[0,80,"Reamur"]]

tipeSuhuAwal = int(input("Masukkan tipe suhu awal: "))
suhuAwal = float(input("Masukkan suhu awal: "))
tipeSuhuTarget = int(input("Masukkan tipe suhu target: "))
suhuTarget = temp[tipeSuhuTarget-1][0]+(suhuAwal*(temp[tipeSuhuTarget-1][1]-temp[tipeSuhuTarget-1][0]))/(temp[tipeSuhuAwal-1][1]-temp[tipeSuhuAwal-1][0])

print(f"Hasil Konversi ({temp[tipeSuhuAwal-1][2]} -> {temp[tipeSuhuTarget-1][2]}): {suhuTarget:.2f}")