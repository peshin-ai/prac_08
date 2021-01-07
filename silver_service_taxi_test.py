from silver_service_taxi import SilverServiceTaxi


def main():
    Hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(Hummer.__str__())

if __name__ == '__main__':
    main()