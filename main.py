from buku_kontak import BukuKontak

bk    = BukuKontak()
LABEL = {
    'nama'   : 'Nama',
    'no'     : 'No. Telepon',
    'alamat' : 'Alamat'
}


def display_menu():
    print()
    print('1. Masukan Kontak Baru')
    print('2. Tampilkan Daftar Kontak')
    print('3. Cari Nama')
    print('4. Cari No. Telepon')
    print('5. Cari Alamat')
    print('0. Exit')
    print()

def buat_kontak():
    nama   = input('> Nama : ').title()
    no     = _input_no()
    alamat = input('> Alamat (opsional)\t: ')

    bk.insert(nama, no, alamat)

    print('\r\n[✓] Kontak berhasil ditambahkan')

def tampilkan(kontak):
    if kontak is None:
        print('[!] Tidak ada kontak')
        return

    i = 1
    while kontak is not None:
        print(f'{i}. {kontak.nama}, {kontak.no}, {kontak.alamat}')

        kontak = kontak.next
        i += 1

# deprecated
def cari_nama():
    nama_dicari = input('> Nama yang ingin dicari: ')

    result = bk.find('nama', nama_dicari)

    print(f'\r\nHasil Pencarian Kontak dengan Nama "{nama_dicari}"')
    tampilkan(result)

def cari(atribut):
    label  = LABEL[atribut]
    dicari = input(f'> {label} yang ingin dicari: ').lower()

    result = bk.find(atribut, dicari)

    print(f'\r\nHasil Pencarian Kontak dengan {label} "{dicari}"')
    tampilkan(result)

def _input_no():
    """
    Input dan validasi No. Telp
    """

    while(True):
        no = input('> No. Telp (opsional)\t: ')

        if no.isnumeric():
            return no
        else:
            print('\r\n[!] No. Telp tidak valid')


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
                tampilkan(bk.head)
            elif pilihan == 3:
                cari('nama')
            elif pilihan == 4:
                cari('no')
            elif pilihan == 5:
                cari('alamat')
            elif pilihan == 0:
                break
            else:
                print('[!] Pilihan tidak ada di menu')
        except ValueError:
            print('[!] Pilihan tidak valid')

    exit()
        