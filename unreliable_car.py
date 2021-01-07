from car import Car
from random import randint

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.min = 0
        self.max = 100

    def drive(self):

        RandomNumber = randint(self.min, self.max)

        if RandomNumber > self.reliability:
            distance_driven = super().drive(RandomNumber)
        else:
            distance_driven = 0

        return distance_driven