from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

print('''
Ini adalah program untuk menghitung luas bangun datar
Silahkan Pilih program yang akan dijalankan:
1. Luas Persegi Panjang
2. Luas Segitiga
3. Luas Lingkaran''')

def main():
    user_choice = int(input("Masukkan pilihan Anda: "))
    if user_choice == 1:
        print('====================')
        print('Luas Persegi Panjang')
        print('====================')
        rect = Rectangle()
        rect.input_area()
        rect.area_answer()
        print(f"Luas Persegi Panjang adalah {rect.luas}")
    elif user_choice == 2:
        print('=============')
        print('Luas Segitiga')
        print('=============')
        tri = Triangle()
        tri.input_area()
        tri.area_answer()
        print(f"Luas Segitiga adalah {tri.luas}")
    elif user_choice == 3:
        print('===============')
        print('Luas Lingkarang')
        print('===============')
        cir = Circle()
        cir.input_area()
        cir.area_answer()
        print(f"Luas Lingkaran adalah {cir.luas}")
    else:
        print("Pilihan tidak valid, Program Berhenti. Terima kasih!")
        
if __name__ == "__main__":
    main()