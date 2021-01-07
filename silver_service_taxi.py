from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel=0):
        super().__init__(name, fuel)
        self.fanciness = 2
        self.price_per_km = super().get_price_per_km() * 4
        self.flagfall = 4.5

    def drive(self, distance):
        super().drive(distance)

    def __str__(self):
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)
