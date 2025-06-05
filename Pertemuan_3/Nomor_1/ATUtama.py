from mobil import Mobil
from motor import Motor

def main():
    mobil1 = Mobil("Mobil Avanza", 4)
    mobil1.bergerak()
    
    motor1 = Motor("Motor Yamaha", 2)
    motor1.bergerak()
    
if __name__ == "__main__":
    main()