history = [{-19000:"beli lauk"}]

while True:
    print("--Sistem Pencatatan Keuangan Sederhana--")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    print("3. Exit\n")

    print("--Riwayat--")
    for historyItem in history:
        for item in historyItem:
            print(f"{item:,}: {historyItem[item]}")
    
    saldo=0
    for historyItem in history:
        for item in historyItem:
            saldo += item
    print(f"[Saldo: {saldo:,}]")
    print()

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        pemasukan = int(input("Masukkan pemasukan: "))
        note = input("Masukkan note: ")
        history.append({pemasukan: note})
    elif pilihan == 2:
        pengeluaran = -int(input("Masukkan pengeluaran: "))
        note = input("Masukkan note: ")
        history.append({pengeluaran: note})
    else:
        break

    print()