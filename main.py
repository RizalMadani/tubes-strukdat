import re
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
    print('3. Update Kontak')
    print('4. Cari Nama')
    print('5. Cari No. Telepon')
    print('6. Cari Alamat')
    print('7. Hapus Kontak')
    print('0. Exit')
    print()


def buat_kontak():
    nama   = input('> Nama : ').title()
    no     = _input_no()
    alamat = input('> Alamat (opsional)\t: ')

    bk.insert(nama, no, alamat)

    print('\r\n[✓] Kontak berhasil ditambahkan')


def tampilkan_semua(kontak):
    if kontak is None:
        print('[!] Tidak ada kontak')
        return

    i = 1
    while kontak is not None:
        no     = kontak.no if kontak.no != '' else '[Tidak ada No. Telp]'
        alamat = kontak.alamat if kontak.alamat else '[Tidak ada alamat]'

        print(f'{i}. {kontak.nama}, {no}, {alamat}')

        kontak = kontak.next
        i += 1


def tampilkan(kontak, is_numbering=False):
    if kontak == []:
        print('[!] Tidak ada kontak')
        return

    for i in range(len(kontak)):
        no     = kontak[i].no if kontak[i].no != '' else '[Tidak ada No. Telp]'
        alamat = kontak[i].alamat if kontak[i].alamat else '[Tidak ada alamat]'

        if is_numbering:
            print(f'{i+1}', sep='. ')

        print(f'{kontak[i].nama}, {no}, {alamat}')


def edit():
    print()
    tampilkan_semua(bk.head)
    print()

    while(True):
        try:
            pilihan = int(input('> Pilih kontak yang ingin di edit: '))

            if pilihan > 0 and pilihan <= bk.size:
                break
            else:
                print('\r\n[!] Pilihan melebihi batas')

        except ValueError:
            print('\r\n[!] Pilihan tidak valid')

    print('\r\n[i] Masukan data baru')
    print('[i] Tekan `enter` jika tidak ingin mengubah data tersebut')

    nama   = input('> Nama (opsional) : ').title()
    no     = _input_no()
    alamat = input('> Alamat (opsional)\t: ')

    teredit = bk.edit(pilihan, nama, no, alamat)

    print('\r\n[✓] Kontak berhasil diubah')

    tampilkan(teredit)


def hapus():
    print()
    tampilkan_semua(bk.head)
    print()

    while(True):
        try:
            pilihan = int(input('> Pilih kontak yang ingin di hapus: '))

            if pilihan > 0 and pilihan <= bk.size:
                break
            else:
                print('\r\n[!] Pilihan melebihi batas')

        except ValueError:
            print('\r\n[!] Pilihan tidak valid')

    while(True):
        konfirmasi = input('> Apakah Anda yakin ingin menghapus kontak ini? [y/n] : ')
        konfirmasi.lower()

        if konfirmasi == 'y':
            break
        elif konfirmasi == 'n':
            print('[!] Dibatalkan')
            return
        else:
            print('\r\n[!] Pilihan tidak valid')
    
    bk.hapus(pilihan)

    print('\r\n[✓] Kontak berhasil dihapus')


def cari(atribut):
    label  = LABEL[atribut]
    dicari = input(f'> {label} yang ingin dicari: ').lower()

    result = bk.find(atribut, dicari)

    print(f'\r\n[i] Hasil Pencarian Kontak dengan {label} "{dicari}"\r\n')
    tampilkan(result)


def _input_no():
    """
    Input dan validasi No. Telp
    """

    while(True):
        no = input('> No. Telp (opsional)\t: ')

        # Cek jika no yang diinput hanya mengandung:
        # tanda + - ( ) spasi dan karakter digit
        if no == '' or re.search('^(\+(\(\d+\))*)?[\d -]{9,}[\d]$', no):
            return no
        else:
            print('\r\n[!] No. Telp tidak valid')


if __name__ == '__main__':
    bk.insert('Amanda Amethyst', '0812344321', 'Jl. Garuda No. 2')
    bk.insert('Dina Diamond', '081232425262', 'Jl. Cendrawasih')
    bk.insert('Jessica Jade', '082313739303', 'Di sini')
    bk.insert('Silvi Shapire', '0898766789', 'Jl. Merpati A10')

    while(True):
        display_menu()

        try:
            pilihan = int(input('> Pilih menu : '))

            if pilihan == 1:
                buat_kontak()
            elif pilihan == 2:
                print('\r\n~~~ Daftar Kontak ~~~')
                tampilkan_semua(bk.head)
            elif pilihan == 3:
                edit()
            elif pilihan == 4:
                cari('nama')
            elif pilihan == 5:
                cari('no')
            elif pilihan == 6:
                cari('alamat')
            elif pilihan == 7:
                hapus()
            elif pilihan == 0:
                break
            else:
                print('[!] Pilihan tidak ada di menu')
        except ValueError:
            print('[!] Pilihan tidak valid')

    exit()
        