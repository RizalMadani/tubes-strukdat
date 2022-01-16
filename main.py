from buku_kontak import BukuKontak

bk = BukuKontak()


def display_menu():
    print()
    print('1. Masukan kontak baru')
    print('2. Tampilkan daftar kontak')
    print('3. Cari kontak berdasarkan nama')
    print('0. Exit')
    print()

def buat_kontak():
    nama   = input('> Nama : ')
    no     = input('> No. Telp (opsional)\t: ')
    alamat = input('> Alamat (opsional)\t: ')

    bk.insert(nama, no, alamat)

    print('\r\n[✓] Kontak berhasil ditambahkan')

def tampil_kontak(kontak):
    if kontak is None:
        print('[!] Tidak ada kontak')
        return

    i = 1
    while kontak is not None:
        print(f'{i}. {kontak.nama}, {kontak.no}, {kontak.alamat}')

        kontak = kontak.next
        i += 1

# def tampil_kontak():
#     if bk.head is None:
#         print('\r\n[!] Belum ada kontak dalam buku')
#         return

#     print('\r\nDAFTAR KONTAK')

#     temp = bk.head
#     i    = 1
#     while temp is not None:
#         print(f'{i}. {temp.nama}, {temp.no}, {temp.alamat}')

#         temp = temp.next
#         i += 1

def cari_nama():
    nama_dicari = input('> Nama yang ingin dicari: ')

    result = bk.find_by_nama(nama_dicari)

    print(f'\r\nHasil Pencarian Kontak dengan Nama "{nama_dicari}"')
    tampil_kontak(result)

if __name__ == '__main__':
    bk.insert('Bebas', '08', 'Di sina')
    bk.insert('Lebah', '09', 'Di situ')

    while(True):
        display_menu()

        try:
            pilihan = int(input('> Pilih menu : '))

            if pilihan == 1:
                buat_kontak()
            elif pilihan == 2:
                print('\r\n~~~Daftar Kontak~~~')
                tampil_kontak(bk.head)
            elif pilihan == 3:
                cari_nama()
            elif pilihan == 0:
                break
            else:
                break
        except:
            print('\r\n[!] Pilihan tidak valid')

    exit()
        