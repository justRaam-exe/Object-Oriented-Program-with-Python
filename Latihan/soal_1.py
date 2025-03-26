class left_pyramid:
    def __init__(self, n : int):
        self.n = n
        
    def run_left_pyramid(self):
        # for i in range(1, self.n + 1):
        #     print('*' * i)
        for i in range(1, self.n + 1):
            for j in range(1, i + 1):
                print('* ', end='')
            print()

