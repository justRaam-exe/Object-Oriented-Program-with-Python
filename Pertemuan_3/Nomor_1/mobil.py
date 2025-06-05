from alat_transportasi import AlatTransportasi

class Mobil(AlatTransportasi):
    def __init__(self, nama: str, jumlahRoda: int):
        super().__init__(nama)
        self.jumlahRoda = jumlahRoda

    def bergerak(self) -> None:
        print("Mobil ini bergerak dengan 4 roda")