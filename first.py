import pyxel
import cupid
#import cupid2
#import cupid3
import mapset
import mobs

class Running:


    player = None

    def __init__(self):
        #pyxel.init(192,160)
        pyxel.init(160, 128)
        self.testload = 0
        self.testmapx = 0
        self.testmapy = 0
        self.x = 0
        self.y = 70
        self.xr = 0
        self.walking = False
        self.mob = mobs.Mobs()
        # self.player = cupid3.CupidThree()
        # self.player = cupid2.CupidTwo()
        self.player = cupid.cupid()
        self.map = mapset.mapset()
        pyxel.load('attempt.pyxel')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update(self.map)
        self.map.update(self.player)
        self.mob.update(self.map, self.player)

    def draw(self):
        # render map
        pyxel.bltm(self.map.render[0], self.map.render[1], 2,
                   2,
                   self.map.tile[0],
                   self.map.tile[1],
                   25,
                   21)
        # render shadows
        pyxel.bltm(self.player.render[0] + 4, self.player.render[1] + 8, 0, 0, 2 if self.player.walkAnim else 0, 8, 2, 2, 0)


        # render mobs
        for car in self.mob.cars_west:
            pyxel.bltm(car.render[0], car.render[1], 0, 0, car.animation[0], car.animation[1], 4, 2, 3)
        for car in self.mob.cars_east:
            pyxel.bltm(car.render[0], car.render[1], 0, 0, car.animation[0], car.animation[1], 4, 2, 3)
        # render player





        pyxel.bltm(self.player.render[0], self.player.render[1], 0,
                   0,
                   self.player.sprite[0],
                   self.player.sprite[1],
                   2,
                   2,
                   14)
        #render occlusion
        for tile in self.map.occlusionList:
            pyxel.bltm(tile[0], tile[1], 2, 2, tile[2], tile[3], 1, 1, tile[4])

        self.map.occlusionList = []

        for bolt in self.player.arrows:
           pyxel.bltm(bolt.x, bolt.y, 1, 0, bolt.sprite[0], bolt.sprite[1], 2, 2, 0)
        #pyxel.blt(0,0,1, self.testmapx, self.testmapy, 96, 16)
        #pyxel.blt(self.player.render[0], self.player.render[1], 0, self.player.sprite[0], self.player.sprite[1], 32, 32, 14)



        # Debug Function
        #pyxel.text(80, 5, str(self.player.true_X), 11)
        # for squares in range(self.player.tile, (self.player.tile + 200 + 1), 200):
        #     for value in range(squares, squares + 2, 1):
        #         pyxel.text(80, loc, str(value), 11)
        #         loc += 5
        # pyxel.text(80, loc, str(self.player.render[0]) + "," + str(self.player.render[1]), 11)
        # loc += 5
        loc = 5
        pyxel.text(80, loc, str(self.player.render), 11)
        loc += 5
        pyxel.text(80, loc, str(self.player.true_location), 11)
        loc +=5
        pyxel.text(80, loc, str(self.player.tile), 11)

        #for tiles in self.player.possible_bump:
        #   loc += 5
        #   pyxel.text(80, loc, str(tiles), 11)


if __name__ == "__main__":
    Running();
