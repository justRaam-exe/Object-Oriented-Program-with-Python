from soal_1 import left_pyramid as LP
from soal_2 import inv_pyramid as IP
from soal_3 import prime_num as PN

print('''
Selamat Datang User, ini adalah tugas Object Orienter Programming (OOP) Python
Silahkan pilih program yang ingin dijalankan:
1. Pyramid
2. Inverted Pyramid
3. Prime Number
4. Exit''')

def main():
    choice = int(input("Masukkan pilihan Anda: "))
    if choice == 1:
        n = int(input("Enter the number of rows: "))
        Lpyramid = LP(n)
        Lpyramid.run_left_pyramid()
    elif choice == 2:
        m = int(input("Enter the number of rows: "))
        inv_pyramid = IP(m)
        inv_pyramid.run_inv_pyramid()
    elif choice == 3:
        n = int(input("Masukkan bilangan: "))
        prima = PN(n)
        if prima.cekPrima():
            print(f"{n} adalah bilangan prima")
        else:
            print(f"{n} bukan bilangan prima")
    elif choice == 4:
        print('Program telah berhenti, Terima kasih')
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()