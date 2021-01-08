from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel=0, fanciness=1):
        super().__init__(name, fuel)
        self.price_per_km = super().get_price_per_km() * fanciness
        self.flagfall = 4.5
        self.fee = 0
        self.display = 0

    def drive(self, distance):
        super().drive(distance)

    def get_fare(self):
        self.fee = super().get_fare() + 4.5
        self.display = self.fee
        return self.fee

    def display_fee(self):
        return super().display_fee()



    def __str__(self):
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)
