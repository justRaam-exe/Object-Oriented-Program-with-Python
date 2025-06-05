class Pelajar():
    def __init__(self, nama: str, alamat: str, gender: str):
        self.nama = nama
        self.alamat = alamat
        self.gender = gender
        
    def belajar(self) -> None:
        print("Pelajar ini belajar")