from hewan import Hewan


class Ular(Hewan):
    def __init__(self, nama : str, warnaKulit : str):
        super().__init__(nama)
        self.warnaKulit = warnaKulit
    def bersuara(self) -> None:
        print("Ular ini mendesis")
    
    def bergerak(self) -> None:
        print("Ular ini bergerak")
    
    def tidur(self) -> None:
        print("Ular ini tidur")        
