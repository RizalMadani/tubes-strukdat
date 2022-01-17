from kontak import Kontak

class BukuKontak:
    """
    Class yang menjadi linked list
    """
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert(self, nama, no='', alamat='') -> None:
        """
        Masukan kontak ke dalam buku di awal linked list
        """

        kontak = Kontak(nama, no, alamat)

        if self.head is None:
            self.head = kontak
        else:
            kontak.next = self.head
            self.head = kontak

        self.size += 1

    # deprecated
    def find_by_nama(self, nama_dicari):
        """
        Cari kontak berdasarkan nama
        """

        temp   = self.head
        result = None

        while temp is not None:
            if temp.nama.find(nama_dicari) != -1:
                if result is None:
                    result = temp
                else:
                    result.next = temp

            temp = temp.next

        return result

    def find(self, atribut, yang_dicari):
        """
        Cari kontak berdasarkan data yang dicari.

        Pencarian tidak harus menggunakan kata yang lengkap
        """

        temp   = self.head
        result = []

        while temp is not None:
            if getattr(temp, atribut).lower().find(yang_dicari) != -1:
                # if result is None:
                #     result = temp
                # else:
                #     result.next = temp

                result.append(temp)

            temp = temp.next

        return result

    def edit(self, indeks, nama='', no='', alamat=''):
        """
        Edit kontak berdasarkan indeks/urutan dalam daftar.

        Return kontak yang telah diedit
        """

        temp = self.head
        i    = 0

        while i < indeks-1:
            temp = temp.next

        if nama != '':
            temp.nama = nama
        if no != '':
            temp.no = no
        if alamat != '':
            temp.alamat = alamat

        return [temp]
    
    def hapus(self, indeks):
        """
        Hapus kontak berdasarkan indeks/urutan dalam daftar
        """

        temp = self.head

        if indeks == 1:
            self.head = temp.next
            temp = None
            return

        i = 0
        while i < indeks-2:
            temp = temp.next
        
        temp.next = temp.next.next
