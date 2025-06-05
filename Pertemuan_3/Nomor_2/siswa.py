from pelajar import Pelajar

class Siswa(Pelajar):
    def __init__(self, nama, umur, kelas, kodeBelajar: int):
        super().__init__(nama, umur, kelas)
        self.kodeBelajar = kodeBelajar
        
    def belajar(self) -> None:
        print("Siswa ini belajar")
        