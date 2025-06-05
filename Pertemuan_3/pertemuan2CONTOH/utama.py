from ular import Ular
from anjing import Anjing

def main():
    ular1 = Ular("Ular Kobra", "Hitam")
    ular1.bersuara()
    ular1.bergerak()
    ular1.tidur()

    anjing1 = Anjing("Anjing Husky", "Putih")
    anjing1.bersuara()
    anjing1.bergerak()
    anjing1.tidur()


if __name__ == "__main__":
    main()
