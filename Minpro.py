# nama  = Rifaa Zainul Arifin (Faa)
# kelas = C
# nim   = 2509116092

target_bulanan= []   

print("=== Menu Target Bulanan ===")
print("1. Tambah target")
print("2. Updagrade progress")
print("3. Hapus target")
print("4. Keluar")

pilihan = input("Pilih menu (1-4): ")

if pilihan == "1":
    target = input("Masukkan target baru : ")
    target_bulanan.append([target, 0])
    print("Target ditambah!")
    for i in range(len(target_bulanan)):
        print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

elif pilihan == "2":
    if not target_bulanan:
        print("Belum ada target diupgrade")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

        pilih_upgrade = int(input("pilih no yang ingin di upgrade prosesnya")) 
        if 1 <= pilih_upgrade <= len(target_bulanan):
            progress_baru = int(input("Masukkan progress baru (0-100): "))
        target_bulanan[pilih_upgrade-1][1] = progress_baru
        print("Progress berhasil diupdate!")

        for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

        else:
            print("Nomor target tidak valid")

elif pilihan == "3":
    if not target_bulanan:
        print("Belum ada target untuk dihapus")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")
        pilih_hapus = int(input("pilih no yang ingin dihapus"))

        if 1 <= pilih_hapus <= len(target_bulanan):
            target_bulanan.pop(pilih_hapus-1)
            print("Target dihapus")

        if not target_bulanan:
            print("Daftar kosong")

        else:    
            for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

            else:
                print("Nomor tidak valid")

elif pilihan =="4":
    print("progam selesai,Terima kasih")

else:
    print("pilihan tidak ada")

lanjut = input("Mau lanjut mengisi? (yes/no)")

#pengulangan 2

if lanjut == "ya":
    print("=== Menu Target Bulanan ===")
    print("1. Tambah target")
    print("2. Upgrade progress")
    print("3. hapus daftar")
    print("4. Keluar")
else : "no"
("program selesai,terima kasih")

pilihan = input("Pilih menu (1-4): ")

if pilihan == "1":
    target = input("Masukkan target baru : ")
    target_bulanan.append([target, 0])
    print("Target ditambah!")

    for i in range(len(target_bulanan)):
        print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

elif pilihan == "2":
    if not target_bulanan:
        print("Belum ada target diupgrade")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

        pilih_upgrade = int(input("pilih no yang ingin di upgrade prosesnya")) 
        if 1 <= pilih_upgrade <= len(target_bulanan):
            progress_baru = int(input("Masukkan progress baru (0-100): "))
        target_bulanan[pilih_upgrade-1][1] = progress_baru
        print("Progress berhasil diupdate!")

        for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

        else:
            print("Nomor target tidak valid")

elif pilihan == "3":
    if not target_bulanan:
        print("Belum ada target untuk dihapus")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")
        pilih_hapus = int(input("pilih no yang ingin dihapus"))

        if 1 <= pilih_hapus <= len(target_bulanan):
            target_bulanan.pop(pilih_hapus-1)
            print("Target dihapus")

        if not target_bulanan:
            print("Daftar kosong")

        else:    
            for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

            else:
                print("Nomor tidak valid")

elif pilihan =="4":
    print("Program selesai,Terima kasih")

else:
    print("pilihan tidak ada")

lanjut = input("Mau lanjut mengisi? (yes/no)")

#pengulangan 3

if lanjut == "ya":
    print("=== Menu Target Bulanan ===")
    print("1. Tambah target")
    print("2. Upgrade progress")
    print("3. hapus daftar")
    print("4. Keluar")

else: 
    ("program selesai,terima kasih")

pilihan = input("Pilih menu (1-4): ")

if pilihan == "1":
    target = input("Masukkan target baru : ")
    target_bulanan.append([target, 0])
    print("Target ditambah!")

    for i in range(len(target_bulanan)):
        print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

elif pilihan == "2":
    if not target_bulanan:
        print("Belum ada target diupgrade")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")
        pilih_upgrade = int(input("pilih no yang ingin di upgrade prosesnya"))

        if 1 <= pilih_upgrade <= len(target_bulanan):
            progress_baru = int(input("Masukkan progress baru (0-100): "))
        target_bulanan[pilih_upgrade-1][1] = progress_baru
        print("Progress berhasil diupdate!")

        for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

        else:
            print("Nomor target tidak valid")


elif pilihan == "3":
    if not target_bulanan:
        print("Belum ada target untuk dihapus")
    else:
        for i in range(len(target_bulanan)):
            print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")
        pilih_hapus = int(input("pilih no yang ingin dihapus"))

        if 1 <= pilih_hapus <= len(target_bulanan):
            target_bulanan.pop(pilih_hapus-1)
            print("Target dihapus")

        if not target_bulanan:
            print("Daftar kosong")

        else:    
            for i in range(len(target_bulanan)):
                print(i+1, ".", target_bulanan[i][0], "-", target_bulanan[i][1], "%")

            else:
                print("Nomor tidak valid")

elif pilihan =="4":
    print("Program selesai,Terima kasih")

else:
    print("pilihan tidak ada")