from shape import Shape

class Circle(Shape):
    def __init__(self):
        super().__init__()
        # self.jari
        # self.luas
        
    def input_area(self):
        self.jari = float(input('Masukkan input Jari-jari : '))
        
    def area_answer(self):
        self.luas = 3.14 * self.jari * self.jari
        