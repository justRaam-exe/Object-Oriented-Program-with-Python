from mahasiswa import Mahasiswa
from siswa import Siswa

def main() -> None:
    mahasiswa = Mahasiswa("Ali", "Jl. Merdeka No. 1", "Laki-laki", 486910)
    mahasiswa.belajar()
    
    siswa1 = Siswa("Sonya", 'Jl. Merdeka No. 2', 'Perempuan', 196840)
    siswa1.belajar()
    
if __name__ == "__main__":
    main()