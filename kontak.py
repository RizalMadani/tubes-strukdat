class Kontak:
    """
    Class yang menjadi node dalam linked list.
    Class Kontak menyimpan data seperti:
    - nama
    - no (opsional)
    - alamat (opsional)
    """

    def __init__(self, nama, no, alamat) -> None:
        self.nama   = nama
        self.no     = no
        self.alamat = alamat
        self.next   = None