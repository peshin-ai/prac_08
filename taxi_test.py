from taxi import Taxi


def main():

    Prius_1 = Taxi("Prius 1", 100, 1.23)
    Prius_1.drive(40)
    print(Prius_1.__str__())


if __name__ == '__main__':
    main()