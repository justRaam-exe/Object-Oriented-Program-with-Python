from alat_transportasi import AlatTransportasi

class Motor(AlatTransportasi):
    def __init__(self, nama: str, jumlahRoda: int):
        super().__init__(nama)
        self.jumlahRoda = jumlahRoda
        
    def bergerak(self) -> None:
        print('Motor ini bergerak dengan 2 roda')