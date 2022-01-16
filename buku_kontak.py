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

    # def display(self):
    #     if self.head is None:
    #         return ['Belum ada kontak dalam buku']