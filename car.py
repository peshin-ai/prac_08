"""
CP1404/CP5632 Practical
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)



    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def set_odometer(self):
        self.odometer = 0
        return self.odometer

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.odometer += distance
            self.fuel = 0
        else:
            self.fuel -= distance
            self.odometer += distance
        return distance


