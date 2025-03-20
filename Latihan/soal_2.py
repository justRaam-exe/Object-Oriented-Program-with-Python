class inv_pyramid:
    def __init__(self, m : int):
        self.m = m
        
    def run_inv_pyramid(self):
        for i in range(self.m, 0, -1):
            for j in range(1, i + 1):
                print('* ', end='')
            print()
            
if __name__ == "__main__":
    m = int(input("Enter the number of rows: "))
    inv_pyramid = inv_pyramid(m)
    inv_pyramid.run_inv_pyramid()