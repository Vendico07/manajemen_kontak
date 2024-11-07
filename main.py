"Program Manajemen Kontak"

kontak1 = {'nama' : "Andi", 'HP' : "123456789", 'email' : "Andi@python.com"}
kontak2 = {'nama' : "Budi", 'HP' : "123332123", 'email' : "Budi@python.com"}
kontak = [kontak1,kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat menu kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. keluar dari kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 dan 4): ")

    if pilihan == '1':
        #melihat semua kontak
        if kontak:
           for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")

    elif pilihan == '2':
        #menambahkan kontak
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomor HP yang baru: ")
        email = input("Masukan Email kontak yang baru: ")
        kontak_baru = {'nama':nama, 'HP': HP, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")
    elif pilihan == '3':
        #menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus")
    elif pilihan == '4':
        #keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah!")