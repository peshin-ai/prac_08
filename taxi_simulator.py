from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def choosetaxi():
    for i in range(len(taxis)):
        print(taxis[i].__str__())

def navigate(char):
    if char == "Q":
        choosetaxi()
    if char == "C":
        pass
    if char == "D":
        pass

def main():
    global taxis
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print('Let\'s drive! ')
    print('q)uit, c)hoose taxi, d)rive')
    choose = input().upper()
    navigate(choose)

if __name__ == '__main__':
    main()