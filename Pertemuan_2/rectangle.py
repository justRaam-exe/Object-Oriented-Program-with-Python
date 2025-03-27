from shape import Shape

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        # self.panjang
        # self.lebar
        # self.luas
        
    def input_area(self):
        self.panjang = float(input('Masukkan input Panjang : '))
        self.lebar = float(input('Masukkan input Lebar : '))
        
    def area_answer(self):
        self.luas = self.panjang * self.lebar