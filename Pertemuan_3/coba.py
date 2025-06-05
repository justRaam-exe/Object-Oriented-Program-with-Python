n = int(input('Masukkan input n: '))

width = n * 2 - 3

for i in range(n):
    for j in range(width):
        if i == 0 or i == n - 1:
            print('*', end=' ')
        elif j == i or j == width - i - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()