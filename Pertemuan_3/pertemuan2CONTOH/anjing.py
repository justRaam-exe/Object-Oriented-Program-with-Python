
from hewan import Hewan

class Anjing(Hewan):
    def __init__(self, nama : str, warnaBulu : str):
        super().__init__(nama)
        self.warnaBulu = warnaBulu
    
    def bersuara(self) -> None:
        super().bersuara()
        print("Guk Guk")
    
    def bergerak(self) -> None:
        super().bergerak()
        print("Anjing ini bergerak")
    
    def tidur(self) -> None:
        print("Anjing ini tidur")