"Program Manajemen Kontak"

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)

class kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}.' + item)
        else:
            print("Kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomor HP yang baru: ")
        email = input("Masukan Email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah dihapus")
            except:
                print("Input yang anda masukan salah!")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

kontak_kantor = kontak()
kontak_keluarga = kontak()

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