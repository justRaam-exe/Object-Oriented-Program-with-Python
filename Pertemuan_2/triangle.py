from shape import Shape

class Triangle(Shape):
    def __init__(self):
        super().__init__()
        # self.alas
        # self.tinggi
        # self.luas
        
    def input_area(self):
        self.alas = float(input('Masukkan input Alas : '))
        self.tinggi = float(input('Masukkan input Tinggi : '))
        
    def area_answer(self):
        self.luas = 0.5 * self.alas * self.tinggi