class Hewan():
    def __init__(self, nama : str):
        self.nama = nama
    
    def bersuara(self) -> None:
        print("Hewan utama ini bersuara")
    
    def bergerak(self) -> None:
        print("Hewan utama ini bergerak")
    
    def tidur(self) -> None:
        print("Hewan utama ini tidur")