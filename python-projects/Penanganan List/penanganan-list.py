list = []

while True:
    print("--Program List Python--")
    print("1. Insert")
    print("2. Remove")
    print("3. Clear")
    print("4. Append")
    print("5. Pop")
    print("6. Reverse")
    print("7. Sort")
    print("8. Exit")
    print("List:", list,"\n")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        index = int(input("Masukkan index: "))
        value = input("Masukkan value: ")
        list.insert(index,value)
    elif pilihan == '2':
        value = input("Masukkan value: ")
        if value in list:
            list.remove(value)
    elif pilihan == '3':
        list.clear()
    elif pilihan == '4':
        value = input("Masukkan value: ")
        list.append(value)
    elif pilihan == '5':
        index = input("Masukkan index: ")
        list.pop(index)
    elif pilihan == '6':
        list.reverse()
    elif pilihan == '7':
        list.sort()
    elif pilihan == '8':
        break
    
    print("")