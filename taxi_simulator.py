from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def Drive():
    global Total
    distance = int(input("Drive how far? "))
    car_choice.drive(distance)
    print(car_choice.__str__())
    Total += Bill_todate(True)
    print('Bill to date: ${:.2f}'.format(Total))
    menu()


def Bill_todate(boolean):
    fee_of_service = 0
    if boolean:
        fee_of_service += car_choice.get_fare()
    else:
        fee_of_service = car_choice.display_fee()
    return fee_of_service


def choose_taxi():
    global car_choice, Total
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i].__str__()))

    number = int(input("Choose taxi: "))
    car_choice = taxis[number]
    Total += Bill_todate(False)
    print('Bill to date: ${:.2f}'.format(Total))
    menu()


def navigate(char):
    if char == "Q":
        pass
    if char == "C":
        choose_taxi()
    if char == "D":
        Drive()


def menu():
    print('q)uit, c)hoose taxi, d)rive')
    choose = input().upper()
    navigate(choose)


def main():
    global taxis
    global Total
    Total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print('Let\'s drive! ')
    menu()


if __name__ == '__main__':
    main()
