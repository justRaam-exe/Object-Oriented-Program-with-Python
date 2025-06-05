from pelajar import Pelajar

class Mahasiswa(Pelajar):
    def __init__(self, nama, alamat, gender, nrp: int):
        super().__init__(nama, alamat, gender)
        self.nrp = nrp
        
    def belajar(self) -> None:
        print("Mahasiswa ini belajar")