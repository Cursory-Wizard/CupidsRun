import pyxel
import random
import cars

class Mobs:

    def __init__(self):
        self.cars_west = []
        self.cars_east = []
        self.mobs = []

    def update(self, maps, player):

        # start with cars
        # check to see if cars in viewport
        if maps.true_location[1] < 128:
            # check to see how many cars are on the road heading west. If less than 2, try to spawn one.
            if len(self.cars_west) < 2:
                if len(self.cars_west) == 0:
                    self.cars_west.append(cars.Cars(144 - maps.true_location[0], 74 - maps.true_location[1], 0))
                # check to make sure the previous car is at least 1 car length ahead
                if self.cars_west[len(self.cars_west) - 1].render[0] < 102:
                    rnd = random.randint(0, 50)
                    if rnd > 40:
                        if rnd > 46:
                            choice = 0
                        else:
                            choice = 3
                        self.cars_west.append(cars.Cars(144 - maps.true_location[0], 74 - maps.true_location[1], choice))

            # check to see how many cars are on the road heading east. If less than 2, try to spawn one.
            if len(self.cars_east) < 2:
                if len(self.cars_east) == 0:
                    self.cars_east.append(cars.Cars(-32 - maps.true_location[0], 98 - maps.true_location[1], 0))
                if self.cars_east[len(self.cars_east) - 1].render[0] > 40:
                    rnd = random.randint(0, 50)
                    if rnd > 40:
                        if rnd > 46:
                            choice = 0
                        else:
                            choice = 3
                        self.cars_east.append(cars.Cars(-32  - maps.true_location[0], 98 - maps.true_location[1], choice))
        # build two lists of all cars heading east and west, removing cars that have passed out of view
        self.cars_west = [car for car in self.cars_west if car.render[0] > -32]
        for car in self.cars_west:
            car.update_west(maps)
        self.cars_east = [car for car in self.cars_east if car.render[0] < 145]
        for car in self.cars_east:
            car.update_east(maps)


