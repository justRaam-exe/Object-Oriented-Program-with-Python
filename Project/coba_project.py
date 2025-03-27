import random

class Dadu:
    def lempar(self):
        return random.randint(1, 6)

class Papan:
    def __init__(self):
        self.ular = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.tangga = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    def cek_posisi(self, posisi):
        if posisi in self.ular:
            print(f"Oops! Ular di {posisi} menggigit, turun ke {self.ular[posisi]}")
            return self.ular[posisi]
        elif posisi in self.tangga:
            print(f"Yeay! Tangga di {posisi}, naik ke {self.tangga[posisi]}")
            return self.tangga[posisi]
        return posisi

class Pemain:
    def __init__(self, nama):
        self.nama = nama
        self.posisi = 0

    def maju(self, langkah, papan):
        self.posisi += langkah
        if self.posisi > 100:
            self.posisi -= langkah  # Tidak bisa lebih dari 100
        else:
            self.posisi = papan.cek_posisi(self.posisi)
        print(f"{self.nama} sekarang di posisi {self.posisi}")

class Game:
    def __init__(self, pemain):
        self.papan = Papan()
        self.dadu = Dadu()
        self.pemain = [Pemain(nama) for nama in pemain]

    def mulai(self):
        selesai = False
        while not selesai:
            for pemain in self.pemain:
                print('=============================================')
                input(f"{pemain.nama}, tekan Enter untuk melempar dadu...")
                langkah = self.dadu.lempar()
                print(f"{pemain.nama} melempar dadu: {langkah}")
                pemain.maju(langkah, self.papan)
                if pemain.posisi == 100:
                    print(f"Selamat {pemain.nama}! Kamu menang! 🏆")
                    selesai = True
                    break

# Memulai game dengan dua pemain
game = Game(["Alice", "Bob"])
game.mulai()
