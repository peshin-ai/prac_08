from unreliable_car import UnreliableCar

def main():
    Honda = UnreliableCar("Honda", 100, 30)
    print(Honda.drive())

if __name__ == '__main__':
    main()