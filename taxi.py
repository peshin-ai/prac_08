"""
CP1404/CP5632 Practical
Car class
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = 1.20
        self.display = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_price_per_km(self):
        return self.price_per_km

    def get_fare(self):
        """Return the price for the taxi trip."""
        self.display = self.price_per_km * self.current_fare_distance
        return self.price_per_km * self.current_fare_distance

    def display_fee(self):
        return self.display

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        self.current_fare_distance = super().set_odometer()
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven