"Program Manajemen Kontak"
import kontak

def main():
    kontak_kantor = kontak.kontak()
    kontak_keluarga = kontak.kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Melihat menu kontak")
        print("2. Menambahkan kontak baru")
        print("3. Menghapus kontak")
        print("4. keluar dari kontak")

        pilihan = input("Masukan pilihan menu kontak (1,2,3 dan 4): ")

        if pilihan == '1':
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()

        elif pilihan == '4':
            #keluar dari
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukan pilihan yang salah!")

if __name__ == "__main__":
    main()