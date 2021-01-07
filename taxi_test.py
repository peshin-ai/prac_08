from taxi import Taxi


def main():

    Prius_1 = Taxi("Prius 1", 100)
    Prius_1.drive(60)
    print(Prius_1.__str__())
    print(Prius_1.get_fare())
    Prius_1.drive(100)
    print(Prius_1.__str__())
    print(Prius_1.get_fare())


if __name__ == '__main__':
    main()