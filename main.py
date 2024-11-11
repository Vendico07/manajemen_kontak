"Program Manajemen Kontak"

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukan nama kontak yang baru: ")
    HP = input("Masukan nomor HP yang baru: ")
    email = input("Masukan Email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus")


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
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        #keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah!")